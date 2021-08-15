import pybithumb
import datetime
import time
from collections import defaultdict
from .bestk import findk
from .pybithumb.ApiConnect import Connect
from .pybithumb.ClientAsset import ClientAsset


class BitcoinAuto():
    def __init__(self):
        """
        Initialize Objects and Variables
        """
        # Objects
        self.connect = Connect()
        self.clientasset = ClientAsset(self.connect)

        # Variables
        self._now = datetime.datetime.now() # 현재 시간
        self._mid = datetime.datetime(self._now.year, self._now.month, self._now.day) + datetime.timedelta(days=1) # 다음 날
        self._ma5 = dict() # 각 코인의 5일간의 이동평균
        self._k = dict() # 각 코인의 최적의 k 값 (딕셔너리로 수정 예정)
        self._target_price = dict() # 각 코인의 타겟가 (딕셔너리로 수정 예정)
        self._bithumb = self.connect.get_bithumb() # 빗썸 객체
        self._my_tickers = self.clientasset.get_ticker() # 내가 가지고 있는 Ticker


    def get_target_price(self, ticker, k):
        """
        목표 매도가를 만드는 함수
        :param ticker: 사용자의 Ticker
        :param k: 최적의 k값 
        :return: None
        """
        df = pybithumb.get_ohlcv(ticker)
        yesterday = df.iloc[-2]
        today_open = yesterday['close']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        target = today_open + (yesterday_high - yesterday_low) * k
        return target

    def buy_crypto_currency(self, ticker):
        """
        실제 매수가 일어나는 함수
        :param ticker: ticker
        :return: None
        """
        krw = self._bithumb.get_balance(ticker)[2]
        orderbook = pybithumb.get_orderbook(ticker)
        sell_price = orderbook['asks'][0]['price']
        unit = krw / float(sell_price)
        self._bithumb.buy_market_order(ticker, unit)

    def sell_crypto_currency(self, ticker):
        """
        실제 매도가 일어나는 함수
        :param ticker: ticker
        :return: None
        """
        unit = self._bithumb.get_balance(ticker)[0]
        self._bithumb.sell_market_order(ticker, unit)

    def get_yesterday_ma5(self, ticker):
        """
        거래일별로 5일 이동평균을 계산한 후 조회일 기준으로 전일의 5일 이동평균 값을 반환하는 함수
        :param ticker: ticker
        :return: ma[-2] : ticker의 5일 간 이동평균
        """
        df = pybithumb.get_ohlcv(ticker)
        close = df['close']
        ma = close.rolling(5).mean()
        return ma[-2]

    def buy_by_condition(self, tickers):
        """
        사용자 조건에 맞추어 비트코인 매수
        :param tickers: 사용자가 가지고 있는 비트코인 정보 
        :return: None
        """
        for ticker in tickers:
            current_price = pybithumb.get_current_price(ticker)
            print("Ticker :", ticker,", Current Price :" , current_price, ", Target Price :", self._target_price[ticker],
                  "5일 간 이동평균" ,self._ma5[ticker], ", Money :" , self._bithumb.get_balance(ticker)[2])

            if (current_price > self._target_price[ticker]) and (current_price > self._ma5[ticker]):
                self.buy_crypto_currency(ticker)

    def sell_by_condition(self, tickers):
        """
        사용자 조건에 맞추어 비트코인 매도
        :param tickers: 사용자가 가지고 있는 비트코인 정보 
        :return: None
        """
        now = datetime.datetime.now()
        for ticker in tickers:
            if self._mid < now < self._mid + datetime.timedelta(seconds=10):
                self._k[ticker] = findk.get_max_ror_k(ticker)
                self._target_price[ticker] = self.get_target_price(ticker, self._k[ticker])
                self._mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
                self._ma5[ticker] = self.get_yesterday_ma5(ticker)
                self.sell_crypto_currency(ticker)

    def auto_start(self):
        """
        자동매매 코드
        :return: None
        """

        for ticker in self._my_tickers:
            self._k[ticker] = findk.get_max_ror_k(ticker)
            self._target_price[ticker] = self.get_target_price(ticker, self._k[ticker])
            self._ma5[ticker] = self.get_yesterday_ma5(ticker)

        while True:
            try:
                self.sell_by_condition(self._my_tickers)
                self.buy_by_condition(self._my_tickers)
                
            except Exception as e:
                print("에러 발생", e)
            time.sleep(1)