import pybithumb
import time
import logging

from collections import defaultdict
<<<<<<< HEAD
from ApiConnect import Connect
from RealTimeWebsocketProcess import RealTimeWebsocketProcess
=======
from .ApiConnect import Connect
from .RealTimeWebsocketProcess import RealTimeWebsocketProcess
>>>>>>> test-websocket
from tqdm import tqdm

class ClientAsset:
    """
    load the Client Asset information
    """
    _ticker_dict = defaultdict(list)
    _client_api = None

    def __init__(self, connect: Connect):
        """
        inquire all tickers and save Client's asset information
        """

        # connect to public, private API
<<<<<<< HEAD
        self._client_api = Connect()
=======
        self._client_api = connect
>>>>>>> test-websocket
        self._ticker_dict = defaultdict(list)

        logging.info("Checking valid tickers (possesed tickers)...")
        tickers = pybithumb.get_tickers()
        for ticker in tqdm(tickers):
<<<<<<< HEAD
            balance = self._client_api.get_bitumb().get_balance(ticker)
            if balance[0] > 0.0:
                self._ticker_dict[ticker].append(balance)

        self.websocket_process = RealTimeWebsocketProcess(self.get_ticker())
=======
            balance = self._client_api.get_bithumb().get_balance(ticker)
            if balance[0] > 0.0:
                self._ticker_dict[ticker].append(balance)

        # self._websocket_process = RealTimeWebsocketProcess(self.get_ticker())
>>>>>>> test-websocket

    def get_ticker(self):
        """
        get the ticker list of client asset
        :return: tickers(List)
        """
        return [ticker for ticker in self._ticker_dict.keys()]

    def get_ticker_dict(self):
        """
        get client asset information
        :return: ticker information(Dict); {ticker : [client asset information]}
        """
<<<<<<< HEAD
        return self._ticker_dict

if __name__ == "__main__":
    client = ClientAsset()

    # check multi processing
    for i in range(1000):
        print("")
        time.sleep(0.5)
=======
        return self._ticker_dict
>>>>>>> test-websocket
