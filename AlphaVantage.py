#!/usr/bin/env python
import json
import requests
import numpy as np
from sklearn import linear_model

json_keys = ('Time Series (Daily)', '1. open')

symbol1 = input("Enter a stock symbol\n")
symbol2 = input("Enter another stock symbol\n")

rawdata1 = requests.get('http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=compact&apikey=Y474'.format(symbol1))

rawdata2 = requests.get('http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=compact&apikey=Y474'.format(symbol2))

data1 = json.loads(rawdata1.text)
data2 = json.loads(rawdata2.text)

inner_dict1 = data1[json_keys[0]]
inner_dict2 = data2[json_keys[0]]

open_values1 = []
open_values2 = []

for key in sorted(inner_dict1.keys()):
    open_values1.append((key.replace('-', '').split(' ')[0], inner_dict1[key][json_keys[1]]))

for key in sorted(inner_dict2.keys()):
    open_values2.append((key.replace('-', '').split(' ')[0], inner_dict2[key][json_keys[1]]))

a = []
for i in range(len(open_values1)):
    a.append([open_values1[i][1], open_values2[i][1]])

a = np.array(a)
b = np.array(list(x[0] for x in open_values1))

a.reshape(len(a), 2)
b.reshape(len(open_values2), 1)

a = a.astype(np.float).tolist()
b = b.astype(np.int).tolist()

clf = linear_model.LinearRegression()
clf.fit(a, b)

print(clf.coef_)
