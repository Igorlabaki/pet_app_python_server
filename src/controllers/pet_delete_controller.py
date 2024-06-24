
from typing import Dict, List

from src.controllers.interfaces.pet_delete_controller_interface import PetDeleteControllerInterface
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository_interface import PetsRepositoryInterface


class PetDeleteController(PetDeleteControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def delete(self, name: str) -> None:
       self.__pets_repository.delete_pets(name)