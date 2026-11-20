"""Use case: get one cafe.

@file get_cafe.py
@brief Returns the cafe a confirmation page names (US-001.03).
"""

from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.domain.repositories.cafe_repository import CafeRepository


## @brief Reads one cafe through a repository.
class GetCafe:
    """Use case that returns the cafe with a given id."""

    def __init__(self, repository: CafeRepository) -> None:
        """Keep the repository the cafe is read from.

        @param repository Source of cafes.
        """
        self._repository = repository

    def execute(self, cafe_id: int) -> Cafe | None:
        """Return the cafe, or None when the id is unknown."""
        return self._repository.get_cafe(cafe_id)
