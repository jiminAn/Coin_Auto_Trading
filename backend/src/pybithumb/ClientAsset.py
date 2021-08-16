
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

    information of each type's contennt visit here
    https://apidocs.bithumb.com/docs/websocket_public
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
            balance = self._client_api.get_balance(ticker)
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
        """
        0.1초 간격으로 queue에 각 websockets으로 부터 받아온 data가 있으면 이를 가져옵니다.
        websocket의 type의 종류에는 "ticker(현재가)", "transaction(체결)", "orderbookdepth(변경호가)"
        의 data를 받아옵니다.

        필요하신 종류의 type이 있다면 self._q[type].get() 과 같이 data를 받아올 수 있습니다.
        Usage:
            if self._q["ticker"] and self._q["transaction"] and self._q["orderbookdepth"]:
                for type in self._types:
                    print(type, '\n', self._q[type].get())
        """

        while True:
            if self._q["ticker"]:
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
        """
        original code:
            https://github.com/sharebook-kr/pybithumb/blob/master/pybithumb/websocket.py
        """

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

    def terminate(self):
        for type in self._types:
            self._alive[type] = False
        super().terminate()



if __name__ == "__main__":
    client = ClientAsset('joono')
    print(client)

    # check multi processing
    for i in range(1000):
        print(i, sep=" ")
        time.sleep(0.5)
