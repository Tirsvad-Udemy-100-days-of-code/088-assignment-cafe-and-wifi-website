"""Integration test: the WSGI app against a copy of the real database."""

import shutil
from pathlib import Path
from typing import Any
from wsgiref.util import setup_testing_defaults

import pytest

from cafe_wifi.__main__ import resolve_database_path
from cafe_wifi.constants import CAFE_WIFI_DB_ENV, CONTENT_TYPE_HTML
from cafe_wifi.presentation.app import create_app

REAL_DB = Path(__file__).resolve().parents[2] / "data" / "cafes.db"


def call(
    app: Any, method: str = "GET", path: str = "/"
) -> tuple[str, dict[str, str], str]:
    """Call a WSGI app and return status, headers and decoded body."""
    environ: dict[str, Any] = {"REQUEST_METHOD": method, "PATH_INFO": path}
    setup_testing_defaults(environ)
    captured: dict[str, Any] = {}

    def start_response(status: str, headers: list[tuple[str, str]]) -> None:
        captured["status"] = status
        captured["headers"] = dict(headers)

    body = b"".join(app(environ, start_response))
    return captured["status"], captured["headers"], body.decode("utf-8")


@pytest.fixture
def app(tmp_path: Path) -> Any:
    database = tmp_path / "cafes.db"
    shutil.copy(REAL_DB, database)
    return create_app(database)


def test_home_lists_all_21_cafes(app: Any) -> None:
    status, headers, body = call(app)
    assert status == "200 OK"
    assert headers["Content-Type"] == CONTENT_TYPE_HTML
    assert body.count('<article class="card">') == 21


def test_home_has_no_replacement_character(app: Any) -> None:
    _, _, body = call(app)
    assert "\ufffd" not in body
    assert "\u00a3" in body


def test_unknown_path_is_404(app: Any) -> None:
    assert call(app, path="/missing")[0] == "404 Not Found"


def test_post_is_405(app: Any) -> None:
    assert call(app, method="POST")[0] == "405 Method Not Allowed"


def test_head_has_empty_body(app: Any) -> None:
    status, _, body = call(app, method="HEAD")
    assert status == "200 OK"
    assert body == ""


def test_resolve_database_path_uses_environment(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv(CAFE_WIFI_DB_ENV, str(tmp_path / "x.db"))
    assert resolve_database_path() == tmp_path / "x.db"


def test_resolve_database_path_defaults_to_data_file(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(CAFE_WIFI_DB_ENV, raising=False)
    assert resolve_database_path() == REAL_DB
