from flask import Blueprint
from flask import request, Response
from json import loads
from http import HTTPStatus
from flask import jsonify
from src.security.security import login_required


from src.services.telephones_service import TelephonesService
from src.utils.validator import validator
from .validators import create_and_update_telephone_validator

service = TelephonesService()

app = Blueprint('telephones', __name__)

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('', methods=['POST'])
@login_required
def create_telephone():
    data = loads(request.data)
    validator(create_and_update_telephone_validator, data)
    return jsonify(service.create(data)), HTTPStatus.CREATED


@app.route('', methods=['GET'])
@login_required
def list_telephones():
    return jsonify(service.list_by_user_id())


@app.route('/<telephone_id>', methods=['GET'])
@login_required
def read_telephone(telephone_id):
    return jsonify(service.read_by_id(telephone_id))


@app.route('/<telephone_id>', methods=['PUT'])
@login_required
def update_telephone(telephone_id):
    data = loads(request.data)
    validator(create_and_update_telephone_validator, data)
    service.update(telephone_id, data)
    return Response(status=HTTPStatus.NO_CONTENT)


@app.route('/<telephone_id>', methods=['DELETE'])
@login_required
def delete_telephone(telephone_id):
    service.delete(telephone_id)
    return Response(status=HTTPStatus.NO_CONTENT)

