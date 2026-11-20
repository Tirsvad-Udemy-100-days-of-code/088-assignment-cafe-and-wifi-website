"""HTML views of the cafe pages.

@file cafe_views.py
@brief Pure functions that turn cafes into escaped HTML.
"""

from html import escape
from string import Template
from urllib.parse import urlsplit

from cafe_wifi.constants import (
    APP_NAME,
    BADGES,
    HOME_SUBTITLE,
    LABEL_MAP,
    LABEL_PRICE,
    LABEL_SEATS,
    PAGE_CSS,
    PAGE_TEMPLATE,
    SAFE_URL_SCHEMES,
    TEXT_NO_CAFES,
    TEXT_UNKNOWN,
)
from cafe_wifi.domain.entities.cafe import Cafe


## @brief Keep a URL only when it is a plain http or https address.
#  @param url Address taken from the database.
#  @return The URL, or None when the scheme is not allowed.
def safe_url(url: str) -> str | None:
    """Return the URL when its scheme is http or https, else None."""
    parts = urlsplit(url.strip())
    if parts.scheme.lower() in SAFE_URL_SCHEMES and parts.netloc:
        return url.strip()
    return None


## @brief Wrap content in the page layout.
#  @param title Page title and heading.
#  @param subtitle Line under the heading.
#  @param content HTML of the page body, already escaped.
#  @return The complete HTML document.
def render_page(title: str, subtitle: str, content: str) -> str:
    """Return a full HTML page; title and subtitle are escaped here."""
    return Template(PAGE_TEMPLATE).substitute(
        title=escape(title),
        subtitle=escape(subtitle),
        css=PAGE_CSS,
        content=content,
    )


def _render_badge(label: str, is_on: bool) -> str:
    """Return one yes/no badge."""
    state = "yes" if is_on else "no"
    return f'<li class="badge {state}">{escape(label)}</li>'


def _render_fact(label: str, value: str | None) -> str:
    """Return one labelled line, with a placeholder for a missing value."""
    text = TEXT_UNKNOWN if value is None or not value.strip() else value
    return f'<p class="facts"><strong>{escape(label)}:</strong> {escape(text)}</p>'


## @brief Render one cafe as a card.
#  @param cafe The cafe to show.
#  @return HTML of the card, every value escaped.
def render_cafe_card(cafe: Cafe) -> str:
    """Return the HTML card of one cafe."""
    image_url = safe_url(cafe.img_url)
    map_url = safe_url(cafe.map_url)
    image = (
        f'<img src="{escape(image_url)}" alt="{escape(cafe.name)}" loading="lazy">'
        if image_url
        else ""
    )
    map_link = (
        f'<p class="facts"><a href="{escape(map_url)}" rel="noopener noreferrer">'
        f"{escape(LABEL_MAP)}</a></p>"
        if map_url
        else ""
    )
    badges = "".join(
        _render_badge(label, bool(getattr(cafe, attribute)))
        for label, attribute in BADGES
    )
    return (
        '<article class="card">'
        f"{image}"
        '<div class="body">'
        f"<h2>{escape(cafe.name)}</h2>"
        f'<p class="location">{escape(cafe.location)}</p>'
        f'<ul class="badges">{badges}</ul>'
        f"{_render_fact(LABEL_SEATS, cafe.seats)}"
        f"{_render_fact(LABEL_PRICE, cafe.coffee_price)}"
        f"{map_link}"
        "</div></article>"
    )


## @brief Render the home page.
#  @param cafes Cafes to list, in display order.
#  @return The complete HTML document.
def render_cafe_list_page(cafes: list[Cafe]) -> str:
    """Return the home page with one card per cafe."""
    if cafes:
        cards = "\n".join(render_cafe_card(cafe) for cafe in cafes)
        content = f'<section class="grid">\n{cards}\n</section>'
    else:
        content = f"<p>{escape(TEXT_NO_CAFES)}</p>"
    return render_page(APP_NAME, HOME_SUBTITLE, content)
