"""Validation of the add cafe form.

@file new_cafe_validation.py
@brief A pure function that turns submitted fields into a NewCafe or errors.
"""

from collections.abc import Mapping
from string import Template
from urllib.parse import urlsplit

from cafe_wifi.constants import (
    CHECKBOX_ON,
    ERROR_REQUIRED,
    ERROR_TOO_LONG,
    ERROR_URL,
    FIELD_CAN_TAKE_CALLS,
    FIELD_COFFEE_PRICE,
    FIELD_HAS_SOCKETS,
    FIELD_HAS_TOILET,
    FIELD_HAS_WIFI,
    FIELD_IMG_URL,
    FIELD_LOCATION,
    FIELD_MAP_URL,
    FIELD_NAME,
    FIELD_SEATS,
    OPTIONAL_TEXT_FIELDS,
    REQUIRED_TEXT_FIELDS,
    SAFE_URL_SCHEMES,
    URL_FIELDS,
)
from cafe_wifi.domain.entities.new_cafe import NewCafe


def _too_long(limit: int) -> str:
    """Return the error text for a value longer than the limit."""
    return Template(ERROR_TOO_LONG).substitute(limit=limit)


def _is_web_address(value: str) -> bool:
    """Tell whether the value is an http or https address with a host."""
    parts = urlsplit(value)
    return parts.scheme.lower() in SAFE_URL_SCHEMES and bool(parts.netloc)


def _check_required(value: str, limit: int) -> str | None:
    """Return the error of a required text value, or None when it is valid."""
    if not value:
        return ERROR_REQUIRED
    if len(value) > limit:
        return _too_long(limit)
    return None


def _check_url(value: str, limit: int) -> str | None:
    """Return the error of a required web address, or None when it is valid."""
    error = _check_required(value, limit)
    if error is not None:
        return error
    return None if _is_web_address(value) else ERROR_URL


def _check_optional(value: str, limit: int) -> str | None:
    """Return the error of an optional text value, or None when it is valid."""
    return _too_long(limit) if len(value) > limit else None


## @brief Validate the fields of the add cafe form.
#  @param form Submitted fields by name; a missing checkbox is unchecked.
#  @return The cafe and no errors when valid, else None and an error text per
#  field name.
def validate_new_cafe(form: Mapping[str, str]) -> tuple[NewCafe | None, dict[str, str]]:
    """Check every field, strip whitespace and build a NewCafe when all pass."""
    text = {key: value.strip() for key, value in form.items()}
    errors: dict[str, str] = {}
    checks = (
        (REQUIRED_TEXT_FIELDS, _check_required),
        (URL_FIELDS, _check_url),
        (OPTIONAL_TEXT_FIELDS, _check_optional),
    )
    for fields, check in checks:
        for field, limit in fields:
            error = check(text.get(field, ""), limit)
            if error is not None:
                errors[field] = error
    if errors:
        return None, errors
    return (
        NewCafe(
            name=text[FIELD_NAME],
            map_url=text[FIELD_MAP_URL],
            img_url=text[FIELD_IMG_URL],
            location=text[FIELD_LOCATION],
            has_sockets=form.get(FIELD_HAS_SOCKETS) == CHECKBOX_ON,
            has_toilet=form.get(FIELD_HAS_TOILET) == CHECKBOX_ON,
            has_wifi=form.get(FIELD_HAS_WIFI) == CHECKBOX_ON,
            can_take_calls=form.get(FIELD_CAN_TAKE_CALLS) == CHECKBOX_ON,
            seats=text.get(FIELD_SEATS) or None,
            coffee_price=text.get(FIELD_COFFEE_PRICE) or None,
        ),
        errors,
    )
