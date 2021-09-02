import pytest
from homework_16.human import Human


@pytest.fixture
def human() -> Human:
    yield Human("Harry", 44, "male")
