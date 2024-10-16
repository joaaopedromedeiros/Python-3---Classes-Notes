
# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
# from print import pprint

from typing import TypedDict
# Tipagem (Auxilia dms)


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''


Movie: Filme = json.loads(string_json) # formato json para python --> vira dict, tudo passa a ter formato python

# print(filme, width=40)
# print(filme['title']) # usando métodos de dict pois virou dict o json
# print(filme['characters'][0])
# print(filme['year'] + 10)

json_string = json.dumps(filme, ensure_ascii=False, indent=2)

print(json_string)