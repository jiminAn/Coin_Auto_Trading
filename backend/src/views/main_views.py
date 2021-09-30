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
from ..crawling.CrawledInfo import *
from ..bitcoinAutoTrade import BitcoinAuto
import multiprocessing
from collections import defaultdict

bp = Blueprint('main', __name__, url_prefix='/')
connect = Connect()
c_asset = None
asset_list = None
db = UpdateDB()
websocket_client_process = None
tickers_info = create_ticker_name_dict()
websocket_process = RealTimeWebsocketProcess([ticker for ticker in tickers_info.keys()])

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
            global c_asset, asset_list, websocket_client_process
            c_asset = ClientAsset(connect)
            asset_list = c_asset.get_ticker()
            websocket_client_process = RealTimeWebsocketProcess(asset_list)
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

@bp.route('/coin/clientassets') # 개인이 가지고있는 코인 정보달 전달
def coin_clientassets():
    global websocket_client_process, c_asset, asset_list
    if asset_list != c_asset.get_ticker():
        websocket_client_process = RealTimeWebsocketProcess(asset_list)

    if request.method == 'GET':
        return jsonify(websocket_client_process.get_data())


@bp.route('/coin/tickers_20') # 상위 20개 코인 정보 전달
def coin_tickers():
    global websocket_process
    if websocket_process == None:
        websocket_process = RealTimeWebsocketProcess([ticker for ticker in tickers_info.keys()])

    if request.method == 'GET':
        return jsonify(websocket_client_process.get_data())


def multiprocessing_start(coin):
    coin.auto_start()
