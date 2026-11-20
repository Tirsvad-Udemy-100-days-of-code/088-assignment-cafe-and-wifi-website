"""Tests of the cafe entity."""

import dataclasses

import pytest

from cafe_wifi.domain.entities.cafe import Cafe


def test_cafe_is_immutable() -> None:
    cafe = Cafe(1, "A", "http://m", "http://i", "L", True, True, True, True, None, None)
    with pytest.raises(dataclasses.FrozenInstanceError):
        cafe.name = "B"  # type: ignore[misc]
