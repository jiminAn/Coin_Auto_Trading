from collections import defaultdict
import re
import pprint as pp


def create_ticker_name_dict():
    """
    create a dictionary that matches korean ticker's naming
    :return: tickers['ticker'] = name
    """
    cnt = 0
    limit = 20
    tickers = defaultdict()
    PATH = '/Users/anjimin/git/Coin_Auto_Trading/backend/src/cralwing'
    with open(PATH + '/tickernames_250.txt', 'r') as f:
        for line in f.readlines():
            cnt += 1
            ticker = re.findall('[a-zA-Z].*',line)[0]
            ko_name = line.replace(ticker,'').strip()
            #print(ticker, ':', ko_name) # for CHECKING

            tickers[ticker] = ko_name
            if cnt == limit:
                break

    return tickers



if __name__ == "__main__":
    tickers_ko_naming = create_ticker_name_dict()
    pp.pprint(tickers_ko_naming)