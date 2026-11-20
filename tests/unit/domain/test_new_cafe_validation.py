"""Tests of the add cafe form validation."""

from cafe_wifi.constants import (
    ERROR_REQUIRED,
    ERROR_URL,
    MAX_TEXT_LENGTH,
    MAX_URL_LENGTH,
)
from cafe_wifi.domain.validation.new_cafe_validation import validate_new_cafe

VALID = {
    "name": "Cafe",
    "location": "Bank",
    "map_url": "https://m.example/x",
    "img_url": "http://i.example/x.jpg",
}


def form(**changes: str) -> dict[str, str]:
    values = dict(VALID)
    values.update(changes)
    return values


def test_valid_minimal_form_builds_cafe_with_defaults() -> None:
    cafe, errors = validate_new_cafe(VALID)
    assert errors == {}
    assert cafe is not None
    assert (cafe.name, cafe.location) == ("Cafe", "Bank")
    assert not any(
        (cafe.has_sockets, cafe.has_toilet, cafe.has_wifi, cafe.can_take_calls)
    )
    assert cafe.seats is None
    assert cafe.coffee_price is None


def test_checked_boxes_are_true_and_absent_boxes_false() -> None:
    cafe, _ = validate_new_cafe(form(has_wifi="on", can_take_calls="on"))
    assert cafe is not None
    assert (cafe.has_wifi, cafe.can_take_calls) == (True, True)
    assert (cafe.has_sockets, cafe.has_toilet) == (False, False)


def test_whitespace_is_stripped() -> None:
    cafe, _ = validate_new_cafe(form(name="  Cafe  ", seats=" 10-20 "))
    assert cafe is not None
    assert (cafe.name, cafe.seats) == ("Cafe", "10-20")


def test_blank_optional_fields_become_none() -> None:
    cafe, _ = validate_new_cafe(form(seats="   ", coffee_price=""))
    assert cafe is not None
    assert cafe.seats is None
    assert cafe.coffee_price is None


def test_price_is_kept_as_typed() -> None:
    cafe, _ = validate_new_cafe(form(coffee_price="£2.50"))
    assert cafe is not None
    assert cafe.coffee_price == "£2.50"


def test_empty_name_is_an_error() -> None:
    cafe, errors = validate_new_cafe(form(name="  "))
    assert cafe is None
    assert errors == {"name": ERROR_REQUIRED}


def test_missing_location_is_an_error() -> None:
    values = form()
    del values["location"]
    assert validate_new_cafe(values)[1] == {"location": ERROR_REQUIRED}


def test_name_at_limit_is_valid_and_above_limit_is_not() -> None:
    assert validate_new_cafe(form(name="a" * MAX_TEXT_LENGTH))[1] == {}
    errors = validate_new_cafe(form(name="a" * (MAX_TEXT_LENGTH + 1)))[1]
    assert "250" in errors["name"]


def test_location_above_limit_is_an_error() -> None:
    errors = validate_new_cafe(form(location="a" * (MAX_TEXT_LENGTH + 1)))[1]
    assert set(errors) == {"location"}


def test_empty_map_url_is_required() -> None:
    assert validate_new_cafe(form(map_url=""))[1] == {"map_url": ERROR_REQUIRED}


def test_url_without_http_scheme_is_an_error() -> None:
    errors = validate_new_cafe(form(img_url="ftp://x.example/a.jpg"))[1]
    assert errors == {"img_url": ERROR_URL}


def test_javascript_url_is_an_error() -> None:
    assert validate_new_cafe(form(map_url="javascript:alert(1)"))[1] == {
        "map_url": ERROR_URL
    }


def test_url_without_host_is_an_error() -> None:
    assert validate_new_cafe(form(map_url="http://"))[1] == {"map_url": ERROR_URL}


def test_url_length_boundary() -> None:
    prefix = "https://x.example/"
    ok = prefix + "a" * (MAX_URL_LENGTH - len(prefix))
    assert validate_new_cafe(form(map_url=ok))[1] == {}
    errors = validate_new_cafe(form(map_url=ok + "a"))[1]
    assert set(errors) == {"map_url"}
    assert "500" in errors["map_url"]


def test_optional_fields_above_limit_are_errors() -> None:
    long = "a" * (MAX_TEXT_LENGTH + 1)
    errors = validate_new_cafe(form(seats=long, coffee_price=long))[1]
    assert set(errors) == {"seats", "coffee_price"}


def test_all_errors_are_reported_together() -> None:
    cafe, errors = validate_new_cafe({})
    assert cafe is None
    assert set(errors) == {"name", "location", "map_url", "img_url"}
