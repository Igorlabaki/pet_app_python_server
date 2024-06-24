from abc import ABC, abstractmethod
from typing import Dict
from src.models.sqlite.entities.people import PeopleTable, PersonWithoutId

class PeopleRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_person(self, person: PersonWithoutId) -> None:
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> PeopleTable:
        pass