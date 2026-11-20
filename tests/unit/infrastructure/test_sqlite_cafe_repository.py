"""Tests of the SQLite cafe repository."""

import sqlite3
from collections.abc import Iterator

import pytest

from cafe_wifi.infrastructure.persistence.sqlite_cafe_repository import (
    SqliteCafeRepository,
    decode_price,
)

SCHEMA = (
    "CREATE TABLE cafe (id INTEGER PRIMARY KEY, name VARCHAR (250) NOT NULL UNIQUE, "
    "map_url VARCHAR (500) NOT NULL, img_url VARCHAR (500) NOT NULL, "
    "location VARCHAR (250) NOT NULL, has_sockets BOOLEAN NOT NULL, "
    "has_toilet BOOLEAN NOT NULL, has_wifi BOOLEAN NOT NULL, "
    "can_take_calls BOOLEAN NOT NULL, seats VARCHAR (250), coffee_price VARCHAR (250))"
)
INSERT = "INSERT INTO cafe VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"


@pytest.fixture
def connection() -> Iterator[sqlite3.Connection]:
    """In-memory database with the cafe schema and two rows."""
    conn = sqlite3.connect(":memory:")
    conn.execute(SCHEMA)
    conn.execute(
        INSERT, (1, "Zed", "http://m", "http://i", "Bank", 1, 0, 1, 0, None, None)
    )
    conn.execute(
        INSERT,
        (
            2,
            "Alpha",
            "http://m",
            "http://i",
            "Peckham",
            0,
            1,
            0,
            1,
            "20-30",
            "\ufffd2.40",
        ),
    )
    yield conn
    conn.close()


def test_decode_price_replaces_replacement_character() -> None:
    assert decode_price("\ufffd2.40") == "\u00a32.40"


def test_decode_price_keeps_clean_price() -> None:
    assert decode_price("\u00a32.40") == "\u00a32.40"


def test_decode_price_returns_none_for_none() -> None:
    assert decode_price(None) is None


def test_get_all_cafes_orders_by_name(connection: sqlite3.Connection) -> None:
    names = [c.name for c in SqliteCafeRepository(connection).get_all_cafes()]
    assert names == ["Alpha", "Zed"]


def test_get_all_cafes_maps_booleans(connection: sqlite3.Connection) -> None:
    alpha = SqliteCafeRepository(connection).get_all_cafes()[0]
    assert (
        alpha.has_sockets,
        alpha.has_toilet,
        alpha.has_wifi,
        alpha.can_take_calls,
    ) == (
        False,
        True,
        False,
        True,
    )


def test_get_all_cafes_decodes_price_and_keeps_null(
    connection: sqlite3.Connection,
) -> None:
    alpha, zed = SqliteCafeRepository(connection).get_all_cafes()
    assert alpha.coffee_price == "\u00a32.40"
    assert zed.seats is None
    assert zed.coffee_price is None


def test_get_all_cafes_returns_empty_list_for_empty_table() -> None:
    conn = sqlite3.connect(":memory:")
    conn.execute(SCHEMA)
    assert SqliteCafeRepository(conn).get_all_cafes() == []
    conn.close()
