from typing import Dict, List

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository_interface import PetsRepositoryInterface
from src.controllers.interfaces.pet_list_controller_interface import PetsListControllerInterface

class PetsListController(PetsListControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def list(self) -> Dict:
        pets = self._get_pets_in_db()
        
        formated_response = self.__formated_respose(pets)
        
        return formated_response
        
    def _get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pets_repository.list_pets()
        return pets
    
    def __formated_respose(self, pets: List[PetsTable]) -> Dict:
        formated_pets = []
        
        for pet in pets:
            formated_pets.append({"name": pet.name, "id": pet.id})
        
        return {
            "data": {
                "type": "Pets",
                "count": len(formated_pets),
                "attributes": formated_pets,
            }
        }