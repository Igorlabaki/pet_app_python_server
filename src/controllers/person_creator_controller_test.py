import pytest

from src.models.sqlite.entities.people import PeopleTable, PersonWithoutId
from src.controllers.person_creator_controller import PersonCreatorController

class MockPeopleRepository():
    def insert_person(self,person: PersonWithoutId):
           return person
    
def test_create():
    person_info : PersonWithoutId = {
        "age" : 3,
        "pet_id" : 1,
        "first_name": "Jorge",
        "last_name" : "Goncalo"
    }

    controller = PersonCreatorController(MockPeopleRepository())

    response = controller.create(person_info)
  
    assert response["data"]["count"] == 1
    assert response["data"]["type"] == 'Person' 
    assert response["data"]["attributes"] == {'age': 33, 'pet_id': 111, 'first_name': 'Jorge', 'last_name': 'Goncalo'}

def test_create_age_error():
    person_info : PersonWithoutId = {
        "age" : 333,
        "pet_id" : 111,
        "first_name": "Jorge123",
        "last_name" : "Goncalo"
    }

    controller = PersonCreatorController(MockPeopleRepository())

    with pytest.raises(Exception, match="Idade da pessoa invalida"):
        controller.create(person_info)

def test_create_pet_id_error():
    person_info : PersonWithoutId = {
        "age" : 33,
        "pet_id" : "testError",
        "first_name": "Jorge123",
        "last_name" : "Goncalo"
    }

    controller = PersonCreatorController(MockPeopleRepository())

    with pytest.raises(Exception, match="Pet_id deve ser um numero"):
        controller.create(person_info)

def test_create_name_error():
    person_info : PersonWithoutId = {
        "age" : 33,
        "pet_id" : 23,
        "first_name": "Jorge123",
        "last_name" : "Goncalo"
    }

    controller = PersonCreatorController(MockPeopleRepository())

    with pytest.raises(Exception, match="Nome da pessoa invalido"):
        controller.create(person_info)


