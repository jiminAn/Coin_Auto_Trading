import pybithumb
import datetime
import time
from collections import defaultdict
from .bestk import findk
import configparser
from .model.Update import UpdateDB


class BitcoinAuto():
    def __init__(self, connect, clientasset):
        """
        Initialize Objects and Variables
        """
        
        # Objects
        self.clientasset = clientasset
        self.connect = connect
        # self.db = UpdateDB()
        
        # Variables
        self._now = datetime.datetime.now() # 현재 시간
        self._mid = datetime.datetime(self._now.year, self._now.month, self._now.day) + datetime.timedelta(days=1) # 다음 날
        self._ma5 = dict() # 각 코인의 5일간의 이동평균
        self._k = dict() # 각 코인의 최적의 k 값 (딕셔너리로 수정 예정)
        self._target_price = dict() # 각 코인의 타겟가 (딕셔너리로 수정 예정)
        self._bithumb = self.connect.get_bithumb() # 빗썸 객체
        self._my_tickers = self.clientasset.get_ticker() # 내가 가지고 있는 Ticker
        self._minimum_order = self.init_minimum_order()

        # PATH
        self._config = configparser.ConfigParser()
        self._config.read('src/config.ini', encoding='utf-8')
        self._log_path = self._config['PATH']['log']

        
    def get_target_price(self, ticker, k):
        '''
        A function that makes a target selling price.
        :param ticker: Ticker information that the user has.
        :param k: The best value of k.
        :return: None
        '''
        df = pybithumb.get_ohlcv(ticker)
        yesterday = df.iloc[-2]
        today_open = yesterday['close']
        yesterday_high = yesterday['high']
        yesterday_low = yesterday['low']
        target = today_open + (yesterday_high - yesterday_low) * k
        return round(target, 1)


    def buy_crypto_currency(self, ticker):
        '''
        Buying coins.
        :param ticker: Ticker information that the user has.
        :return: None
        '''
        krw = self._bithumb.get_balance(ticker)[2]
        print(krw)
        if krw < 500:
            with open(self._log_path, "a") as f:
                f.write(self.get_curr_time() + "|돈이 500원 이하입니다.\n")
            return

        orderbook = pybithumb.get_orderbook(ticker)
        sell_price = orderbook['asks'][0]['price']
        unit = float(format(krw / float(sell_price), '.6f'))

        if unit < self._minimum_order[self.get_minimum_orders_key(sell_price)]:
            with open(self._log_path, "a") as f:
                f.write(self.get_curr_time() + "|주문 가능 금액을 초과했습니다.\n")
            return

        self._bithumb.buy_market_order(ticker, unit)
        fee = self._bithumb.get_trading_fee(ticker)
        # self.db.updateClientAssetInfo(ticker, unit, pybithumb.get_ohlcv(ticker), fee)


    def sell_crypto_currency(self, ticker):
        '''
        Selling coins.
        :param ticker: Ticker information that the user has.
        :return: None
        '''
        unit = self._bithumb.get_balance(ticker)[0]
        tmp = self._bithumb.sell_market_order(ticker, unit)
        if isinstance(tmp, tuple):
            fee = self._bithumb.get_trading_fee(ticker)
            # self.db.updateClientAssetInfo(ticker, -unit, pybithumb.get_ohlcv(ticker), fee)
            with open(self._log_path, "a") as f:
                f.write(self.get_curr_time() +"|" + ticker + "판매 완료\n")

        else:
            with open(self._log_path, "a") as f:
                f.write(self.get_curr_time() + "|" + tmp['status'] + ":" + tmp['message'])


    def get_yesterday_ma5(self, ticker):
        '''
        A function that calculates the 5-day moving average
        for each trading day and returns the 5-day moving average value
        of the previous day based on the inquiry date.
        :param ticker: Ticker information that the user has.
        :return: ma[-2] : Moving average for 5 days.
        '''
        df = pybithumb.get_ohlcv(ticker)
        close = df['close']
        ma = close.rolling(5).mean()
        return ma[-2]
    

    def buy_by_condition(self, tickers):
        '''
        Coin purchase according to the purchase conditions set by the developer.
        :param tickers: ticker information that the user has.
        :return: None
        '''
        for ticker in tickers:
            current_price = pybithumb.get_current_price(ticker)
            log_data = {"ticker": ticker, "currentPrice ": current_price, "targetPrice": self._target_price[ticker],
                        "rolling": self._ma5[ticker], "money": self._bithumb.get_balance(ticker)[2]}

            if current_price > self._target_price[ticker]:
                self.buy_crypto_currency(ticker)

    def sell_by_condition(self, tickers):
        '''
        Selling coin according to the selling conditions set by the developer.
        :param tickers: ticker information that the user has.
        :return: None
        '''
        now = datetime.datetime.now()
        for ticker in tickers:
            if self._mid < now < self._mid + datetime.timedelta(seconds=10):
                self._k[ticker] = findk.get_max_ror_k(ticker)
                self._target_price[ticker] = self.get_target_price(ticker, self._k[ticker])
                self._mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
                self._ma5[ticker] = self.get_yesterday_ma5(ticker)
                self.sell_crypto_currency(ticker)


    def init_minimum_order(self):
        '''
        Find the minimum order amount for ticker.
        '''
        cnt, val = 0, 10
        ret = defaultdict(int)
        while True:
            if cnt >= 7:
                break
            ret[cnt] = val
            if cnt >= 1:
                val /= 10
            cnt += 1
        return ret


    def get_curr_time(self):
        '''
        Find the current time.
        :param tickers: 
        :return: "%04d/%02d/%02d|%02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        '''
        now = time.localtime()
        return "%04d/%02d/%02d|%02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    
    def get_minimum_orders_key(self, sell_price):
        '''
        Find the minimul order key using the present value.
        param sell_price : ticker's current price
        '''
        if sell_price < 100:
            return 1
        elif 100 <= sell_price < 1000:
            return 2
        elif 1000 <= sell_price < 10000:
            return 3
        elif 10000 <= sell_price < 100000:
            return 4
        elif 100000 <= sell_price < 1000000:
            return 5
        else:
            return 6


    def auto_start(self):
        '''
        Start autotrading
        :return: None
        '''
        with open(self._log_path, "w") as f:
            f.write(self.get_curr_time() + "|Auto Start\n")

        if self._my_tickers is None:  # 예외
            with open(self._log_path, "w") as f:
                f.write(self.get_curr_time() + "|보유한 코인이 없습니다.\n")
            return

        for ticker in self._my_tickers:
            self._k[ticker] = findk.get_max_ror_k(ticker)
            self._target_price[ticker] = self.get_target_price(ticker, self._k[ticker])
            self._ma5[ticker] = self.get_yesterday_ma5(ticker)

        while True:
            try:
                self.sell_by_condition(self._my_tickers)
                self.buy_by_condition(self._my_tickers)

            except Exception as e:
                with open(self._log_path, "w") as f:
                    f.write(self.get_curr_time() + "|" + str(e) + "|자동매매 시스템을 종료합니다.\n")
                    return 0
