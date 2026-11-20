"""Integration test: the delete cafe flow through the WSGI app on a database copy."""

import shutil
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any

import pytest
from tests.integration.test_list_page import REAL_DB, call

from cafe_wifi.presentation.app import create_app

CARD = '<article class="card">'


@pytest.fixture
def database(tmp_path: Path) -> Path:
    path = tmp_path / "cafes.db"
    shutil.copy(REAL_DB, path)
    return path


@pytest.fixture
def app(database: Path) -> Any:
    return create_app(database)


def first_cafe(database: Path) -> tuple[int, str]:
    with closing(sqlite3.connect(database)) as connection:
        row = connection.execute("SELECT id, name FROM cafe ORDER BY id").fetchone()
    return int(row[0]), str(row[1])


def count(database: Path) -> int:
    with closing(sqlite3.connect(database)) as connection:
        return int(connection.execute("SELECT COUNT(*) FROM cafe").fetchone()[0])


def test_get_delete_shows_confirmation_with_cafe_name(app: Any, database: Path) -> None:
    cafe_id, name = first_cafe(database)
    status, _, body = call(app, path=f"/delete/{cafe_id}")
    assert status == "200 OK"
    assert name.replace("&", "&amp;") in body
    assert f'action="/delete/{cafe_id}"' in body
    assert count(database) == 21


def test_get_delete_never_deletes(app: Any, database: Path) -> None:
    cafe_id, _ = first_cafe(database)
    for method in ("GET", "GET", "HEAD", "GET"):
        call(app, method, f"/delete/{cafe_id}")
    assert count(database) == 21
    assert call(app)[2].count(CARD) == 21


def test_post_delete_redirects_and_cafe_leaves_the_list(
    app: Any, database: Path
) -> None:
    cafe_id, name = first_cafe(database)
    status, headers, _ = call(app, "POST", f"/delete/{cafe_id}")
    assert status == "303 See Other"
    assert headers["Location"] == "/"
    body = call(app)[2]
    assert body.count(CARD) == 20
    assert f'href="/delete/{cafe_id}"' not in body
    assert count(database) == 20
    assert call(app, path=f"/delete/{cafe_id}")[0] == "404 Not Found"
    assert name.replace("&", "&amp;") not in body.split("<main>")[1]


def test_post_delete_of_unknown_id_is_404_and_changes_nothing(
    app: Any, database: Path
) -> None:
    status, _, _ = call(app, "POST", "/delete/999999")
    assert status == "404 Not Found"
    assert count(database) == 21


def test_get_delete_of_unknown_id_is_404(app: Any) -> None:
    assert call(app, path="/delete/999999")[0] == "404 Not Found"


@pytest.mark.parametrize(
    "path", ["/delete/abc", "/delete/-1", "/delete/1/2", "/delete/" + "9" * 30]
)
def test_bad_delete_ids_are_404_and_change_nothing(
    app: Any, database: Path, path: str
) -> None:
    assert call(app, "GET", path)[0] == "404 Not Found"
    assert call(app, "POST", path)[0] == "404 Not Found"
    assert count(database) == 21


def test_home_has_a_delete_link_per_cafe(app: Any) -> None:
    body = call(app)[2]
    assert body.count(">Delete</a>") == 21
    assert body.count('<a href="/delete/') == 21


def test_put_delete_is_405_with_allow_header(app: Any, database: Path) -> None:
    status, headers, _ = call(app, "PUT", "/delete/1")
    assert status == "405 Method Not Allowed"
    assert headers["Allow"] == "GET, HEAD, POST"
    assert count(database) == 21
