from flask import Blueprint, jsonify

router = Blueprint('loader_io', __name__, url_prefix='')


@router.route('/loaderio-4f2d0dc9a3c15e9dbb0a87e4de154b4a/', methods=['GET'])
def loader_io():
    return 'loaderio-4f2d0dc9a3c15e9dbb0a87e4de154b4a'
