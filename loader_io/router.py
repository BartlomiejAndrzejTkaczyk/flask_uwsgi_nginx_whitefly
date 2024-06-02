from flask import Blueprint

router = Blueprint('loader_io', __name__, url_prefix='')


@router.route('/loaderio-97fb4e92f5a1df31d401de96e96f3d97/', methods=['GET'])
def loader_io():
    return 'loaderio-97fb4e92f5a1df31d401de96e96f3d97'
