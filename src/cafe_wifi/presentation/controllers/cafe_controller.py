"""Controller of the cafe pages.

@file cafe_controller.py
@brief Maps a request line to a use case call and a response.
"""

from cafe_wifi.application.use_cases.list_cafes import ListCafes
from cafe_wifi.constants import (
    ALLOW_HEADER_VALUE,
    ALLOWED_METHODS,
    HOME_PATH,
    STATUS_METHOD_NOT_ALLOWED,
    STATUS_NOT_FOUND,
    STATUS_OK,
    TEXT_METHOD_NOT_ALLOWED,
    TEXT_NOT_FOUND,
)
from cafe_wifi.presentation.controllers.response import Response
from cafe_wifi.presentation.views.cafe_views import render_cafe_list_page
from cafe_wifi.presentation.views.error_views import render_error_page


## @brief Answers requests for the cafe pages.
class CafeController:
    """Controller for GET / (the list of cafes)."""

    def __init__(self, list_cafes: ListCafes) -> None:
        """Keep the use case the home page needs.

        @param list_cafes Use case that returns all cafes.
        """
        self._list_cafes = list_cafes

    def handle(self, method: str, path: str) -> Response:
        """Return the response for a request.

        @param method HTTP method of the request.
        @param path Request path.
        @return 200 with the list, 404 for another path, 405 for another method.
        """
        if path != HOME_PATH:
            return Response(
                STATUS_NOT_FOUND,
                render_error_page(STATUS_NOT_FOUND, TEXT_NOT_FOUND),
            )
        if method not in ALLOWED_METHODS:
            return Response(
                STATUS_METHOD_NOT_ALLOWED,
                render_error_page(STATUS_METHOD_NOT_ALLOWED, TEXT_METHOD_NOT_ALLOWED),
                (("Allow", ALLOW_HEADER_VALUE),),
            )
        return Response(STATUS_OK, render_cafe_list_page(self._list_cafes.execute()))
