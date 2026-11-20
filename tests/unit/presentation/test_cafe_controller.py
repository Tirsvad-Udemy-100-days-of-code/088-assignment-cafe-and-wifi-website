"""Tests of the cafe controller."""

from cafe_wifi.application.use_cases.list_cafes import ListCafes
from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.presentation.controllers.cafe_controller import CafeController


class FakeCafeRepository:
    """Fake of the cafe repository port."""

    def get_all_cafes(self) -> list[Cafe]:
        return [
            Cafe(
                1, "A", "http://m", "http://i", "L", True, True, True, True, None, None
            )
        ]


def make_controller() -> CafeController:
    return CafeController(ListCafes(FakeCafeRepository()))


def test_handle_returns_list_for_get_home() -> None:
    response = make_controller().handle("GET", "/")
    assert response.status == "200 OK"
    assert "<article" in response.body


def test_handle_accepts_head_home() -> None:
    assert make_controller().handle("HEAD", "/").status == "200 OK"


def test_handle_returns_404_for_unknown_path() -> None:
    assert make_controller().handle("GET", "/nope").status == "404 Not Found"


def test_handle_returns_405_with_allow_header_for_post() -> None:
    response = make_controller().handle("POST", "/")
    assert response.status == "405 Method Not Allowed"
    assert ("Allow", "GET, HEAD") in response.extra_headers
