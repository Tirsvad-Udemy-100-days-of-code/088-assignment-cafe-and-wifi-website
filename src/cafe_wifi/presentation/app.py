"""The WSGI application and its composition root.

@file app.py
@brief Builds the concrete objects of one request and serves the response.
"""

import sqlite3
from collections.abc import Callable, Iterable
from contextlib import closing
from pathlib import Path
from typing import Any

from cafe_wifi.application.use_cases.list_cafes import ListCafes
from cafe_wifi.constants import CONTENT_TYPE_HTML, RESPONSE_ENCODING
from cafe_wifi.infrastructure.persistence.sqlite_cafe_repository import (
    SqliteCafeRepository,
)
from cafe_wifi.presentation.controllers.cafe_controller import CafeController

## WSGI start_response callable.
StartResponse = Callable[..., Any]


## @brief Create the WSGI application for a database file.
#  @param database Path of the SQLite file.
#  @return A WSGI callable that opens one connection per request.
def create_app(
    database: Path,
) -> Callable[[dict[str, Any], StartResponse], Iterable[bytes]]:
    """Return the WSGI application reading cafes from the given database."""

    def app(environ: dict[str, Any], start_response: StartResponse) -> Iterable[bytes]:
        method = str(environ.get("REQUEST_METHOD", "GET"))
        path = str(environ.get("PATH_INFO", "/")) or "/"
        with closing(sqlite3.connect(database)) as connection:
            controller = CafeController(ListCafes(SqliteCafeRepository(connection)))
            response = controller.handle(method, path)
        body = response.body.encode(RESPONSE_ENCODING)
        headers = [
            ("Content-Type", CONTENT_TYPE_HTML),
            ("Content-Length", str(len(body))),
            *response.extra_headers,
        ]
        start_response(response.status, headers)
        return [] if method == "HEAD" else [body]

    return app
