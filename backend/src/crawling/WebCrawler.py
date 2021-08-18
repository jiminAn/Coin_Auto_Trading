import requests
from bs4 import BeautifulSoup


url = 'https://www.bithumb.com/'
html = requests.get(url).text

soup = BeautifulSoup(html,'html.parser')
coins = soup.select('.coin_list tr')

with open('bithumb.txt', 'w', encoding='utf-8') as f:
    for coin in coins:
        ticker = coin.select_one('td:nth-of-type(1) p a').text.strip()
        f.write(f'{ticker}\n')
