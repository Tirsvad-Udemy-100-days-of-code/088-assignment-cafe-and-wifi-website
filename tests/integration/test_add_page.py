"""Integration test: the add cafe flow through the WSGI app on a database copy."""

import shutil
import sqlite3
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import pytest
from tests.integration.test_list_page import REAL_DB, call

from cafe_wifi.presentation.app import create_app

CARD = '<article class="card">'
VALID = {
    "name": "Brand New Cafe",
    "location": "Bank",
    "map_url": "https://maps.example/x",
    "img_url": "https://img.example/x.jpg",
    "has_wifi": "on",
    "seats": "10-20",
    "coffee_price": "£2.50",
}


@pytest.fixture
def database(tmp_path: Path) -> Path:
    path = tmp_path / "cafes.db"
    shutil.copy(REAL_DB, path)
    return path


@pytest.fixture
def app(database: Path) -> Any:
    return create_app(database)


def submit(app: Any, form: dict[str, str]) -> tuple[str, dict[str, str], str]:
    return call(app, "POST", "/add", urlencode(form).encode())


def count(database: Path) -> int:
    with sqlite3.connect(database) as connection:
        return int(connection.execute("SELECT COUNT(*) FROM cafe").fetchone()[0])


def test_get_add_shows_empty_form(app: Any) -> None:
    status, _, body = call(app, path="/add")
    assert status == "200 OK"
    assert "<form" in body


def test_valid_post_redirects_and_cafe_is_listed(app: Any) -> None:
    status, headers, _ = submit(app, VALID)
    assert status == "303 See Other"
    assert headers["Location"] == "/"
    _, _, body = call(app)
    assert body.count(CARD) == 22
    assert "Brand New Cafe" in body
    assert "£2.50" in body


def test_invalid_post_shows_errors_and_stores_nothing(app: Any, database: Path) -> None:
    form = {**VALID, "name": "", "map_url": "ftp://x"}
    status, _, body = submit(app, form)
    assert status == "422 Unprocessable Content"
    assert "This field is required." in body
    assert "Enter a web address" in body
    assert 'value="ftp://x"' in body
    assert count(database) == 21


def test_duplicate_name_is_rejected(app: Any, database: Path) -> None:
    assert submit(app, VALID)[0] == "303 See Other"
    status, _, body = submit(app, VALID)
    assert status == "422 Unprocessable Content"
    assert "A cafe with this name already exists" in body
    assert count(database) == 22


def test_script_name_is_escaped_in_list_page(app: Any) -> None:
    submit(app, {**VALID, "name": "<script>alert(1)</script>"})
    _, _, body = call(app)
    assert "<script>alert(1)</script>" not in body
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in body


def test_injection_name_is_stored_as_text(app: Any, database: Path) -> None:
    submit(app, {**VALID, "name": "x'); DROP TABLE cafe;--"})
    assert count(database) == 22


def test_home_has_link_to_form(app: Any) -> None:
    assert '<a href="/add">Add a cafe</a>' in call(app)[2]


def test_put_add_is_405_with_allow_header(app: Any) -> None:
    status, headers, _ = call(app, "PUT", "/add")
    assert status == "405 Method Not Allowed"
    assert headers["Allow"] == "GET, HEAD, POST"
