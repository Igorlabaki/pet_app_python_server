from src.controllers.pet_delete_controller import PetDeleteController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PetDeleteView(ViewInterface):
    def __init__(self, pet_delete_controller: PetDeleteController) -> None:
        self.__pet_delete_controller = pet_delete_controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self.__pet_delete_controller.delete(name)
        
        return HttpResponse(status_code=204)
        
        