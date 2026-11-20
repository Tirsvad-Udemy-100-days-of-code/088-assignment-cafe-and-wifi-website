"""Tests of the delete cafe use case."""

from cafe_wifi.application.use_cases.delete_cafe import DeleteCafe


class FakeCafeRepository:
    """Fake of the cafe repository port that holds ids."""

    def __init__(self) -> None:
        self.ids = {1, 2}

    def delete_cafe(self, cafe_id: int) -> bool:
        if cafe_id not in self.ids:
            return False
        self.ids.remove(cafe_id)
        return True


def test_execute_returns_true_and_removes_known_id() -> None:
    repository = FakeCafeRepository()
    assert DeleteCafe(repository).execute(1) is True  # type: ignore[arg-type]
    assert repository.ids == {2}


def test_execute_returns_false_for_unknown_id() -> None:
    repository = FakeCafeRepository()
    assert DeleteCafe(repository).execute(9) is False  # type: ignore[arg-type]
    assert repository.ids == {1, 2}
