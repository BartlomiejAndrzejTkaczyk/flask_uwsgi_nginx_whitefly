from flask import Blueprint, request, jsonify
from user_async.services import create_user

router = Blueprint('user_async', __name__, url_prefix='/user_async')


@router.route('/usertest', methods=['POST'])
def hello_world():
    return jsonify({'hello_world': 200})


@router.route('/add', methods=['POST'])
def add_user():
    nickname = request.json.get('nickname', 'nickname')
    password = request.json.get('password', 'password')
    info = request.json.get('info', 'info')
    task = create_user.apply_async((nickname, password, info))
    return jsonify({'New user': task.id})
