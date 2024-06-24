from typing import Dict

from src.models.sqlite.entities.people import PeopleTable
from src.errors.errors_types.http_not_found import HttpNotFoundError
from src.models.sqlite.interfaces.people_repository_interface import PeopleRepositoryInterface
from src.controllers.interfaces.person_finder_controller_interface import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id) -> Dict:
        person = self.__find_person_in_db(person_id)
        formated_response = self.__formated_respose(person)

        return formated_response

    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Pessoa nao encontrada")
        return person

    def __formated_respose(self, person: PeopleTable) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "last_name": person.last_name,
                    "first_name": person.first_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type,
                }
            }
        }