from typing import Dict
from abc import ABC, abstractmethod

from src.models.sqlite.entities.people import PersonWithoutId

class PersonCreatorControllerInterface(ABC):
    
    @abstractmethod
    def create(self, person_info: PersonWithoutId) -> Dict:
        pass