"""Definitions of the screenshots of each build step.

@file shots.py
@brief One function per step; each milestone adds its own.
"""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Page


def take_list(page: Page, base: str, out: Path) -> None:
    """Take the full-page screenshot of the cafe list.

    @param page Browser page to draw in.
    @param base Base URL of the running site.
    @param out Folder the PNG file is written to.
    """
    page.goto(base)
    page.screenshot(path=str(out / "step-1-list.png"), full_page=True)


def take_add_form(page: Page, base: str, out: Path) -> None:
    """Take the screenshots of the empty add form and of its error state.

    @param page Browser page to draw in.
    @param base Base URL of the running site.
    @param out Folder the PNG files are written to.
    """
    page.goto(f"{base}/add")
    page.screenshot(path=str(out / "step-2-add-form.png"), full_page=True)
    page.click("button[type=submit]")
    page.wait_for_selector(".error")
    page.screenshot(path=str(out / "step-2-add-errors.png"), full_page=True)


def take_delete_confirm(page: Page, base: str, out: Path) -> None:
    """Take the screenshot of the delete confirmation of the first cafe.

    @param page Browser page to draw in.
    @param base Base URL of the running site.
    @param out Folder the PNG file is written to.
    """
    page.goto(base)
    page.click("text=Delete >> nth=0")
    page.wait_for_selector("form.confirm")
    page.screenshot(path=str(out / "step-3-delete-confirm.png"), full_page=True)


def take(step: str, page: Page, base: str, out: Path) -> None:
    """Take the screenshots of one build step.

    @param step Step id, for example "1".
    @param page Browser page to draw in.
    @param base Base URL of the running site.
    @param out Folder the PNG files are written to.
    """
    if step == "1":
        take_list(page, base, out)
        return
    if step == "2":
        take_add_form(page, base, out)
        return
    if step == "3":
        take_delete_confirm(page, base, out)
        return
    raise SystemExit(f"step {step} has no screenshots defined yet")
