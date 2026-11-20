"""Tests of the add cafe use case."""

from cafe_wifi.application.use_cases.add_cafe import AddCafe
from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.domain.entities.new_cafe import NewCafe
from cafe_wifi.domain.errors.duplicate_cafe_error import DuplicateCafeError

FORM = {
    "name": "Cafe",
    "location": "Bank",
    "map_url": "https://m.example/x",
    "img_url": "https://i.example/x.jpg",
}


class FakeCafeRepository:
    """Fake of the cafe repository port that keeps new cafes in a list."""

    def __init__(self) -> None:
        self.added: list[NewCafe] = []

    def get_all_cafes(self) -> list[Cafe]:
        return []

    def add_cafe(self, new_cafe: NewCafe) -> Cafe:
        if any(added.name == new_cafe.name for added in self.added):
            raise DuplicateCafeError(new_cafe.name)
        self.added.append(new_cafe)
        return Cafe(len(self.added), **vars_of(new_cafe))


def vars_of(new_cafe: NewCafe) -> dict[str, object]:
    return {name: getattr(new_cafe, name) for name in NewCafe.__slots__}


def test_execute_stores_valid_cafe_and_returns_no_errors() -> None:
    repository = FakeCafeRepository()
    assert AddCafe(repository).execute(FORM) == {}
    assert [c.name for c in repository.added] == ["Cafe"]


def test_execute_returns_field_errors_and_stores_nothing_when_invalid() -> None:
    repository = FakeCafeRepository()
    errors = AddCafe(repository).execute({**FORM, "name": ""})
    assert set(errors) == {"name"}
    assert repository.added == []


def test_execute_turns_duplicate_into_name_error() -> None:
    repository = FakeCafeRepository()
    use_case = AddCafe(repository)
    use_case.execute(FORM)
    assert use_case.execute(FORM) == {"name": "A cafe with this name already exists"}
    assert len(repository.added) == 1
