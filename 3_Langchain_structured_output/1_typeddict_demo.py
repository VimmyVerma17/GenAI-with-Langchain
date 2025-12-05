from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': "Sahil", 'age': 5}

print(new_person)