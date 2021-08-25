# main.py
from src import create_app
from src.pybithumb.ClientAsset import ClientAsset
from src.pybithumb.ApiConnect import Connect
from src.pybithumb.RealTimeWebsocketProcess import RealTimeWebsocketProcess

import pybithumb

app = create_app("dev")

if __name__ == '__main__':

	websocket = RealTimeWebsocketProcess(pybithumb.Bithumb.get_tickers())

	app.run()