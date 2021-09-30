import json
from datetime import time
import time
from flask import Blueprint, url_for, request, jsonify, Response
from werkzeug.utils import redirect
from flask import Blueprint

from ..model.Update import UpdateDB
from ..pybithumb.ApiConnect import Connect
from ..pybithumb.ClientAsset import ClientAsset
from ..pybithumb.RealTimeWebsocketProcess import RealTimeWebsocketProcess
from ..bitcoinAutoTrade import BitcoinAuto
import multiprocessing
from collections import defaultdict

bp = Blueprint('main', __name__, url_prefix='/')
connect = Connect()
c_asset = None
asset_list = None
db = UpdateDB()
websocket_process = None

@bp.route('/')
def index():
    return redirect(url_for('coin.start'))

@bp.route('/login', methods=['GET', 'POST'])
def login():  # get method에 대한 처리
    """
    get publicKey and privateKey from front-end post request
    :return: connecting object
    """
    if request.method == 'POST':
        # postman
        con_key = request.form.get('publicKey')
        sec_key = request.form.get('privateKey')

        # frontend
        '''
        keys = json.loads(request.get_data().decode('utf-8'))
        con_key, sec_key = keys['publicKey'], keys['privateKey']
        '''
        connect.log_in(con_key, sec_key)

        if connect.is_api_key_valid():
            global c_asset, asset_list, websocket_process
            c_asset = ClientAsset(connect)
            asset_list = c_asset.get_ticker()
            websocket_process = RealTimeWebsocketProcess(asset_list)
            return jsonify(status="200", validation=True)
        return jsonify(status="200", validation=False)



@bp.route('/coin')
def coin():
    if request.method == 'GET':
        api_value = connect.get_con_key()

        client_assets = db.getClientAsset(client_api=api_value)
        return jsonify(client_assets)


# @bp.route('coin/start/')
# def start():
#     if request.method == 'GET':
#         client_asset = ClientAsset(connect)
#         # websocket = RealTimeWebsocketProcess(client_asset.get_ticker())

#         coin = BitcoinAuto(connect, client_asset)
#         p1 = multiprocessing.Process(name="Sub", target=multiprocessing_start, args=(coin,))
#         p1.start()

#         return "test"

@bp.route('/coin/test') # 개인이 가지고있는 코인 정보
def coin_test():
    global websocket_process, c_asset, asset_list
    if asset_list != c_asset.get_ticker():
        websocket_process = RealTimeWebsocketProcess(asset_list)

    if request.method == 'GET':
        return jsonify(websocket_process.get_data())

'''
def generate_random_data():
    websocket_process = RealTimeWebsocketProcess(["BTC"])
    while True:
        json_data = json.dumps(c)
        yield f"data:{json_data}"
        print(json_data)
        time.sleep(2)



@bp.route('coin/test/')
def chart_data():
    return Response(generate_random_data(), mimetype="text/event-stream")
'''

def multiprocessing_start(coin):
    coin.auto_start()