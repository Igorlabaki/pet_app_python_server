from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface
from src.controllers.person_creator_controller import PersonCreatorController
from src.errors.validators.person_creator_validator import person_creator_validator

class PersonCreatorView(ViewInterface):
    def __init__(self, person_creator_controller: PersonCreatorController) -> None:
        self.__person_creator_controller = person_creator_controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_creator_validator(http_request)
        
        person_info = http_request.body
        
        body_response = self.__person_creator_controller.create(person_info)
        
        return HttpResponse(status_code=201, body=body_response)
        
        