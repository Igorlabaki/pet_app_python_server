from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface
from src.controllers.person_finder_controller import PersonFinderController

class PersonFinderView(ViewInterface):
    def __init__(self, person_finder_controller: PersonFinderController) -> None:
        self.__person_finder_controller = person_finder_controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["person_id"]
        
        body_response = self.__person_finder_controller.find(person_id)
        
        return HttpResponse(status_code=200, body=body_response)
        
        