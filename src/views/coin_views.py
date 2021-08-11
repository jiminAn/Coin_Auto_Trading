import datetime
from flask import Blueprint
import pybithumb
from ..bitcoinAutoTrade import BitcoinAuto
from ..pybithumb.ApiConnect import Connect
from ..pybithumb.ClientAsset import ClientAsset
import multiprocessing
from ..bestk import findk

bp = Blueprint('coin', __name__, url_prefix='/coin')

@bp.route('/start/')
def start():
    coin = BitcoinAuto()
    p = multiprocessing.Process(name="Sub", target=multiprocessing_start, args=(coin,))
    p.start()
    return "test"


def multiprocessing_start(coin):
    coin.auto_start()
