"""The new cafe value object.

@file new_cafe.py
@brief The data of a cafe that has not been stored yet.
"""

from dataclasses import dataclass


## @brief A cafe before it has an id.
@dataclass(frozen=True, slots=True)
class NewCafe:
    """The validated fields of a cafe to add; seats and price may be unknown."""

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
