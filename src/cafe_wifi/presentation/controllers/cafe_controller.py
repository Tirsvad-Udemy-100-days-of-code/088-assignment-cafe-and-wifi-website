"""Controller of the cafe pages.

@file cafe_controller.py
@brief Maps a request line and body to a use case call and a response.
"""

import re
from urllib.parse import parse_qs

from cafe_wifi.application.use_cases.add_cafe import AddCafe
from cafe_wifi.application.use_cases.delete_cafe import DeleteCafe
from cafe_wifi.application.use_cases.get_cafe import GetCafe
from cafe_wifi.application.use_cases.list_cafes import ListCafes
from cafe_wifi.constants import (
    ADD_ALLOW_HEADER_VALUE,
    ADD_ALLOWED_METHODS,
    ADD_PATH,
    ALLOW_HEADER_VALUE,
    ALLOWED_METHODS,
    DELETE_ALLOW_HEADER_VALUE,
    DELETE_ALLOWED_METHODS,
    DELETE_PATH_PATTERN,
    HEADER_LOCATION,
    HOME_PATH,
    MAX_BODY_BYTES,
    MAX_CAFE_ID,
    MAX_FORM_FIELDS,
    RESPONSE_ENCODING,
    STATUS_BAD_REQUEST,
    STATUS_CONTENT_TOO_LARGE,
    STATUS_METHOD_NOT_ALLOWED,
    STATUS_NOT_FOUND,
    STATUS_OK,
    STATUS_SEE_OTHER,
    STATUS_UNPROCESSABLE,
    TEXT_BAD_REQUEST,
    TEXT_CONTENT_TOO_LARGE,
    TEXT_METHOD_NOT_ALLOWED,
    TEXT_NOT_FOUND,
)
from cafe_wifi.presentation.controllers.response import Response
from cafe_wifi.presentation.views.add_cafe_views import render_add_form
from cafe_wifi.presentation.views.cafe_views import render_cafe_list_page
from cafe_wifi.presentation.views.delete_cafe_views import render_delete_confirmation
from cafe_wifi.presentation.views.error_views import render_error_page

_DELETE_PATH = re.compile(DELETE_PATH_PATTERN, re.ASCII)


def _parse_delete_id(path: str) -> int | None:
    """Return the cafe id of a delete path, or None when the path is not one."""
    match = _DELETE_PATH.fullmatch(path)
    if match is None:
        return None
    cafe_id = int(match.group(1))
    return cafe_id if cafe_id <= MAX_CAFE_ID else None


def _error_response(status: str, message: str) -> Response:
    """Return an error page response."""
    return Response(status, render_error_page(status, message))


def _not_allowed(allow: str) -> Response:
    """Return the 405 response that lists the allowed methods."""
    return Response(
        STATUS_METHOD_NOT_ALLOWED,
        render_error_page(STATUS_METHOD_NOT_ALLOWED, TEXT_METHOD_NOT_ALLOWED),
        (("Allow", allow),),
    )


def _parse_form(body: bytes) -> dict[str, str]:
    """Decode a urlencoded body to one value per field name.

    @throws ValueError When the body holds too many fields.
    """
    parsed = parse_qs(
        body.decode(RESPONSE_ENCODING, errors="replace"),
        keep_blank_values=True,
        max_num_fields=MAX_FORM_FIELDS,
    )
    return {name: values[0] for name, values in parsed.items()}


## @brief Answers requests for the cafe pages.
class CafeController:
    """Controller for GET / (the list), /add (the form) and /delete/<id>."""

    def __init__(
        self,
        list_cafes: ListCafes,
        add_cafe: AddCafe,
        get_cafe: GetCafe,
        delete_cafe: DeleteCafe,
    ) -> None:
        """Keep the use cases the pages need.

        @param list_cafes Use case that returns all cafes.
        @param add_cafe Use case that stores a new cafe.
        @param get_cafe Use case that returns one cafe.
        @param delete_cafe Use case that removes a cafe.
        """
        self._list_cafes = list_cafes
        self._add_cafe = add_cafe
        self._get_cafe = get_cafe
        self._delete_cafe = delete_cafe

    def handle(self, method: str, path: str, body: bytes = b"") -> Response:
        """Return the response for a request.

        @param method HTTP method of the request.
        @param path Request path.
        @param body Request body, read only for POST /add.
        @return The page, a 303 redirect, a 422 form with errors, 404 for another
        path or an unknown cafe id, or 405 for a method the path does not accept.
        """
        if path == HOME_PATH:
            return self._handle_home(method)
        if path == ADD_PATH:
            return self._handle_add(method, body)
        cafe_id = _parse_delete_id(path)
        if cafe_id is not None:
            return self._handle_delete(method, cafe_id)
        return _error_response(STATUS_NOT_FOUND, TEXT_NOT_FOUND)

    def _handle_home(self, method: str) -> Response:
        """Answer a request for the list of cafes."""
        if method not in ALLOWED_METHODS:
            return _not_allowed(ALLOW_HEADER_VALUE)
        return Response(STATUS_OK, render_cafe_list_page(self._list_cafes.execute()))

    def _handle_add(self, method: str, body: bytes) -> Response:
        """Answer a request for the add cafe form."""
        if method not in ADD_ALLOWED_METHODS:
            return _not_allowed(ADD_ALLOW_HEADER_VALUE)
        if method == "POST":
            return self._submit(body)
        return Response(STATUS_OK, render_add_form({}, {}))

    def _submit(self, body: bytes) -> Response:
        """Store the submitted cafe, or show the form again with the errors."""
        if len(body) > MAX_BODY_BYTES:
            return _error_response(STATUS_CONTENT_TOO_LARGE, TEXT_CONTENT_TOO_LARGE)
        try:
            form = _parse_form(body)
        except ValueError:
            return _error_response(STATUS_BAD_REQUEST, TEXT_BAD_REQUEST)
        errors = self._add_cafe.execute(form)
        if errors:
            return Response(STATUS_UNPROCESSABLE, render_add_form(form, errors))
        return Response(STATUS_SEE_OTHER, "", ((HEADER_LOCATION, HOME_PATH),))

    def _handle_delete(self, method: str, cafe_id: int) -> Response:
        """Answer a request for the delete page; only POST deletes."""
        if method not in DELETE_ALLOWED_METHODS:
            return _not_allowed(DELETE_ALLOW_HEADER_VALUE)
        if method == "POST":
            if not self._delete_cafe.execute(cafe_id):
                return _error_response(STATUS_NOT_FOUND, TEXT_NOT_FOUND)
            return Response(STATUS_SEE_OTHER, "", ((HEADER_LOCATION, HOME_PATH),))
        cafe = self._get_cafe.execute(cafe_id)
        if cafe is None:
            return _error_response(STATUS_NOT_FOUND, TEXT_NOT_FOUND)
        return Response(STATUS_OK, render_delete_confirmation(cafe))
