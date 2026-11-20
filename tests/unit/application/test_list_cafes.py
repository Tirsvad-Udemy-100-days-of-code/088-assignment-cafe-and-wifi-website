"""Tests of the list cafes use case."""

from cafe_wifi.application.use_cases.list_cafes import ListCafes
from cafe_wifi.domain.entities.cafe import Cafe

CAFE = Cafe(1, "A", "http://m", "http://i", "L", True, True, True, True, None, None)


class FakeCafeRepository:
    """Fake of the cafe repository port."""

    def get_all_cafes(self) -> list[Cafe]:
        return [CAFE]


def test_execute_returns_cafes_of_repository() -> None:
    assert ListCafes(FakeCafeRepository()).execute() == [CAFE]
