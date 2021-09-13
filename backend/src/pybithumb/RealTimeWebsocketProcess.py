from collections import defaultdict

# from src.ApiConnect import Connect
from multiprocessing import Process
from tqdm import tqdm  # for progress bar
import multiprocessing as mp
# import pybithumb
import logging
import time
import sys
import websockets
import asyncio
import json

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class RealTimeWebsocketProcess():
    """
    connecting real time websocket processed
    If you want to know information of each type's content please visit below website
    https://apidocs.bithumb.com/docs/websocket_public
    """

    def __init__(self, tickers: list):
        """
        ticker: tickers the client possessed
        example: websocket_process = RealtimeWebsocketProcess(["BTC", "ETH"])
        """

        # tickers possessed by client
        self._tickers = tickers  # for RUN CHECKING

        # connecting websockets
        self._types = ["ticker", "transaction", "orderbookdepth"]
        self._alive = {"ticker": False, "transaction": False, "orderbookdepth": False}
        self._q = {"ticker": mp.Queue(1000), "transaction": mp.Queue(1000), "orderbookdepth": mp.Queue(1000)}
        self.request_types_info()
        self.get_tikcer_info()

    def run(self) -> None:
        """
        0.1초 간격으로 queue에 각 websockets으로 부터 받아온 data가 있으면 이를 가져옵니다.
        websocket의 type의 종류에는 "ticker(현재가)", "transaction(체결)", "orderbookdepth(변경호가)"
        의 data를 받아옵니다.
        필요하신 종류의 type이 있다면 self._q[type].get() 과 같이 data를 받아올 수 있습니다.
        Usage:
            if self._q["ticker"] and self._q["transaction"] and self._q["orderbookdepth"]:
                for type in self.__types:
                    print(type, '\n', self._q[type].get())
        """
        ws_tickers = [ticker + '_KRW' for ticker in self._tickers]
        print(ws_tickers)
        while True:
            if self._q["ticker"]:
                data = self._q['ticker'].get()
                # for tickers in client.tickers:

                if data['content']['symbol'] in ws_tickers:
                    print(data)

            time.sleep(0.1)

    def request_types_info(self):
        logging.info("Connecting websockets for possesed coins...")

        # pybithumb supports only KRW market
        ws_tickers = [ticker + '_KRW' for ticker in self._tickers]
        logging.info(f"Subscribe {ws_tickers}")

        for type in self._types:
            self._ws_ticker_process = Process(name=type, target=self.get_type_info, args=(type, ws_tickers,))
            self._ws_ticker_process.start()
            logging.info(f'start websocket {type} process')

        logging.info("Websockets are connected successfully")

    async def connect_websocket(self, type, symbols):
        """
        original code:
            https://github.com/sharebook-kr/pybithumb/blob/master/pybithumb/websocket.py
        """

        uri = "wss://pubwss.bithumb.com/pub/ws"

        async with websockets.connect(uri, ping_interval=None) as websocket:
            connection_msg = await websocket.recv()
            # {"status":"0000","resmsg":"Connected Successfully"}
            if "Connected Successfully" not in connection_msg:
                print("connection error")

            data = {
                "type": type,
                'symbols': symbols,
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

    def start_websocket(self, type, symbols):
        self._alive[type] = True
        self._aloop = asyncio.get_event_loop()
        self._aloop.run_until_complete(self.connect_websocket(type, symbols))

    # MultiProcessing 실행 함수
    def get_type_info(self, type, ws_tickers):
        self.start_websocket(type, ws_tickers)

    def get_tikcer_info(self):
        self._ws_ticker_process = Process(name="ticker", target=self.run)
        self._ws_ticker_process.start()

    def terminate(self):
        for type in self._types:
            self._alive[type] = False