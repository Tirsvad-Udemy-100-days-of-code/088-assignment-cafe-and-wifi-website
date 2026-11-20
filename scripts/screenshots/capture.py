"""Takes the screenshots of the website inside a Docker container.

@file capture.py
@brief Starts the site on a temporary copy of the database and saves PNG files.

Run through run.sh or run.ps1, never on the host desktop.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import threading
from pathlib import Path
from wsgiref.simple_server import WSGIServer, make_server

from playwright.sync_api import Page, sync_playwright

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

SMOKE_HTML = (
    "<!doctype html><title>smoke</title>"
    "<h1>Screenshot harness works</h1><p>Headless browser in a container.</p>"
)


def start_site(database: Path) -> tuple[WSGIServer, str]:
    """Start the website on a free port with the given database.

    @param database Path of the SQLite file the site reads and writes.
    @return The running server and its base URL.
    """
    from cafe_wifi.app import create_app  # imported late: not present at baseline

    server = make_server("127.0.0.1", 0, create_app(database))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_port}"


def smoke(page: Page, out: Path) -> None:
    """Save a screenshot of a static page, proving the harness works.

    @param page Browser page to draw in.
    @param out Folder the PNG is written to.
    """
    page.set_content(SMOKE_HTML)
    page.screenshot(path=str(out / "smoke.png"))


def main() -> int:
    """Take the screenshots named on the command line.

    @return Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "docs" / "screenshots")
    parser.add_argument("--smoke", action="store_true", help="static page only")
    parser.add_argument("--steps", nargs="*", default=[], help="step ids, e.g. 1 2 3")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        if args.smoke:
            smoke(page, args.out)
        if args.steps:
            import shots  # step definitions live beside this file

            with tempfile.TemporaryDirectory() as tmp:
                database = Path(tmp) / "cafes.db"
                shutil.copy(ROOT / "data" / "cafes.db", database)
                server, base = start_site(database)
                try:
                    for step in args.steps:
                        shots.take(step, page, base, args.out)
                finally:
                    server.shutdown()
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
