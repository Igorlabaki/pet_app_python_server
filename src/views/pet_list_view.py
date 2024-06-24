from src.controllers.pet_list_controller import  PetsListController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PetListView(ViewInterface):
    def __init__(self, pets_list_controller: PetsListController) -> None:
        self.__pets_list_controller = pets_list_controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse: 
        body_response = self.__pets_list_controller.list() 
        
        return HttpResponse(status_code=200, body=body_response)