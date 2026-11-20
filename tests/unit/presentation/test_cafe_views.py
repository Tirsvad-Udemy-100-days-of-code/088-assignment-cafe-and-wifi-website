"""Tests of the cafe views."""

from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.presentation.views.add_cafe_views import render_add_form
from cafe_wifi.presentation.views.cafe_views import (
    render_cafe_card,
    render_cafe_list_page,
    render_page,
    safe_url,
)
from cafe_wifi.presentation.views.delete_cafe_views import render_delete_confirmation
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
    assert ">Map</a>" not in html


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


def test_render_add_form_is_empty_without_values() -> None:
    html = render_add_form({}, {})
    assert 'method="post" action="/add"' in html
    assert 'class="error"' not in html
    assert "checked" not in html


def test_render_add_form_escapes_entered_values() -> None:
    html = render_add_form({"name": '"><script>alert(1)</script>'}, {})
    assert "<script>" not in html
    assert "&quot;&gt;&lt;script&gt;" in html


def test_render_add_form_escapes_errors() -> None:
    html = render_add_form({}, {"name": "<b>bad</b>"})
    assert "<b>" not in html
    assert "&lt;b&gt;bad" in html


def test_render_add_form_shows_error_beside_its_field() -> None:
    html = render_add_form({}, {"map_url": "Nope"})
    assert 'class="field invalid"' in html
    assert 'id="error-map_url">Nope' in html


def test_render_add_form_keeps_checked_boxes() -> None:
    html = render_add_form({"has_wifi": "on"}, {})
    assert html.count(" checked>") == 1


def test_render_cafe_list_page_links_to_add_form() -> None:
    assert '<a href="/add">Add a cafe</a>' in render_cafe_list_page([])


def test_render_cafe_card_links_to_delete_page() -> None:
    assert '<a href="/delete/5">Delete</a>' in render_cafe_card(make_cafe(id=5))


def test_render_delete_confirmation_names_cafe_and_posts_to_delete_path() -> None:
    html = render_delete_confirmation(make_cafe(id=5, name="Blue"))
    assert "<strong>Blue</strong>" in html
    assert 'method="post" action="/delete/5"' in html
    assert ">Delete</button>" in html
    assert '<a href="/">Cancel</a>' in html


def test_render_delete_confirmation_escapes_script_name() -> None:
    html = render_delete_confirmation(make_cafe(name="<script>alert(1)</script>"))
    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
