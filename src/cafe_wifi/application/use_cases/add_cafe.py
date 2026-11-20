"""Use case: add a cafe.

@file add_cafe.py
@brief Validates a submitted form and stores the cafe (US-001.02).
"""

from collections.abc import Mapping

from cafe_wifi.constants import ERROR_DUPLICATE_NAME, FIELD_NAME
from cafe_wifi.domain.errors.duplicate_cafe_error import DuplicateCafeError
from cafe_wifi.domain.repositories.cafe_repository import CafeRepository
from cafe_wifi.domain.validation.new_cafe_validation import validate_new_cafe


## @brief Adds a cafe through a repository.
class AddCafe:
    """Use case that validates the submitted fields and stores a new cafe."""

    def __init__(self, repository: CafeRepository) -> None:
        """Keep the repository the cafe is stored in.

        @param repository Store of cafes.
        """
        self._repository = repository

    def execute(self, form: Mapping[str, str]) -> dict[str, str]:
        """Store the cafe when the fields are valid.

        @param form Submitted fields by name.
        @return An error text per field name; empty when the cafe was stored.
        """
        new_cafe, errors = validate_new_cafe(form)
        if new_cafe is None:
            return errors
        try:
            self._repository.add_cafe(new_cafe)
        except DuplicateCafeError:
            return {FIELD_NAME: ERROR_DUPLICATE_NAME}
        return {}
