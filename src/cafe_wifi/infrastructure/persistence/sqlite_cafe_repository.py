"""SQLite implementation of the cafe repository.

@file sqlite_cafe_repository.py
@brief Reads cafes with the standard library sqlite3 module.
"""

import sqlite3
from contextlib import closing

from cafe_wifi.constants import PRICE_CURRENCY_SIGN, PRICE_REPLACEMENT_CHARACTER
from cafe_wifi.domain.entities.cafe import Cafe

_SELECT_ALL_CAFES = (
    "SELECT id, name, map_url, img_url, location, has_sockets, has_toilet, "
    "has_wifi, can_take_calls, seats, coffee_price FROM cafe ORDER BY name"
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
