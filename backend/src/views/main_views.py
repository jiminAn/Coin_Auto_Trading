from flask import Blueprint, url_for, request
from werkzeug.utils import redirect
import pybithumb

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('.login')) # get


@bp.route('/login', methods=['GET', 'POST']) # 여기서 빗썸 객체를 front에게 보내게하면 어떨까?
def login(): # get method에 대한 처리
    """
    get publicKey and privateKey from front-end post request
    :return: connecting object
    """
    if request.method == 'POST':
        # b'{"publicKey":"admin","privateKey":"admin"}' bytes 타입으로 프론트엔드에서 백엔드로 요청 전송
        # 이 구문을 수정해서 백엔드 전체에서 사용해야 합니다.(key가 필요한 모든 부분에 대해서)
        # 이 구문에 대해서 API key 유효성 검사를 한 후 유효할 경우와 그렇지 않은 경우에 대해서 프론트엔드에 객체를 return해주면 될 것 같습니다.
        print(request.get_data()) # b'{"publicKey":"admin","privateKey":"admin"}'
        return "This is Post" # 프론트 엔드로 이 정보가 전송됩니다.
    return "test"
