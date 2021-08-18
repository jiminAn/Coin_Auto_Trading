from src.model.models import Client, Coin
from src.database import db
from src.cralwing.CrawledInfo import  *
from datetime import datetime
import pybithumb
from src import create_app
app = create_app("dev")
app.app_context().push()


if __name__ == "__main__":
    tickers = create_ticker_name_dict()
    for ticker, ko_name in tickers.items():
        infos = pybithumb.get_market_detail(ticker)
        open, high, low, close, volume  = infos
        full_date = datetime.now()
        date = full_date.strftime('%Y-%m-%d')
        coin = Coin(name=ko_name,ticker_date=ticker+date,ticker = ticker, datetime=full_date,open=open, high=high, low=low, close=close, volume=volume)
        db.session.add(coin)
        db.session.commit()

