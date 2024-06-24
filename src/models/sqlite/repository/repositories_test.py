import pytest

from .pets_repository import PetsRepository
from src.models.sqlite.repository.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import db_connection_handler

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interacao com o banco")
def test_list_pets():
    repo = PetsRepository(db_connection=db_connection_handler)
    repo.list_pets()

@pytest.mark.skip(reason="Interacao com o banco")
def test_delete_pets():
    name = "belinha"
    repo = PetsRepository(db_connection=db_connection_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason="Interacao com o banco")
def test_insert_person():
    age= 33
    pet_id= 1
    lastname="Goncalo"
    first_name = "Igor"
    
    repo = PeopleRepository(db_connection=db_connection_handler)
    repo.insert_person(last_name=lastname, age=age,first_name=first_name, pet_id=pet_id)

@pytest.mark.skip(reason="Interacao com o banco")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connection=db_connection_handler)
    repo.get_person(person_id=person_id)





    

    