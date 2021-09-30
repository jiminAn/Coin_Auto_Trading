from collections import defaultdict

from backend.src import create_app, db
from backend.src.crawling.CrawledInfo import create_ticker_name_dict
from backend.src.model.models import Coin, Client
from backend.src.pybithumb.ApiConnect import Connect

import datetime
import pybithumb

class UpdateDB:
    """
    Search, Update, Delete Coin & Client table
    """
    def __init__(self):
        """
        initialize ticker dictionary and connect client api
        """
        self._tickers = create_ticker_name_dict()
        self._client = Connect()
        self._app = create_app("dev")
        
    def updateCoinInfo(self):
        """
        Insert Coin information for every AM 00:00
        """
        for ticker, ko_name in self._tickers.items():
            infos = pybithumb.get_market_detail(ticker)
            open, high, low, close, volume = infos
            full_date = datetime.now()
            date = full_date.strftime('%Y-%m-%d')
            coin = Coin(name=ko_name, ticker_date=ticker + date, ticker=ticker, datetime=full_date, open=open,
                        high=high, low=low, close=close, volume=volume)

            db.session.add(coin)
            db.session.commit()

    def updateClientAssetInfo(self, ticker, quantity, buy_price, fee):
        """
        Insert Client asset information for every sell and buy
        :param ticker: buying or selling ticker eng name
        :param quantity: buying or selling quantity
        :param buy_price:buying or selling price
        :param fee: buying or selling fee
        """
        client_api = self._client.get_con_key() # client connect key
        buy_time = datetime.now()
        ticker_time = client_api + str(buy_time) # PK : client connect key + ticker
        name = self._tickers[ticker] # ticker's korean name

        # insert client's asset information
        client = Client(client_api=client_api, ticker_time=ticker_time, name=name, ticker=ticker,
                        buy_price=buy_price, buy_time=buy_time, quantity=quantity, fee=fee)
        # db add & commit
        db.session.add(client)
        db.session.commit()

    def delete(self, pk_list):
        """
        Delete rows in Primary Key list
        :param pk_list: primary keys(list)
        :return: success(True) / fail(False)
        """
        if not pk_list:
            return False
        else:
            for row in pk_list:
                db.session.delete(row)
                db.session.commit()
            return True

    def searchTicker(self, table, ticker):
        """
        get Primary Key from each table filter with ticker
        :param table: Name of table
        :param ticker: ticker name
        :return: Primary Key(List)
        """
        pk_list = table.query.filter(table.ticker == ticker).all()
        return pk_list

    def searchName(self, table, name):
        """
        get Primary Key from each table filter with name
        :param table: Name of table
        :param name: ticker name
        :return: Primary Key(List)
        """
        pk_list = table.query.filter(table.name == name).all()
        return pk_list

    def searchDatetime(self, table, datetime):
        """
        get Primary Key from each table filter with datetime
        :param table: Name of table
        :param datetime: date time
        :return: Primary Key(Lst)
        """
        pk_list = table.query.filter(table.datetime.like('%'+datetime+'%')).all()
        return pk_list

    def getClientAsset(self,client_api):
        """
        get the client's asset
        :param client_api: connect key
        :return: client's asset information
        """
        client_asset_info = []
        info_list = db.session.query(Client.name, Client.ticker, Client.buy_price, Client.buy_time
                                     , Client.quantity, Client.fee).filter_by(client_api=client_api).all()

        if not info_list:
            return [{'name': "", 'ticker': "", 'buy_price': 0, 'buy_time': "", 'quantity': 0, 'fee': 0,
                     'open': 0, 'high': 0, 'low': 0, 'close': 0, 'volume': 0}]
        else :
            for info in info_list:
                name, ticker, buy_price, buy_time, quantity, fee = info
                dt = {}
                dt["name"] = name
                dt["ticker"] = ticker
                dt["buy_price"] = buy_price
                dt["buy_time"] = buy_time
                dt["quantity"] = quantity
                dt["fee"] = fee
                #additional info(update 24H)
                coin_detals = pybithumb.get_ohlcv(ticker)
                dt["open"] = coin_detals['open'][-2]
                dt["high"] = coin_detals['high'][-2]
                dt["low"] = coin_detals['low'][-2]
                dt["close"]= coin_detals['close'][-2]
                dt["volume"] = coin_detals['volume'][-2]
                client_asset_info.append(dt)
        return client_asset_info

    def getTickersInfo(self, datetime):
        """
        get top 20 coin information
        :param datetime(str):
        :return: top 20 coin information
        """
        tickerInfo = []
        infoList = db.session.query(Coin.name, Coin.ticker, Coin.datetime, Coin.open
                    , Coin.high, Coin.low, Coin.close, Coin.volume).filter(Coin.datetime.like('%'+datetime+'%')).all()

        if not infoList:
            return [{'name': "", 'ticker': "", 'datetime': "", 'open': 0, 'high': 0, 'low': 0, 'close': 0, 'volume': 0}]
        else:
            for info in infoList:
                name, ticker, datetime, open, high, low, close, volume = info

                dt = { 'name': name, 'ticker': ticker, 'datetime': datetime, 'open': open, 'high': high, 'low': low,
                       'close': close, 'volume': volume}

                tickerInfo.append(dt)

        return tickerInfo

if __name__ == "__main__":
    #for TEST
    DB = UpdateDB()
    #DB.updateCoinInfo()
    date1 = '2021-09-30'
    date2 = '2021-09-29'
    print(DB.getClientAsset("1e1f0025831be87f41ca6c3710af876d"))
    print(DB.getClientAsset("8138240ab46ec4b73f064f3f9fd9df73"))
    print(DB.getTickersInfo(date1))
    print(DB.getTickersInfo(date2))
    #DB.updateClientAssetInfo('BTC', 1.1, 5132163.0, 1.1)
    #DB.updateClientAssetInfo('DOGE', 2.1, 2163.0, 1.1)
    #DB.updateClientAssetInfo('EOS', 10.1, 63163.0, 1.1)

    # CURD + 예외 처리
    #dt = DB.searchDatetime(Coin,date)
    #DB.delete(dt)  # 매달 1일 삭제

    
