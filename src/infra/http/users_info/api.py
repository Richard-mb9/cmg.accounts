from flask import Blueprint
from flask import request, Response
from json import loads
from http import HTTPStatus
from flask import jsonify
from src.security.security import login_required

from src.services.users_info_service import UsersInfoService
from src.utils.validator import validator
from .validators import create_and_update_users_info


service = UsersInfoService()

app = Blueprint('users_info', __name__)

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('', methods=['POST'])
@login_required
def create_and_update_users_info():
    data = loads(request.data)
    validator(create_and_update_users_info, data)
    return Response(service.create_and_update(data), status=HTTPStatus.CREATED)


@app.route('', methods=['GET'])
def read_users_info_by_user_id():
    user_info = service.get_user_info_logged()
    return jsonify(user_info)