
from collections import defaultdict
from ApiConnect import Connect
from multiprocessing import Process
from tqdm import tqdm

import multiprocessing as mp

import pybithumb
import logging
import time
import sys
import websockets
import asyncio
import json


logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ClientAsset(Process):
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
        for ticker in tqdm(pybithumb.get_tickers()):
            balance = self._client_api.get_bitumb().get_balance(ticker)
            if balance[0] > 0.0:
                self._ticker_dict[ticker].append(balance)
                self._tickers.append(ticker)

        # connecting websockets
        self._types = ["ticker", "transaction", "orderbookdepth"]
        self._alive = {"ticker": False, "transaction": False, "orderbookdepth": False}
        self._q = {"ticker": mp.Queue(1000), "transaction": mp.Queue(1000), "orderbookdepth": mp.Queue(1000)}
        self._connect_websockets()

        # start process
        self.start()

    def run(self) -> None:
        while True:
            if self._q["ticker"] and self._q["transaction"] and self._q["orderbookdepth"]:
                for type in self._types:
                    print(type, '\n', self._q[type].get())

            time.sleep(0.1)

    def _connect_websockets(self):
        logging.info("Connecting websockets for possesed coins...")

        # pybithumb supports only KRW market
        ws_tickers = [ticker + '_KRW' for ticker in self._tickers]
        logging.info(f"Subscribe {ws_tickers}")

        for type in self._types:
            self._ws_ticker_process = Process(name="ticker", target=self.__start_websocket, args=(type, ws_tickers,))
            self._ws_ticker_process.start()
            logging.info(f'start websocket {type} process')

        logging.info("Websockets are connected successfully")

    async def __connect_websocket(self, type, symbols):
        uri = "wss://pubwss.bithumb.com/pub/ws"

        async with websockets.connect(uri, ping_interval=None) as websocket:
            connection_msg = await websocket.recv()
            # {"status":"0000","resmsg":"Connected Successfully"}
            if "Connected Successfully" not in connection_msg :
                print("connection error")

            data = {
                "type"     : type,
                'symbols'  : symbols,
                'tickTypes': ["1H"]
            }
            await websocket.send(json.dumps(data))

            registration_msg = await websocket.recv()
            # {"status":"0000","resmsg":"Filter Registered Successfully"}
            if "Filter Registered Successfully" not in registration_msg:
                print("Registration error")

            while self._alive[type]:
                recv_data = await websocket.recv()
                self._q[type].put(json.loads(recv_data))

    def __start_websocket(self, type, symbols):
        self._alive[type] = True
        self.__aloop = asyncio.get_event_loop()
        self.__aloop.run_until_complete(self.__connect_websocket(type, symbols))

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

    def get_orderbookdepth_data(self):
        """
        {
	    "type" : "orderbookdepth",
		"content" : {
		"list" : [
			{
				"symbol" : "BTC_KRW",
				"orderType" : "ask",		// 주문타입 – bid / ask
				"price" : "10593000",		// 호가
				"quantity" : "1.11223318",	// 잔량
				"total" : "3"				// 건수
			},
		],
		"datetime":1580268255864325		// 일시
	        }
        }
        """
        pass

    def get_transaction_data(self):
        """
        "type" : "transaction",
	    "content" : {
		    "list" : [
                {
                    "symbol" : "BTC_KRW",					// 통화코드
                    "buySellGb" : "1",							// 체결종류(1:매도체결, 2:매수체결)
                    "contPrice" : "10579000",					// 체결가격
                    "contQty" : "0.01",							// 체결수량
                    "contAmt" : "105790.00",					// 체결금액
                    "contDtm" : "2020-01-29 12:24:18.830039",	// 체결시각
                    "updn" : "dn"								// 직전 시세와 비교 : up-상승, dn-하락
                }
            ]
	    }
        """
        pass



if __name__ == "__main__":
    client = ClientAsset('joono')

    # check multi processing
    for i in range(1000):
        print(i, sep=" ")
        time.sleep(0.5)
