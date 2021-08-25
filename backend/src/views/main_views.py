from flask import Blueprint, url_for, request
from werkzeug.utils import redirect
import pybithumb

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('.login')) # get


@bp.route('/login', methods=['GET', 'POST']) # 여기서 빗썸 객체를 front에게 보내게하면 어떨까?
def login(): # get method에 대한 처리
    if request.method == 'POST':
        print(request.form["publicKey"], request.form["privateKey"])
        return "This is Post"
    return "test"
