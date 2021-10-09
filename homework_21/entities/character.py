from __future__ import annotations


class Character:
    def __init__(self, id, name, status, species, type, gender):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender

    def __eq__(self, other: Character):
        return self.__dict__ == other.__dict__
