import pytest


@pytest.mark.skip("No property for name in human.py")
def test_return_name(human):
    pass


def test_return_age(human):
    assert human.age == 44


def test_return_gender(human):
    assert human.gender == "male"


def test_growing(human):
    human.grow()
    assert human._Human__age == 45


def test_max_age_limit(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__age", 110
    )
    human.grow()
    assert human._Human__status == "dead"


def test_return_alive(human):
    human._Human__is_alive()
    assert human._Human__status == "alive"


def test_exception(human, monkeypatch):
    monkeypatch.setattr(
        human, "_Human__age", 110
    )
    human.grow()
    with pytest.raises(Exception):
        human._Human__is_alive()


@pytest.mark.parametrize(
    "gender, expected",
    [("male", "male"),
     ("female", "female")],
    ids=["change_to_male", "change_to_female"]
)
def test_change_gender(human, gender, expected):
    human.change_gender(gender)
    assert human.gender == expected


def test_exception_change_gender(human):
    with pytest.raises(Exception):
        human._Human__change_gender("male")


def test_exception_validate_gender(human):
    with pytest.raises(Exception):
        human._Human__validate_gender("trap")
