from collections import defaultdict
import re
import pprint as pp


def create_ticker_name_dict():
    """
    create a dictionary that matches korean ticker's naming
    :return: tickers['ticker'] = name
    """
    cnt = 0
<<<<<<< HEAD
    limit = 20 # the limited number of tickers
    tickers = defaultdict()
    with open('../tickernames.txt', 'r', encoding= 'utf-8') as f:
=======
    limit = 20
    tickers = defaultdict()
    PATH = '/Users/anjimin/git/Coin_Auto_Trading/backend/src/cralwing'
    with open(PATH + '/tickernames_250.txt', 'r') as f:
>>>>>>> feature/websocket
        for line in f.readlines():
            cnt += 1
            ticker = re.findall('[a-zA-Z].*',line)[0]
            ko_name = line.replace(ticker,'').strip()
<<<<<<< HEAD
            
=======
            #print(ticker, ':', ko_name) # for CHECKING

>>>>>>> feature/websocket
            tickers[ticker] = ko_name
            if cnt == limit:
                break

    return tickers

<<<<<<< HEAD
if __name__ == "__main__":
     tickers_ko_naming = create_ticker_name_dict()
     pp.pprint(tickers_ko_naming)
=======


if __name__ == "__main__":
    tickers_ko_naming = create_ticker_name_dict()
    pp.pprint(tickers_ko_naming)
>>>>>>> feature/websocket
