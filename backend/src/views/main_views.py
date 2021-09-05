from flask import Blueprint, url_for, request, jsonify
from werkzeug.utils import redirect
from flask import Blueprint
from ..bitcoinAutoTrade import BitcoinAuto
import multiprocessing
from ..pybithumb.ClientAsset import ClientAsset
from ..pybithumb.ApiConnect import Connect
from ..pybithumb.RealTimeWebsocketProcess import RealTimeWebsocketProcess


bp = Blueprint('main', __name__, url_prefix='/')
connect = Connect()

@bp.route('/')
def index():
    return redirect(url_for('coin.start'))


# @bp.route('/', methods=['GET', 'POST'])
# def index():
#     return redirect(url_for('.login')) # get


@bp.route('/login', methods=['GET', 'POST'])
def login(): # get method에 대한 처리
    """
    get publicKey and privateKey from front-end post request
    :return: connecting object
    """
    if request.method == 'POST':
        con_key = request.form.get('publicKey')
        sec_key = request.form.get('privateKey')

        connect.log_in(con_key, sec_key)
        if connect.is_api_key_valid():
            return jsonify(status="200", validation=True)
        return jsonify(status="200", validation=False)

@bp.route('/coin')
def coin():
    pass


# @bp.route('coin/start/')
# def start():
#     connect = Connect()
#     client_asset = ClientAsset(connect)
#     websocket = RealTimeWebsocketProcess(client_asset.get_ticker())
#
#     coin = BitcoinAuto(connect, client_asset)
#     p1 = multiprocessing.Process(name="Sub", target=multiprocessing_start, args=(coin,))
#     p1.start()
#
#     return "test"

def multiprocessing_start(coin):
    coin.auto_start()
