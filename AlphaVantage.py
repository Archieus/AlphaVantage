#!/usr/bin/env python
import json
import requests
import numpy as np
from sklearn import linear_model
from scipy import stats

json_keys = ('Time Series (Daily)', '4. close')

symbol1 = input("Enter a stock symbol\n")
symbol2 = input("Enter another stock symbol\n")

rawdata1 = requests.get('http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=compact&apikey=Y474'.format(symbol1))

rawdata2 = requests.get('http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=compact&apikey=Y474'.format(symbol2))

data1 = json.loads(rawdata1.text)
data2 = json.loads(rawdata2.text)

inner_dict1 = data1[json_keys[0]]
inner_dict2 = data2[json_keys[0]]

values1 = []
values2 = []

for key in sorted(inner_dict1.keys()):
    values1.append((key.replace('-', '').split(' ')[0], inner_dict1[key][json_keys[1]]))

for key in sorted(inner_dict2.keys()):
    values2.append((key.replace('-', '').split(' ')[0], inner_dict2[key][json_keys[1]]))

a = []
for i in range(len(values1)):
    a.append([values1[i][1], values2[i][1]])

a = np.array(a)
b = np.array(list(x[0] for x in values1))

a.reshape(len(a), 2)
b.reshape(len(values2), 1)

a = a.astype(np.float).tolist()
b = b.astype(np.int).tolist()

clf = linear_model.LinearRegression()
clf.fit(a, b)

foo1 = [float(x[1]) for x in values1]
foo2 = [float(x[1]) for x in values2]

slope, intercept, r_value, p_value, std_err = stats.linregress(foo1, foo2)
print(slope, intercept)

print(clf.coef_)
