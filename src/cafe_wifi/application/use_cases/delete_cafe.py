"""Use case: delete a cafe.

@file delete_cafe.py
@brief Removes a cafe after the visitor confirmed it (US-001.03).
"""

from cafe_wifi.domain.repositories.cafe_repository import CafeRepository


## @brief Deletes a cafe through a repository.
class DeleteCafe:
    """Use case that removes the cafe with a given id."""

    def __init__(self, repository: CafeRepository) -> None:
        """Keep the repository the cafe is removed from.

        @param repository Store of cafes.
        """
        self._repository = repository

    def execute(self, cafe_id: int) -> bool:
        """Delete the cafe.

        @param cafe_id Id of the cafe to remove.
        @return True when the cafe existed and was removed.
        """
        return self._repository.delete_cafe(cafe_id)
