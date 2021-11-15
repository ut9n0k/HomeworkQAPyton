import pytest
from homework_21.infrastructure.character_service import CharacterService
from homework_21.entities.character import Character


@pytest.fixture(scope="session")
def character_service() -> CharacterService:
    yield CharacterService()


@pytest.fixture
def first_character():
    yield Character(
        id=1,
        name="Rick Sanchez",
        status="Alive",
        species="Human",
        type="",
        gender="Male"
    )
