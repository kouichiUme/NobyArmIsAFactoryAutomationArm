import requests
from pprint import pprint

r = requests.get('https://api.bitflyer.jp/v1/board?product_code=BTC_JPY')
json = r.json()
pprint(json)