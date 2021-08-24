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
    with open('../tickernames.txt', 'r', encoding= 'utf-8') as f:
        for line in f.readlines():
            cnt += 1
            ticker = re.findall('[a-zA-Z].*',line)[0]
            ko_name = line.replace(ticker,'').strip()
            #print(ticker, ':', ko_name) # for CHECKING

            tickers[ticker] = ko_name
            if cnt == limit:
                break

    return tickers


def create_asset_name_dict(asset_list):
    list = asset_list
    tickers = defaultdict()
    index = 0
    limit = len(list)
    with open('../tickernames.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            ticker = re.findall('[a-zA-Z].*', line)[0]
            ko_name = line.replace(ticker, '').strip()
            if list[index] == ticker:
                index += 1
                tickers[ticker] = ko_name

            if index == limit:
                break
    return tickers

if __name__ == "__main__":
     tickers_ko_naming = create_asset_name_dict()
     pp.pprint(tickers_ko_naming)
