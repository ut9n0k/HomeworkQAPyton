from __future__ import annotations
from typing import List
from xml.etree import ElementTree


class Movie:
    def __init__(self, genre: str, decade: str, movie: str, format: str, year: int, rating: str, description: str):
        self._genre = genre
        self._decade = decade
        self._movie = movie
        self._format = format
        self._year = year
        self._rating = rating
        self._description = description

    @classmethod
    def from_xml(cls, path: str) -> List[Movie]:
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        final = []

        for genre in collection:
            for decade in genre:
                for movie in decade.iter("movie"):
                    movies.append(movie)
                for form in collection:
                    for year in form:
                        for reating in year:
                            for description in reating.iter('description'):
                                for thing in description:
                                    final.append(cls(*thing))
                                    return final


# class Movie:
#     def __init__(
#         self,
#         title: str,
#         format: str,
#         year: int,
#         rating: str,
#         description: str
#     ):
#         self.title = title
#         self.format = format
#         self.year = year
#         self.rating = rating
#         self.description = description
#
#     @classmethod
#     def from_xml(cls, path: str) -> List[Movie]:
#         tree = ElementTree.parse(path)
#         collection = tree.getroot()
#         movies = []
#
#         for movie in collection.iter('movie'):
#             data = {}
#             data["title"] = movie.attrib["title"]
#
#             for child in movie:
#                 data[child.tag] = child.text
#             movies.append(cls(**data))
#         return movies
#
#     def __str__(self):
#         data = ""
#         for key, value in self.__dict__.items():
#             data += f"\t{key}: {value}\n"
#         return f"{{\n{data[:len(data) - 1]}\n}}"
#
#
# if __name__ == '__main__':
#     movies = Movie.from_xml("market.xml")
#     for movie in movies:
#         print(movie)

if __name__ == '__main__':
    movies = Movie.from_xml("market.xml")
