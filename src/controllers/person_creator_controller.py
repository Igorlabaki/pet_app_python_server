import re
from typing import Dict

from src.models.sqlite.entities.people import PersonWithoutId
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.models.sqlite.interfaces.people_repository_interface import PeopleRepositoryInterface
from src.controllers.interfaces.person_creator_controller_interface import PersonCreatorControllerInterface


class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: PersonWithoutId) -> Dict:
        age = person_info["age"]
        pet_id = person_info["pet_id"]
        last_name = person_info["last_name"]
        first_name = person_info["first_name"]

        self.__validate_age(age)
        self.__validate_pet_Id(pet_id)
        self.__validate_first_and_last_name(first_name,last_name)

        input_data : PersonWithoutId = {
            "age" : age,
            "pet_id" : pet_id,
            "first_name": first_name,
            "last_name" : last_name
        }

        self.__insert_person(input_data)
        
        formated_response = self.__formated_respose(input_data) 

        return formated_response

    
    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # expressao regular para caracteres que nao sao letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
            raise HttpUnprocessableEntityError("Nome da pessoa invalido")
        
    def __validate_age(self, age: int) -> None:
        formated_age = str(age)
        # expressao regular para idade
        non_valid_caracteres = re.compile(r'^(?:1[0-4]?\d|150|[1-9]?\d)$')

        if not non_valid_caracteres.search(formated_age):
            raise HttpUnprocessableEntityError("Idade da pessoa invalida")
        
    def __validate_pet_Id(self, pet_id: int) -> None:
        formated_age = str(pet_id)
    
        non_valid_caracteres = re.compile(r'^\d+$')

        if not non_valid_caracteres.search(formated_age):
            raise HttpUnprocessableEntityError("Pet_id deve ser um numero")
    
    def __insert_person(self, person: PersonWithoutId):
        return self.__people_repository.insert_person(person)

    def __formated_respose(self, new_person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": new_person_info
            }
        }