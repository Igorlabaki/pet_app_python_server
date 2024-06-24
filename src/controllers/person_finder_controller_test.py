from typing import Dict
import pytest

from src.controllers.person_finder_controller import PersonFinderController
from src.models.sqlite.entities.people import PeopleTable

class MockPerson():
    def __init__(self,first_name, last_name, pet_name, pet_type) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.pet_name = pet_name
        self.pet_type = pet_type

class MockPeopleRepository(): 
    def get_person(self,person_id: int) -> PeopleTable:
        return MockPerson(
            first_name ="Jhon",
            last_name ="Bolt",
            pet_name ="Joias",
            pet_type ="Dog",
        )
    
def test_find_person():
    person_id = 1

    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(person_id)

    assert response["data"]["count"] == 1
    assert response["data"]["type"] == 'Person' 
    assert response["data"]["attributes"] == {'pet_name': 'Joias', 'pet_type': 'Dog', 'first_name': 'Jhon', 'last_name': 'Bolt'}

