import json
import requests

symbol = input("Enter a stock symbol\n")

rawdata = requests.get('http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=compact&apikey=Y474'.format(symbol))

data = json.loads(rawdata.text)

print(data)

inner_dict = data['Time Series (Daily)']

for key in inner_dict.keys():
    print('{}: {}'.format(key, inner_dict[key]))
