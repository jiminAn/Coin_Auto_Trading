from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/') # app.route가 아닌 블루프린트 클래스 객체 bg.route로 표시한다.

def hello_pybo():
    return 'Hello, Pybo!'