"""Error raised when a cafe name is already stored.

@file duplicate_cafe_error.py
@brief The failure a repository reports for a second cafe with the same name.
"""


## @brief A cafe with the same name already exists.
class DuplicateCafeError(Exception):
    """Raised by a repository when a new cafe repeats a stored name."""
