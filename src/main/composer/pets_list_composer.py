from src.models.sqlite.settings.connection import db_connection_handler

from src.views.pet_list_view import PetListView
from src.controllers.pet_list_controller import PetsListController
from src.models.sqlite.repository.pets_repository import PetsRepository

def pet_list_composer():
    model       = PetsRepository(db_connection_handler)
    controller  = PetsListController(model)
    view        = PetListView(controller)
    
    return view