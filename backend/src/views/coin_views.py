from flask import Blueprint

import multiprocessing

from ..bitcoinAutoTrade import BitcoinAuto
import multiprocessing
from ..pybithumb.ClientAsset import ClientAsset
from ..pybithumb.ApiConnect import Connect
from ..pybithumb.RealTimeWebsocketProcess import RealTimeWebsocketProcess



bp = Blueprint('coin', __name__, url_prefix='/coin')

""" 
This is Test Page
"""

@bp.route('/start/')
def start():
    from ..bitcoinAutoTrade import BitcoinAuto # 함수 안에 임포트
    coin = BitcoinAuto()
    p = multiprocessing.Process(name="Sub", target=multiprocessing_start, args=(coin,))
    p.start()
    return "test"


    from pybithumb import Bithumb
    connect = Connect()
    client_asset = ClientAsset(connect)

    websocket = RealTimeWebsocketProcess(client_asset.get_ticker())

    coin = BitcoinAuto(connect, client_asset)
    p1 = multiprocessing.Process(name="Sub", target=multiprocessing_start, args=(coin,))
    p1.start()

    return "test"


def multiprocessing_start(coin):
    coin.auto_start()
