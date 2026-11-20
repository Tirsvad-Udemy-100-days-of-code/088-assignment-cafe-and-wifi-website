"""Definitions of the screenshots of each build step.

@file shots.py
@brief One function per step; each milestone adds its own.
"""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Page


def take(step: str, page: Page, base: str, out: Path) -> None:
    """Take the screenshots of one build step.

    @param step Step id, for example "1".
    @param page Browser page to draw in.
    @param base Base URL of the running site.
    @param out Folder the PNG files are written to.
    """
    raise SystemExit(
        f"step {step} has no screenshots defined yet ({base}, {out}, {page})"
    )
