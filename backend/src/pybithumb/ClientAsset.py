import pybithumb
from collections import defaultdict


class ClientAsset:
    """
    load the Client Asset information
    """
    _ticker_dict = defaultdict(list)
    _client_api = None

    def __init__(self, connect):
        """
        inquire all tickers and save Client's asset information
        """
        self._client_api = connect
        tickers = pybithumb.get_tickers()
        for ticker in tickers:
            balance = self._client_api.get_balance(ticker)
            if balance[0] > 0.0:
                self._ticker_dict[ticker].append(balance)

    def get_ticker(self):
        """
        get the ticker list of client asset
        :return: tickers(List)
        """
        return [ticker for ticker in self._ticker_dict.keys()]

    def get_ticker_dict(self):
        """
        get client asset information
        :return: ticker information(Dict); {ticker : [client asset information]}
        """
        return self._ticker_dict