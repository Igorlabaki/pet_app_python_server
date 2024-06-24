from flask import Blueprint, jsonify, request

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

from src.errors.error_handle import handle_errors
from src.main.composer.pets_list_composer import pet_list_composer
from src.main.composer.pet_delete_composer import pet_delete_composer

pet_route_bp = Blueprint("pets_routes",__name__)

@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
    try:
        view : ViewInterface = pet_list_composer()
        http_request : HttpRequest = HttpRequest()
        
        http_response : HttpResponse = view.handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        
        return jsonify(http_response.body), http_response.status_code


@pet_route_bp.route("/pets/<name>", methods=["DELETE"])
def delete_pet(name):
    try:
        view : ViewInterface = pet_delete_composer()
        http_request : HttpRequest = HttpRequest(param={"name": name})
        
        http_response : HttpResponse = view.handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        
        return jsonify(http_response.body), http_response.status_code
