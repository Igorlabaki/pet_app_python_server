from flask import Blueprint, jsonify, request

# Interfaces
from src.errors.error_handle import handle_errors
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

# Composer
from src.main.composer.person_finder_composer import person_finder_composer 
from src.main.composer.person_creator_composer import person_creator_composer 

person_route_bp = Blueprint("person_routes",__name__)

@person_route_bp.route("/people", methods=["POST"])
def create_person():
    try:
        view : ViewInterface = person_creator_composer()
        http_request : HttpRequest = HttpRequest(body=request.json)
        
        http_response : HttpResponse = view.handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        
        return jsonify(http_response.body), http_response.status_code

@person_route_bp.route("/people/<person_id>", methods=["GET"])
def finder_person(person_id):
    try:
        view : ViewInterface = person_finder_composer()
        http_request : HttpRequest = HttpRequest(param={"person_id": person_id})
        
        http_response : HttpResponse = view.handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        
        return jsonify(http_response.body), http_response.status_code
