from flask import Blueprint, request, render_template
from user_async.services import create_user

router = Blueprint('user_async', __name__, url_prefix='/user_async', template_folder='templates')


@router.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        nickname = request.form.get('nickname', 'nickname')
        password = request.form.get('password', 'password')
        info = request.form.get('info', 'info')
        task = create_user.apply_async((nickname, password, info))
        return render_template('success.html', task_id=task.id)
    else:
        return render_template('add_user.html')
