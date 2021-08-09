import pybithumb
from collections import defaultdict
from ApiConnect import Connect
from threading import Thread

import logging
import time
import sys
from tqdm import tqdm

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ClientAsset(Thread):
    """
    load the Client Asset information
    """

    def __init__(self, name):
        """
        inquire all tickers and save Client's asset information
        """
        super().__init__()
        self.name = name
        logging.info(f"Name: {self.name}")

        self._client_api = Connect()
        self._ticker_dict = defaultdict(list)

        logging.info("Checking valid tickers (possesed tickers)...")
        self._tickers = ['ETH']

        # for ticker in tqdm(pybithumb.get_tickers()):
        #     balance = self._client_api.get_bitumb().get_balance(ticker)
        #     if balance[0] > 0.0:
        #         self._ticker_dict[ticker].append(balance)
        #         self._tickers.append(ticker)

        # connecting websockets
        self._ws_ticker = None
        self._ws_transaction = None
        self._ws_orderbookdepth = None
        self._connect_websockets()

        # start update data
        self.start()
        # self._ws_thread = Thread(target=self._update_data)
        # self._ws_thread.start()

    def _connect_websockets(self):
        logging.info("Connecting websockets for possesed coins...")

        # pybithumb sopports only KRW market
        ws_tickers = [ticker + '_KRW' for ticker in self._tickers]
        logging.info(f"Subscribe {ws_tickers}")
        self._ws_ticker = pybithumb.WebSocketManager("ticker", ws_tickers)
        self._ws_transaction = pybithumb.WebSocketManager("transaction", ws_tickers)
        self._ws_orderbookdepth = pybithumb.WebSocketManager("orderbookdepth", ws_tickers)

        if self._ws_ticker is None or self._ws_transaction is None or self._ws_orderbookdepth is None:
            logging.error(f"_ws_ticker          connection: {not self._ws_ticker is None}")
            logging.error(f"_ws_transaction     connection: {not self._ws_transaction is None}")
            logging.error(f"_ws_orderboookdepth connection: {not self._ws_orderbookdepth is None}")
            raise ConnectionError("Wecsockets are not connected..")
        else:
            logging.info("Websockets are connected successfully")


    def run(self) -> None:
        while True:
            num = input("enter to get data")

            data_ticker = self._ws_ticker.get()
            data_transaction = self._ws_transaction.get()
            data_orderbookdepth = self._ws_orderbookdepth.get()

            print("=== data ticker ====")
            print(data_ticker); print('\n')

            print("=== data transaction ====")
            print(data_transaction); print('\n')

            print("=== data orderbookdepth ====")
            print(data_orderbookdepth); print('\n')

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
        return self._ticker_dict

if __name__ == "__main__":
    client = ClientAsset("joono")

    num = input("enter number")
    print(num)

    print(client.get_ticker())
    print(client.get_ticker_dict())