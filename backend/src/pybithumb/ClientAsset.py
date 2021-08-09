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
        self._tickers = []
        for ticker in tqdm(pybithumb.get_tickers()):
            balance = self._client_api.get_bitumb().get_balance(ticker)
            if balance[0] > 0.0:
                self._ticker_dict[ticker].append(balance)
                self._tickers.append(ticker)

        # connecting websockets
        self._ws_ticker = None
        self._ws_transaction = None
        self._ws_orderbookdepth = None
        self._connect_websockets()

    def _connect_websockets(self):
        logging.info("Connecting websockets for possesed coins...")

        # pybithumb supports only KRW market
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

    def get_ticker_data(self, ):
        """
        현재가(ticker)

        "type" : "ticker",
	    "content" : {
		"symbol" : "BTC_KRW",			    // 통화코드
		"tickType" : "24H",					// 변동 기준시간- 30M, 1H, 12H, 24H, MID
		"date" : "20200129",				// 일자
		"time" : "121844",					// 시간
		"openPrice" : "2302",				// 시가
		"closePrice" : "2317",				// 종가
		"lowPrice" : "2272",				// 저가
		"highPrice" : "2344",				// 고가
		"value" : "2831915078.07065789",	// 누적거래금액
		"volume" : "1222314.51355788",	    // 누적거래량
		"sellVolume" : "760129.34079004",	// 매도누적거래량
		"buyVolume" : "462185.17276784",	// 매수누적거래량
		"prevClosePrice" : "2326",			// 전일종가
		"chgRate" : "0.65",					// 변동률
		"chgAmt" : "15",					// 변동금액
		"volumePower" : "60.80"			    // 체결강도
	    }
        """
        data = self._ws_ticker.get()
        return data

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

    while True:
        print(client.get_ticker_data())