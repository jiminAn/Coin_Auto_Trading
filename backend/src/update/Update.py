from src.model.models import Client, Coin
from src.database import db
from src.crawling.CrawledInfo import  *
from src.pybithumb.ApiConnect import *
from src import create_app
app = create_app("dev")
app.app_context().push()

from datetime import datetime
import pybithumb



class UpdateDB:
    def __init__(self):
        self._tickers = create_ticker_name_dict()
        self._client = Connect()

    def updateCoinInfo(self):
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
        client_api = self._client.get_con_key() # client connect key
        buy_time = datetime.now()
        ticker_time = client_api + str(buy_time) # PK : client connect key + ticker
        name = self._tickers[ticker] # ticker's korean name
        #hoding_krw 보유원화 잔고는 보류


        client = Client(client_api=client_api, ticker_time=ticker_time, name=name, ticker=ticker,
                        buy_price=buy_price, buy_time=buy_time, quantity=quantity, fee=fee)
        db.session.add(client)
        db.session.commit()


if __name__ == "__main__":
    DB = UpdateDB()
    DB.updateClientAssetInfo('BTC', 1, 5500, 0.01)