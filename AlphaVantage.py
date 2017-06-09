import json
import requests
rawdata = requests.get('http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&outputsize=compact&apikey=Y474')

print (rawdata.json())
