"""Tests of the cafe views."""

from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.presentation.views.cafe_views import (
    render_cafe_card,
    render_cafe_list_page,
    render_page,
    safe_url,
)
from cafe_wifi.presentation.views.error_views import render_error_page


def make_cafe(**changes: object) -> Cafe:
    values: dict[str, object] = {
        "id": 1,
        "name": "Cafe",
        "map_url": "https://m.example/x",
        "img_url": "https://i.example/x.jpg",
        "location": "Bank",
        "has_sockets": True,
        "has_toilet": False,
        "has_wifi": True,
        "can_take_calls": False,
        "seats": "20-30",
        "coffee_price": "\u00a32.40",
    }
    values.update(changes)
    return Cafe(**values)  # type: ignore[arg-type]


def test_safe_url_accepts_https() -> None:
    assert safe_url("https://a.example/x") == "https://a.example/x"


def test_safe_url_rejects_javascript() -> None:
    assert safe_url("javascript:alert(1)") is None


def test_safe_url_rejects_empty() -> None:
    assert safe_url("") is None


def test_render_cafe_card_escapes_name() -> None:
    html = render_cafe_card(make_cafe(name="<script>alert(1)</script>"))
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


def test_render_cafe_card_escapes_quote_in_url() -> None:
    html = render_cafe_card(make_cafe(img_url='https://a.example/"onerror="x'))
    assert '"onerror="' not in html


def test_render_cafe_card_omits_unsafe_urls() -> None:
    html = render_cafe_card(make_cafe(map_url="javascript:alert(1)", img_url="data:x"))
    assert "javascript:" not in html
    assert "<img" not in html
    assert "<a " not in html


def test_render_cafe_card_shows_price_seats_and_badges() -> None:
    html = render_cafe_card(make_cafe())
    assert "\u00a32.40" in html
    assert "20-30" in html
    assert 'badge yes">Wifi' in html
    assert 'badge no">Toilet' in html


def test_render_cafe_card_shows_placeholder_for_missing_values() -> None:
    html = render_cafe_card(make_cafe(seats=None, coffee_price=None))
    assert html.count("n/a") == 2


def test_render_cafe_list_page_has_one_card_per_cafe() -> None:
    html = render_cafe_list_page([make_cafe(), make_cafe(name="Other")])
    assert html.count('<article class="card">') == 2


def test_render_cafe_list_page_handles_no_cafes() -> None:
    assert "No cafes found." in render_cafe_list_page([])


def test_render_page_escapes_title() -> None:
    assert "<b>" not in render_page("<b>", "s", "")


def test_render_error_page_shows_status_and_escapes_message() -> None:
    html = render_error_page("404 Not Found", "<i>x</i>")
    assert "404 Not Found" in html
    assert "<i>" not in html
