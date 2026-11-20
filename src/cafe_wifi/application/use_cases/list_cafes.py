"""Use case: list all cafes.

@file list_cafes.py
@brief Returns every cafe for the home page (US-001.01).
"""

from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.domain.repositories.cafe_repository import CafeRepository


## @brief Lists all cafes through a repository.
class ListCafes:
    """Use case that returns all cafes ordered by name."""

    def __init__(self, repository: CafeRepository) -> None:
        """Keep the repository the cafes are read from.

        @param repository Source of cafes.
        """
        self._repository = repository

    def execute(self) -> list[Cafe]:
        """Return every cafe."""
        return self._repository.get_all_cafes()
