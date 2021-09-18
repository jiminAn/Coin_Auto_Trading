import json
from flask import Blueprint, url_for, request, jsonify
from werkzeug.utils import redirect
from flask import Blueprint
from ..bitcoinAutoTrade import BitcoinAuto
from collections import defaultdict
import multiprocessing

from ..model.Update import UpdateDB
from ..pybithumb.ApiConnect import Connect
from ..pybithumb.ClientAsset import ClientAsset


from ..pybithumb.RealTimeWebsocketProcess import RealTimeWebsocketProcess


bp = Blueprint('main', __name__, url_prefix='/')
connect = Connect()
db = UpdateDB()

@bp.route('/')
def index():
    return redirect(url_for('coin.start'))


# @bp.route('/', methods=['GET', 'POST'])
# def index():
#     return redirect(url_for('.login')) # get




@bp.route('/login', methods=['GET', 'POST'])
def login():  # get method에 대한 처리
    """
    get publicKey and privateKey from front-end post request
    :return: connecting object
    """
    if request.method == 'POST':
        # get_data() : 프론트에서 보낸 데이터를 byte type으로 받음. json.load() : byte -> json (dictionary)
        # 포스트맨 전용
        con_key = request.form.get('publicKey')
        sec_key = request.form.get('privateKey')

        # keys = json.loads(request.get_data().decode('utf-8'))
        #
        # con_key = keys['publicKey']
        # sec_key = keys['privateKey']
        connect.log_in(con_key, sec_key)
        if connect.is_api_key_valid():
            return jsonify(status="200", validation=True)
        return jsonify(status="200", validation=False)



@bp.route('/coin')
def coin():
    if request.method == 'GET': # back -> front
        api_value = connect.get_con_key()

        client_assets = db.getClientAsset(client_api=api_value)
        return jsonify(client_assets)


        #api_type = request.args.keys() # get User's publicKey(ConnectKey

        #ret = defaultdict(str)
        #for arg in args:
        #    ret[arg] = "aa"

        #return jsonify(ret)



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
