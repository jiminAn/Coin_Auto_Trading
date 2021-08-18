from flask import Blueprint
from ..bitcoinAutoTrade import BitcoinAuto
import multiprocessing

bp = Blueprint('coin', __name__, url_prefix='/coin')

""" 
This is Test Page
"""

@bp.route('/start/')
def start():
    coin = BitcoinAuto()
    p = multiprocessing.Process(name="Sub", target=multiprocessing_start, args=(coin,))
    p.start()
    return "test"


def multiprocessing_start(coin):
    coin.auto_start()
