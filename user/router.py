from flask import Blueprint, request, jsonify, render_template
from user.services import create_user

router = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')


@router.route('/usertest', methods=['POST'])
def hello_world():
    return jsonify({'hello_world': 200})


@router.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        nickname = request.form.get('nickname', 'nickname')
        password = request.form.get('password', 'password')
        info = request.form.get('info', 'info')
        task = create_user(nickname, password, info)
        return render_template('success.html', task_id=task.id)
    else:
        return render_template('add_user.html')
