"""SQLite implementation of the cafe repository.

@file sqlite_cafe_repository.py
@brief Reads and stores cafes with the standard library sqlite3 module.
"""

import sqlite3
from contextlib import closing
from dataclasses import asdict

from cafe_wifi.constants import (
    PRICE_CURRENCY_SIGN,
    PRICE_REPLACEMENT_CHARACTER,
    SQLITE_UNIQUE_ERROR_NAME,
)
from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.domain.entities.new_cafe import NewCafe
from cafe_wifi.domain.errors.duplicate_cafe_error import DuplicateCafeError

_SELECT_ALL_CAFES = (
    "SELECT id, name, map_url, img_url, location, has_sockets, has_toilet, "
    "has_wifi, can_take_calls, seats, coffee_price FROM cafe ORDER BY name"
)
_SELECT_CAFE = (
    "SELECT id, name, map_url, img_url, location, has_sockets, has_toilet, "
    "has_wifi, can_take_calls, seats, coffee_price FROM cafe WHERE id = ?"
)
_DELETE_CAFE = "DELETE FROM cafe WHERE id = ?"
_INSERT_CAFE = (
    "INSERT INTO cafe (name, map_url, img_url, location, has_sockets, has_toilet, "
    "has_wifi, can_take_calls, seats, coffee_price) "
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
)


## @brief Restore the pound sign lost in a stored price.
#  @param price Price as stored, or None.
#  @return The price with U+FFFD replaced by the pound sign, or None.
def decode_price(price: str | None) -> str | None:
    """Replace the replacement character of a stored price with the pound sign."""
    if price is None:
        return None
    return price.replace(PRICE_REPLACEMENT_CHARACTER, PRICE_CURRENCY_SIGN)


## @brief Reads cafes from an open SQLite connection.
class SqliteCafeRepository:
    """Cafe repository backed by a sqlite3 connection owned by the caller."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        """Keep the connection to read from.

        @param connection Open connection to a database with a cafe table.
        """
        self._connection = connection

    def get_all_cafes(self) -> list[Cafe]:
        """Return every cafe ordered by name."""
        with closing(self._connection.execute(_SELECT_ALL_CAFES)) as cursor:
            return [_to_cafe(row) for row in cursor.fetchall()]

    def add_cafe(self, new_cafe: NewCafe) -> Cafe:
        """Insert the cafe with bound parameters and commit.

        @param new_cafe The validated cafe to store.
        @return The stored cafe with its id.
        @throws DuplicateCafeError When the name is already stored.
        """
        values = (
            new_cafe.name,
            new_cafe.map_url,
            new_cafe.img_url,
            new_cafe.location,
            new_cafe.has_sockets,
            new_cafe.has_toilet,
            new_cafe.has_wifi,
            new_cafe.can_take_calls,
            new_cafe.seats,
            new_cafe.coffee_price,
        )
        try:
            with closing(self._connection.execute(_INSERT_CAFE, values)) as cursor:
                cafe_id = cursor.lastrowid
            self._connection.commit()
        except sqlite3.IntegrityError as error:
            self._connection.rollback()
            if error.sqlite_errorname == SQLITE_UNIQUE_ERROR_NAME:
                raise DuplicateCafeError(new_cafe.name) from error
            raise
        return Cafe(id=int(str(cafe_id)), **asdict(new_cafe))

    def get_cafe(self, cafe_id: int) -> Cafe | None:
        """Return the cafe with the id, or None when there is none."""
        with closing(self._connection.execute(_SELECT_CAFE, (cafe_id,))) as cursor:
            row = cursor.fetchone()
        return None if row is None else _to_cafe(row)

    def delete_cafe(self, cafe_id: int) -> bool:
        """Delete the cafe with a bound parameter and commit.

        @param cafe_id Id of the cafe to remove.
        @return True when a row was removed.
        """
        with closing(self._connection.execute(_DELETE_CAFE, (cafe_id,))) as cursor:
            removed = cursor.rowcount > 0
        self._connection.commit()
        return removed


def _to_cafe(row: tuple[object, ...]) -> Cafe:
    """Map one result row to a Cafe."""
    (cafe_id, name, map_url, img_url, location, sockets, toilet, wifi, calls) = row[:9]
    seats, price = row[9], row[10]
    return Cafe(
        id=int(str(cafe_id)),
        name=str(name),
        map_url=str(map_url),
        img_url=str(img_url),
        location=str(location),
        has_sockets=bool(sockets),
        has_toilet=bool(toilet),
        has_wifi=bool(wifi),
        can_take_calls=bool(calls),
        seats=None if seats is None else str(seats),
        coffee_price=decode_price(None if price is None else str(price)),
    )
