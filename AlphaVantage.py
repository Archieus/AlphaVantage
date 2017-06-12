import json
import requests
rawdata = requests.get('http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&outputsize=compact&apikey=Y474')

data = json.loads(rawdata.text)

print(data)

inner_dict = data['Time Series (Daily)']

for key in inner_dict.keys():
    print('{}: {}'.format(key, inner_dict[key]))
