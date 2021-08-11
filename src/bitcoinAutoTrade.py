import pybithumb
import datetime
import time
from collections import defaultdict
from .bestk import findk
from .pybithumb.ApiConnect import Connect
from .pybithumb.ClientAsset import ClientAsset

class BitcoinAuto():
    def __init__(self):
        # Object
        self.connect = Connect()
        self.clientasset = ClientAsset(self.connect)

        # 변수
        self._now = datetime.datetime.now()
        self._mid = datetime.datetime(self._now.year, self._now.month, self._now.day) + datetime.timedelta(days=1)
        self._ma5 = defaultdict(float)
        self._k = findk.get_max_ror_k(self)
        self._target_price = 0.0
        self._bithumb = self.connect.get_bithumb()
        self._my_tickers = self.clientasset.get_ticker()
    # 목표가 갱신

    def get_target_price(self, ticker, k):
        df = pybithumb.get_ohlcv(ticker)
        yesterday = df.iloc[-2]

        today_open = yesterday['close']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        target = today_open + (yesterday_high - yesterday_low) * k
        return target

    def buy_crypto_currency(self, ticker):
        krw = self._bithumb.get_balance(ticker)[2]
        orderbook = pybithumb.get_orderbook(ticker)
        sell_price = orderbook['asks'][0]['price']
        unit = krw / float(sell_price)
        self._bithumb.buy_market_order(ticker, unit)

    def sell_crypto_currency(self, ticker):
        unit = self._bithumb.get_balance(ticker)[0]
        self._bithumb.sell_market_order(ticker, unit)

    def get_yesterday_ma5(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        close = df['close']
        ma = close.rolling(5).mean()
        return ma[-2]

    def buy_by_condition(self, tickers):
        for ticker in tickers:
            print("buy:", ticker)
            current_price = pybithumb.get_current_price(ticker)
            if (current_price > self._target_price) and (current_price > self._ma5[ticker]):
                self.buy_crypto_currency(ticker)

    def sell_by_condition(self, tickers):
        now = datetime.datetime.now()
        for ticker in tickers:
            if self._mid < now < self._mid + datetime.timedelta(seconds=10):
                self._target_price = self.get_target_price(ticker, self.k)
                self._mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
                self._ma5[ticker] = self.get_yesterday_ma5(ticker)
                self.sell_crypto_currency(ticker)

    def auto_start(self):
        while True:
            try:
                print("작동 중")
                self.sell_by_condition(self._my_tickers)
                self.buy_by_condition(self._my_tickers)
                
            except Exception as e:
                print("에러 발생", e)
            time.sleep(1)