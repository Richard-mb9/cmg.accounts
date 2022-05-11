from flask import Blueprint
from flask import request, Response
from json import loads
from http import HTTPStatus
from flask import jsonify
from src.security.security import login_required

from src.services.stores_service import StoresService
from src.utils.validator import validator
from .validators import create_and_update_store


service = StoresService()

app = Blueprint('stores', __name__)

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('', methods=['POST'])
@login_required
def create_and_update_store():
    data = loads(request.data)
    validator(create_and_update_store, data)
    return Response(service.create_and_update(data), status=HTTPStatus.CREATED)


@app.route('', methods=['GET'])
def read_store_by_user_id():
    store = service.get_store_logged()
    return jsonify(store)