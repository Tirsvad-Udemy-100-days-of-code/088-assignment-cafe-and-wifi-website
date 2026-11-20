"""Tests of the get cafe use case."""

from cafe_wifi.application.use_cases.get_cafe import GetCafe
from cafe_wifi.domain.entities.cafe import Cafe

CAFE = Cafe(7, "A", "http://m", "http://i", "L", True, True, True, True, None, None)


class FakeCafeRepository:
    """Fake of the cafe repository port."""

    def get_cafe(self, cafe_id: int) -> Cafe | None:
        return CAFE if cafe_id == CAFE.id else None


def test_execute_returns_cafe_of_known_id() -> None:
    assert GetCafe(FakeCafeRepository()).execute(7) == CAFE  # type: ignore[arg-type]


def test_execute_returns_none_for_unknown_id() -> None:
    assert GetCafe(FakeCafeRepository()).execute(8) is None  # type: ignore[arg-type]
