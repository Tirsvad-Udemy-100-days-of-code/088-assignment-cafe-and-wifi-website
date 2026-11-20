"""Tests of the cafe controller."""

from urllib.parse import urlencode

from cafe_wifi.application.use_cases.add_cafe import AddCafe
from cafe_wifi.application.use_cases.list_cafes import ListCafes
from cafe_wifi.constants import MAX_BODY_BYTES
from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.domain.entities.new_cafe import NewCafe
from cafe_wifi.domain.errors.duplicate_cafe_error import DuplicateCafeError
from cafe_wifi.presentation.controllers.cafe_controller import CafeController
from cafe_wifi.presentation.controllers.response import Response

FORM = {
    "name": "New",
    "location": "Bank",
    "map_url": "https://m.example/x",
    "img_url": "https://i.example/x.jpg",
}


class FakeCafeRepository:
    """Fake of the cafe repository port."""

    def __init__(self) -> None:
        self.added: list[NewCafe] = []

    def add_cafe(self, new_cafe: NewCafe) -> Cafe:
        if new_cafe.name == "A":
            raise DuplicateCafeError(new_cafe.name)
        self.added.append(new_cafe)
        return Cafe(2, **{n: getattr(new_cafe, n) for n in NewCafe.__slots__})

    def get_all_cafes(self) -> list[Cafe]:
        return [
            Cafe(
                1, "A", "http://m", "http://i", "L", True, True, True, True, None, None
            )
        ]


def make_controller(repository: FakeCafeRepository | None = None) -> CafeController:
    repository = repository or FakeCafeRepository()
    return CafeController(ListCafes(repository), AddCafe(repository))


def post(
    controller: CafeController, form: dict[str, str], path: str = "/add"
) -> "Response":
    return controller.handle("POST", path, urlencode(form).encode())


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


def test_handle_returns_empty_form_for_get_add() -> None:
    response = make_controller().handle("GET", "/add")
    assert response.status == "200 OK"
    assert "<form" in response.body


def test_handle_returns_405_with_post_in_allow_header_for_put_add() -> None:
    response = make_controller().handle("PUT", "/add")
    assert response.status == "405 Method Not Allowed"
    assert ("Allow", "GET, HEAD, POST") in response.extra_headers


def test_handle_redirects_to_home_after_valid_post() -> None:
    repository = FakeCafeRepository()
    response = post(make_controller(repository), FORM)
    assert response.status == "303 See Other"
    assert ("Location", "/") in response.extra_headers
    assert [c.name for c in repository.added] == ["New"]


def test_handle_returns_422_with_errors_and_values_for_invalid_post() -> None:
    repository = FakeCafeRepository()
    response = post(make_controller(repository), {**FORM, "name": "", "seats": "7"})
    assert response.status == "422 Unprocessable Content"
    assert "This field is required." in response.body
    assert 'value="7"' in response.body
    assert repository.added == []


def test_handle_returns_422_for_duplicate_name() -> None:
    response = post(make_controller(), {**FORM, "name": "A"})
    assert response.status == "422 Unprocessable Content"
    assert "already exists" in response.body


def test_handle_reads_checkbox_from_body() -> None:
    repository = FakeCafeRepository()
    post(make_controller(repository), {**FORM, "has_wifi": "on"})
    assert repository.added[0].has_wifi is True


def test_handle_returns_413_for_oversized_body() -> None:
    body = b"a" * (MAX_BODY_BYTES + 1)
    assert make_controller().handle("POST", "/add", body).status.startswith("413")


def test_handle_returns_400_for_too_many_fields() -> None:
    body = "&".join(f"f{i}=1" for i in range(100)).encode()
    assert make_controller().handle("POST", "/add", body).status.startswith("400")


def test_handle_returns_405_for_post_home() -> None:
    assert make_controller().handle("POST", "/").status == "405 Method Not Allowed"
