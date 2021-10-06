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
import datetime
import json
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
coin_info = defaultdict(dict)
asset_info = defaultdict(dict)



class RealTimeWebsocketProcess():
    """
    connecting real time websocket processed
    If you want to know information of each type's content, please visit the below website
    https://apidocs.bithumb.com/docs/websocket_public
    """

    def __init__(self, tickers: list):
        '''
        set the client's assets and connecting websocket
        :param tickers: tickers the client possessed
        example: websocket_process = RealTimeWebsocketProcess(["BTC", "ETH"])
        '''

        # tickers possessed by client
        self._tickers = tickers

        # connecting websockets
        self._types = ["ticker", "transaction", "orderbookdepth"]
        self._alive = {"ticker": False, "transaction": False, "orderbookdepth": False}
        self._q = {"ticker": mp.Queue(1000), "transaction": mp.Queue(1000), "orderbookdepth": mp.Queue(1000)}
        self.request_types_info()
        self.get_tikcer_info()

    def run(self) -> None:
        '''
        Every 0.1 second, if data in the queue from websocket, bring it
        Type of websocket data: ticker(current price), transaction(contract), orderbookdepth
        if you need a specific type, you can get data using by 'self._q[type].get()
        Usage:
            if self._q["ticker"] and self._q["transaction"] and self._q["orderbookdepth"]:
                for type in self.__types:
                    print(type, '\n', self._q[type].get())
        '''
        ws_tickers = [ticker + '_KRW' for ticker in self._tickers]
        print(ws_tickers)
        while True:
            if self._q["ticker"]:
                data = self._q['ticker'].get()

                if data['content']['symbol'] in ws_tickers:
                    lowPrice = data['content']['lowPrice']              # 저가
                    highPrice = data['content']['highPrice']            # 고가
                    value = data['content']['value']                    # 누적 거래금액
                    prevClosePrice = data['content']['prevClosePrice']  # 전일 종가
                    chgRate = data['content']['chgRate']                # 변동률
                    chgAmt = data['content']['chgAmt']                  # 변동 금액
                    date = data['content']['date']                      # 일자
                    _time = data['content']['time']                     # 시간

                print(f"코인 종류:      {data['content']['symbol']}",
                      f"저가:         {lowPrice}원",
                      f"고가:         {highPrice}원",
                      f"누적 거래 금액:  {round(float(value))}원",
                      f"전일 종가:      {prevClosePrice}원",
                      f"변동률:        {chgRate}%",
                      f"변동 금액:      {chgAmt}원",
                      f"현재가:        {int(prevClosePrice) + int(chgAmt)}원",
                      '\n',
                      sep="\n"
                      )

    def get_asset_data(self):
        '''
        load client's asset data in Queue
        :return: asset_info(list in dictionary)
        '''
        global asset_info

        while not self._q['ticker'].empty():
            data = self._q['ticker'].get()
            value = float(data['content']['value'])  # 누적 거래금액
            prevClosePrice = float(data['content']['prevClosePrice'])  # 전일 종가
            chgRate = float(data['content']['chgRate'])  # 변동률
            chgAmt = float(data['content']['chgAmt']) # 변동 금액
            cur_price = int(prevClosePrice) + int(chgAmt)
            symbol = data['content']['symbol'][:-4]
            asset_info[symbol] = {"ticker" : symbol, "value":value, "chgRate":chgRate, "chgAmt":chgAmt, "cur_price":cur_price}

        return asset_info

    def get_coin_data(self):
        '''
        load coin data in Queue
        :return: coin_info(list in dictionary)
        '''
        global coin_info

        while not self._q['ticker'].empty():
            data = self._q['ticker'].get()
            value = float(data['content']['value'])  # 누적 거래금액
            prevClosePrice = float(data['content']['prevClosePrice'])  # 전일 종가
            chgRate = float(data['content']['chgRate'])  # 변동률
            chgAmt = float(data['content']['chgAmt']) # 변동 금액
            cur_price = int(prevClosePrice) + int(chgAmt)
            symbol = data['content']['symbol'][:-4]
            coin_info[symbol] = {"ticker" : symbol, "value":value, "chgRate":chgRate, "chgAmt":chgAmt, "cur_price":cur_price}

        return coin_info



    def request_types_info(self):
        '''
        inform the type of request
        '''
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
        '''
        connect websocket
        :param type: data type
        :param symbols: data symbols
        original code:
            https://github.com/sharebook-kr/pybithumb/blob/master/pybithumb/websocket.py
        '''

        uri = "wss://pubwss.bithumb.com/pub/ws"

        async with websockets.connect(uri, ping_interval=None) as websocket:
            connection_msg = await websocket.recv()
            # {"status":"0000","resmsg":"Connected Successfully"}
            if "Connected Successfully" not in connection_msg:
                print("connection error")

            data = {
                "type": type,
                'symbols': symbols,
                'tickTypes': ["MID"]
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
        '''
        start websocket
        :param type: data type
        :param symbols: data symbols
        '''
        self._alive[type] = True
        self._aloop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._aloop)
        self._aloop.run_until_complete(self.connect_websocket(type, symbols))

    def get_type_info(self, type, ws_tickers):
        '''
        get the type of information
        :param type: data type
        :param ws_tickers: websocket tickers
        '''
        self.start_websocket(type, ws_tickers)

    def get_tikcer_info(self):
        '''
        get the type of tickers
        '''
        #self._ws_ticker_process = Process(name="ticker", target=self.run)
        #self._ws_ticker_process.start()
        pass

    def terminate(self):
        '''
        terminate the processing
        '''
        for type in self._types:
            self._alive[type] = False
