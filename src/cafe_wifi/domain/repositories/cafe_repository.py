"""The cafe repository port.

@file cafe_repository.py
@brief The interface the application layer needs to read and add cafes.
"""

from typing import Protocol

from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.domain.entities.new_cafe import NewCafe


## @brief Read and write access to the stored cafes.
class CafeRepository(Protocol):
    """Source of cafes, implemented by an adapter."""

    def get_all_cafes(self) -> list[Cafe]:
        """Return every cafe ordered by name."""
        ...

    def add_cafe(self, new_cafe: NewCafe) -> Cafe:
        """Store a cafe and return it with its new id.

        @param new_cafe The validated cafe to store.
        @return The stored cafe.
        @throws DuplicateCafeError When a cafe with the same name exists.
        """
        ...
