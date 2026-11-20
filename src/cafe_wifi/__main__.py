"""Entry point: python -m cafe_wifi.

@file __main__.py
@brief Serves the site with wsgiref on the configured host and port.
"""

import logging
import os
from pathlib import Path
from wsgiref.simple_server import make_server

from cafe_wifi.constants import (
    CAFE_WIFI_DB_ENV,
    DEFAULT_DB_RELATIVE_PATH,
    DEFAULT_HOST,
    DEFAULT_PORT,
)
from cafe_wifi.presentation.app import create_app

_REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
_LOGGER = logging.getLogger(__name__)


## @brief Find the database file.
#  @return The path in the environment variable, else the default file.
def resolve_database_path() -> Path:
    """Return the database path from the environment or the default."""
    override = os.environ.get(CAFE_WIFI_DB_ENV)
    if override:
        return Path(override)
    return _REPOSITORY_ROOT / DEFAULT_DB_RELATIVE_PATH


## @brief Serve the site until interrupted.
def main() -> None:
    """Start the development server."""
    logging.basicConfig(level=logging.INFO)
    app = create_app(resolve_database_path())
    with make_server(DEFAULT_HOST, DEFAULT_PORT, app) as server:
        _LOGGER.info("Serving on http://%s:%s", DEFAULT_HOST, DEFAULT_PORT)
        server.serve_forever()


if __name__ == "__main__":
    main()
