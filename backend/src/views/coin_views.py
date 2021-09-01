from flask import Blueprint
import multiprocessing

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


def multiprocessing_start(coin):
    coin.auto_start()