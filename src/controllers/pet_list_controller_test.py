from typing import Dict
import pytest

from src.controllers.person_finder_controller import PersonFinderController
from src.controllers.pet_list_controller import PetsListController
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable

class MockPetsRepository():
   def list_pets(self):
       return [
           PetsTable(name="Flufy",type="cat", id=4),
           PetsTable(name="buddy",type="dog", id=45),
           PetsTable(name="jorge",type="turtle", id=9)
       ]

def test_list_pets():
    
    controller = PetsListController(MockPetsRepository())
    response = controller.list()

    assert response["data"]["count"] == 3
    assert response["data"]["type"] == 'Pets' 
    
    expected_response = {
        "data": {
            "type": "Pets",
            "count": 3,
            "attributes": [
                {"name": "Flufy", "id": 4},
                {"name": "buddy", "id": 45},
                {"name": "jorge", "id": 9},
            ],
        }
    }
    
    assert response == expected_response
