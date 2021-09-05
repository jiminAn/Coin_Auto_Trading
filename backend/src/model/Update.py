from ..model.models import Client, Coin
from ..database import db
from ..crawling.CrawledInfo import *
from ..pybithumb.ApiConnect import *
from ...main import create_app

app = create_app("dev")
app.app_context().push()

from datetime import datetime
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
        Insert Client asset information for every sell & buy
        """
        client_api = self._client.get_con_key() # client connect key
        buy_time = datetime.now()
        ticker_time = client_api + str(buy_time) # PK : client connect key + ticker
        name = self._tickers[ticker] # ticker's korean name
        #hoding_krw 보유원화 잔고는 보류


        client = Client(client_api=client_api, ticker_time=ticker_time, name=name, ticker=ticker,
                        buy_price=buy_price, buy_time=buy_time, quantity=quantity, fee=fee)

        db.session.add(client)
        db.session.commit()

    def delete(self, pk_list):
        """
        Delete rows in Primary Key list
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
        :return: Primary Key(List)
        """
        pk_list = table.query.filter(table.ticker == ticker).all()
        return pk_list

    def searchName(self, table, name):
        """
        get Primary Key from each table filter with name
        :return: Primary Key(List)
        """
        pk_list = table.query.filter(table.name == name).all()
        return pk_list

    def searchDatetime(self, table, datetime):
        """
        get Primary Key from each table filter with datetime
        :return: Primary Key(List)
        """
        pk_list = table.query.filter(table.datetime.like('%'+datetime+'%')).all()
        return pk_list


if __name__ == "__main__":
    DB = UpdateDB()
    #DB.updateCoinInfo()
    date = '2021-09-01'

    # CRUD + 예외 처리
    dt = DB.searchDatetime(Coin,date)
    DB.delete(dt)  # 매달 1일 삭제

    
