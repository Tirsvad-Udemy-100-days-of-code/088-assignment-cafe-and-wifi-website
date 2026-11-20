"""The cafe entity.

@file cafe.py
@brief Plain data for one row of the cafe table.
"""

from dataclasses import dataclass


## @brief A cafe where one can work remotely.
@dataclass(frozen=True, slots=True)
class Cafe:
    """A cafe with its facilities; seats and price may be unknown."""

    id: int
    name: str
    map_url: str
    img_url: str
    location: str
    has_sockets: bool
    has_toilet: bool
    has_wifi: bool
    can_take_calls: bool
    seats: str | None
    coffee_price: str | None
