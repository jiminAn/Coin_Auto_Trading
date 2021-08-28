# main.py
from src import create_app
from src.pybithumb.RealTimeWebsocketProcess import RealTimeWebsocketProcess
from pybithumb import Bithumb
#from src.model.models import User
app = create_app("dev")

if __name__ == '__main__':
	websocket = RealTimeWebsocketProcess(Bithumb.get_tickers())

	app.run()