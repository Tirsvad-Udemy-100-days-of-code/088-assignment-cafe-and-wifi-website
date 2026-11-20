"""The response a controller returns.

@file response.py
@brief Plain data the WSGI adapter turns into a real response.
"""

from dataclasses import dataclass, field


## @brief Status, headers and body of one HTTP response.
@dataclass(frozen=True, slots=True)
class Response:
    """Framework-free HTTP response."""

    status: str
    body: str
    extra_headers: tuple[tuple[str, str], ...] = field(default=())
