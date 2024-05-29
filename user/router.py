from flask import Blueprint, request, jsonify
from user.services import create_user

router = Blueprint('user', __name__, url_prefix='/user')


@router.route('/usertest', methods=['POST'])
def hello_world():
    return jsonify({'hello_world': 200})


@router.route('/add', methods=['POST'])
def add_user():
    nickname = request.json.get('nickname', 'nickname')
    password = request.json.get('password', 'password')
    info = request.json.get('info', 'info')
    user_json = create_user(nickname, password, info)
    return jsonify({'New user': user_json})
