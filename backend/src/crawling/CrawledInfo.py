from collections import defaultdict
import re
import pprint as pp


def create_ticker_name_dict():
    """
    create a dictionary that matches korean ticker's naming
    :return: tickers['ticker'] = name
    """
    cnt = 0
    limit = 20  # the limited number of tickers
    tickers = defaultdict()
    PATH = "/Users/mac/git/Coin_Auto_Trading/backend/src"
    with open(PATH + '/tickernames.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            cnt += 1
            ticker = re.findall('[a-zA-Z].*', line)[0]
            ko_name = line.replace(ticker, '').strip()

            tickers[ticker] = ko_name
            if cnt == limit:
                break

    return tickers


if __name__ == "__main__":
    tickers_ko_naming = create_ticker_name_dict()
    pp.pprint(tickers_ko_naming)
