
#-------------------------------------------------------------------------
import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

querystring = {"region":"US","symbols":"AAPL"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data =response.text
data = json.loads(data)

print(data["quoteResponse"]["result"][0]["regularMarketPrice"])




print(response.text)


5









import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

querystring = {"symbol":"AAPL","interval":"1m","range":"1d","region":"US","comparisons":"TSLA"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


data =response.text
data = json.loads(data)
data["chart"]["result"][0]["timestamp"][1]
data["chart"]["result"][0]["indicators"]["quote"][0]["low"][1]
data["chart"]["result"][0]["indicators"]["quote"][0]["high"][1]
data["chart"]["result"][0]["indicators"]["quote"][0]["close"][1]



import pandas as pd

nas = pd.read_csv("nasdaq_symbols.csv")

nasList = nas.Symbol.tolist()
import random

desired_number = 13
guesses = list(range(0,len(nasList)))
random.shuffle(guesses)
indexes = guesses[:20]



savingNas = nas.loc[indexes , ['Symbol']  ]
savingNas = savingNas["Symbol"].tolist()

savingNas.append("AAPL")
df = pd.DataFrame({"symbol" : savingNas , "longName" : longName})
df.to_csv("symbol_names.csv" , index = False)
pd.read_csv("symbol_names.csv")

savingNas

len(longName)



import requests
import json
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
import time
longName = []
for symbol in savingNas:
    print(symbol)
    querystring = {"region":"US","symbols":symbol}
    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data =response.text
    data = json.loads(data)

    longName.append(data["quoteResponse"]["result"][0]["longName"])
    time.sleep(5)







data



data["quoteResponse"]["result"][0]["regularMarketVolume"]
data["quoteResponse"]["result"][0]["averageDailyVolume3Month"]
data["quoteResponse"]["result"][0]["averageDailyVolume10Day"]


import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-movers"

querystring = {"region":"US","lang":"en-US","count":"6","start":"0"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data2 = response.text
data2 = json.loads(data2)
for i in data2["finance"]["result"][0].keys():
    print(i)

data2["finance"]["result"][0]["quotes"]

#symbol
#regularMarketPrice
#shareOutstanding - 발행 주식수
#trailingPE 12개월 가격 / 주당순이익
#averageDailyVolume10Day": 233119800,
#"averageDailyVolume3Month": 170533131,
#dividendsPerShare dividends Per Share 뜻 : 주당배당금
#dividendRate 배당
# bid : 매수가
# ask  : 매도가
# bid size 매수량
# ask size  매도량
# floatShares 유동주식수
# epsForward 12개월선행 EPS로 현시점에서 향후 12개월동안의 주당순이익 추정
# shortPercentFloat 공매도 비율
#"dividendYield":0.59 배당수익
#"regularMarketChange":4.519989 시장 변화
#"regularMarketChangePercent":3.0417151 시장 변화 파센티지
#"regularMarketDayHigh":153.49
#"regularMarketDayRange":"148.61 - 153.49"
#"regularMarketDayLow":148.61
#"regularMarketVolume":90956723

import pandas as pd
import json
--


symbols = pd.read_csv("symbol_names.csv")["symbol"].tolist()

import requests
from flask import request as flaskRequest

quote_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

quote_querystring = {"region":"US","symbols": ",".join(symbols) }

quote_headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
    }

response = requests.request("GET", quote_url, headers=quote_headers, params=quote_querystring)

data = json.loads(response.text)
resultlen = len(data["quoteResponse"]["result"])


data["quoteResponse"]["result"][0]["regularMarketVolume"]

gc_realtime_stock_config = {
    "symbol" : "SYMBOL",
    "regularMarketPrice" : "MARKET_PRICE",
    "sharesOutstanding" : "SHARE_OUTSTANDING",
    "averageDailyVolume10Day" : "AVG_DAILY_VOLUME10DAY",
    "averageDailyVolume3Month" : "AVG_DAILY_VOLUME3MONTH",
    "dividendsPerShare" : "DIVIDENDS_PER_SHARE",
    "bid" : "BID",
    "ask" : "ASK",
    "bidSize" : "BID_SIZE",
    "askSize" : "ASK_SIZE",
    "floatShares" : "FLOATING_SHARES",
    "shortRatio" : "SHORT_RATIO",
    "epsForward" : "EPS_FORWARD",
    "bookValue" : "BOOK_VALUE",
    "sharesShort" : "SHARES_SHORT",
    "dividendYield" : "DIVIDENDS_YIELD",
    "regularMarketChange" : "MARKET_CHANGE",
    "regularMarketChangePercent" : "MARKET_CHANGE_PERCENT",
    "regularMarketDayHigh" : "MARKET_DAY_HIGH",
    "regularMarketDayLow" : "MARKET_DAT_LOW",
    "regularMarketVolume" : "MARKET_VOLUME"
}

gc_realtime_stock_keys =  list(gc_realtime_stock_config.keys())
current_data = data["quoteResponse"]["result"][0]

current_dict = {key: current_data[key] for key in gc_realtime_stock_keys if key in current_data.keys()}
insertingDict = {}
for key in current_dict.keys():
    insertingDict[gc_realtime_stock_config[key]] = current_dict[key]

columns = ",".join(list(insertingDict.keys()))
values = str(tuple(insertingDict.values()))
inserting_sql = "INSERT INTO GC_REALTIME_STOCK({}) VALUES{}".format(columns , values)


from sqlalchemy.engine import create_engine
import cx_Oracle
import os
connectString = os.getenv('db_connect')
con = cx_Oracle.connect(connectString)




DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'hmchung2' #enter your username
PASSWORD = '1234' #enter your password
HOST = '192.168.127.111' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
SERVICE = 'cdb1' # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
engine = create_engine(ENGINE_PATH_WIN_AUTH)

with engine.connect() as conn:
    result = conn.execute(inserting_sql)
    conn.commit()




conn = engine.connect()

engine.execute(inserting_sql)


inserting_sql

#test query
import pandas as pd
test_df = pd.read_sql_query('SELECT * FROM global_name', engine)


current_dict







print(response.text)

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.text
data = json.loads(data)
for i in data.keys():
    print(i)

data["defaultKeyStatistics"]







170533131
233119800
168404235
data["finance"]["result"][0]

print(response.text)
