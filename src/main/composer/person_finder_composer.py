from src.views.person_finder_view import PersonFinderView
from src.models.sqlite.repository.people_repository import PeopleRepository
from src.controllers.person_finder_controller import PersonFinderController

from src.models.sqlite.settings.connection import db_connection_handler

def person_finder_composer():
    model       = PeopleRepository(db_connection_handler)
    controller  = PersonFinderController(model)
    view        = PersonFinderView(controller)
    
    return view
    
    
    
    