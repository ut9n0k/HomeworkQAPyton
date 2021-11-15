from homework_21.entities.character import Character


def test_check_character_01(character_service):
    response = character_service.get_character(1)
    print(response)


def test_check_character_2(character_service):
    response = character_service.get_character(1)
    keys = ["name", "species"]
    assert all(key in response.json() for key in keys)


def test_check_character_3(character_service, first_character):
    response = character_service.get_character(1)
    actual_character = Character(
        response.json()["id"],
        response.json()["name"],
        response.json()["status"],
        response.json()["species"],
        response.json()["type"],
        response.json()["gender"]
    )
    assert actual_character == first_character
