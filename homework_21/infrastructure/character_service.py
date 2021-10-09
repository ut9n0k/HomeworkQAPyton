from requests import Response, get
from homework_21.app import config


class CharacterService:
    def __init__(self):
        self.__character_url = f"{config['host']}/character"

    def get_character(self, id: int) -> Response:
        return get(f"{self.__character_url}/{id}")
