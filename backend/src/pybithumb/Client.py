from pybithumb import Bithumb
from pybithumb import WebSocketManager

from PyQt5.QtCore import *

import logging
import unittest
import time

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

class Client(QThread):
    """
    private connect, secret key에 대응하는 info들을 받아오는 class
    """
    recv = pyqtSignal(str)

    def __init__(self, connect_key, secret_key):
        super(Client, self).__init__()
        self._connect_key = connect_key
        self._secrete_key = secret_key

        # connect to private API
        try:
            self._bithumb = Bithumb(connect_key, secret_key)
        except Exception:
            self._bithumb = None
            raise ValueError('Invalid key.\n Check your connect key and secret key')
        logging.info(f"Login private API with {self._connect_key}")

        # 보유중인 ticker check
        self._tickers = []
        self._websocket_managers = None
        self._update_ticker_links()

    def _update_ticker_links(self):
        logging.info("Connecting websockets for possesed coins... ")
        begin_time = time.perf_counter()

        tickers = Bithumb.get_tickers()
        for ticker in tickers:
            balance = self._bithumb.get_balance(ticker)
            # balance[0]: 해당 ticker의 보유 개수
            try:
                self._tickers.append(ticker) if balance[0] > 0.0 else self._tickers.remove(ticker)
            except:
                pass

        if not self._tickers:
            raise RuntimeError('There is no possesed coin Please check your account')

        logging.info(f"Possesed coin: {self._tickers}")

        # connect websockets for each tickers
        # pybithumb의 현재 버전에서는 원화 시장만을 지원한다.
        self._websocket_managers = WebSocketManager("transaction", [ticker + "_KRW" for ticker in self._tickers])
        logging.info(f"Updating websockets are done time: {time.perf_counter() - begin_time:.1f}s")

    def _get_orders(self):
        pass

    @pyqtSlot()
    def run(self):
        while True:
            data = self._websocket_managers.get()
            # msg = f"time            : {data['content']['date']}:{data['content']['time']}\n" +\
            #       f"Symbol          : {data['content']['symbol']}\n" +\
            #       f"Currnet price   : {data['content']['closePrice']}"
            # print()

            # 마지막으로 체결된 해당 ticker의 가격 정보 출력해야해
            # pass

            # print(data)

            # data = self._bithumb.get_order_completed(self._tickers)
            data = self._bithumb.get_transaction_history('ETH_KRW')
            for d in data:
                print(d)
            # print(data)

            self.recv.emit('hello')

if __name__ == '__main__':
    unittest.main()