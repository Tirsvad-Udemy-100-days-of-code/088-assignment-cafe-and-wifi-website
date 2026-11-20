"""The cafe repository port.

@file cafe_repository.py
@brief The interface the application layer needs to read cafes.
"""

from typing import Protocol

from cafe_wifi.domain.entities.cafe import Cafe


## @brief Read access to the stored cafes.
class CafeRepository(Protocol):
    """Source of cafes, implemented by an adapter."""

    def get_all_cafes(self) -> list[Cafe]:
        """Return every cafe ordered by name."""
        ...
