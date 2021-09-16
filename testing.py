from flask import Flask,jsonify,render_template, Response


from flask import request as flaskRequest
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import pandas as pd
import time
from config import *
from sqlalchemy.engine import create_engine
import requests
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



executors = {
    'default': ThreadPoolExecutor(16),
    'processpool': ProcessPoolExecutor(4)
}

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
engine = create_engine(ENGINE_PATH_WIN_AUTH)
conn = engine.connect()


def getSymbols():
    data = conn.execute("select symbol from gc_stock")
    results = data.fetchall()
    results = list(map(lambda x: x[0] , results))
    return results

symbols = getSymbols();



@app.route("/startInsertStocks")
def startInsertStock():
    try:
        if insertStock.state == 1:
            return {"result" : "success" , "state" : "alreadyStartedProcessing"}
        elif insertStock.state == 0:
            insertStock.start()
            return {"result" : "success" , "state" : "startedProcessing"}
        elif insertStock.state == 2:
            insertStock.resume()
            return {"result" : "success" , "state" : "resumedProcessing"}
        else:
            return {"result" : "fail" , "state" : "unknownState"}
    except Exception as e:
        return {"result" : "fail" , "state" : str(e)}

@app.route("/pauseInsertStocks")
def pauseInsertStock():
    try:
        if insertStock.state == 1:
            insertStock.pause()
            return {"result" : "success" , "state" : "pausedProcessing"}
        elif insertStock.state == 0:
            return {"result" : "success" , "state" : "notStartedProcessing"}
        elif insertStock.state == 2:
            return {"result" : "fail" , "state" : "alreadyPausedProcessing"}
        else:
            return {"result" : "fail" , "state" : "unknownState"}
    except Exception as e:
        return {"result" : "fail" , "state" : str(e)}


@app.route("/startInsertSummaryStocks")
def startInsertSummaryStock():
    try:
        if insertSummary.state == 1:
            return {"result" : "success" , "state" : "alreadyStartedProcessing"}
        elif insertSummary.state == 0:
            insertSummary.start()
            return {"result" : "success" , "state" : "startedProcessing"}
        elif insertSummary.state == 2:
            insertSummary.resume()
            return {"result" : "success" , "state" : "resumedProcessing"}
        else:
            return {"result" : "fail" , "state" : "unknownState"}
    except Exception as e:
        return {"result" : "fail" , "state" : str(e)}


@app.route("/pauseInsertSummaryStocks")
def pauseInsertSummaryStock():
    try:
        if insertSummary.state == 1:
            insertSummary.pause()
            return {"result" : "success" , "state" : "pausedProcessing"}
        elif insertSummary.state == 0:
            return {"result" : "success" , "state" : "notStartedProcessing"}
        elif insertSummary.state == 2:
            return {"result" : "fail" , "state" : "alreadyPausedProcessing"}
        else:
            return {"result" : "fail" , "state" : "unknownState"}
    except Exception as e:
        return {"result" : "fail" , "state" : str(e)}


@app.route("/updateSymbols",methods=['GET'] )
def updateSymbols():
    try:
        print("hello")
        newSymbol = flaskRequest.args['symbol']
        print(newSymbol)
        newLongName = flaskRequest.args['longName']
        print(newLongName)
        df = pd.read_csv("symbol_names.csv")
        print("reading")
        df = df.append(pd.DataFrame({"symbol" : newSymbol, "longName" : newLongName}   , index = [df.index.values.max() + 1] ) )
        print("apprending")
        df.to_csv("symbol_names.csv" , index = False)
        print("writing")
        global symbols
        symbols = pd.read_csv("symbol_names.csv")["symbol"].tolist()
        print("updating")
        return {"result":"success"}
    except Exception as e:
        return {"result" : "fail" , "state" : str(e)}

#@cross_origin()
@app.route("/getSymbols")
def getSymbols():
    return jsonify({"symbols" : symbols})


@app.route("/trySymbol" ,methods=['GET'])
def trySymbo():
    try:
        newSymbol = flaskRequest.args['symbol']
        quote_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
        quote_querystring = {"region":"US","symbols": newSymbol }
        quote_headers = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
        }
        response = requests.request("GET", quote_url, headers=quote_headers, params=quote_querystring)
        result = response.text
        return {"result" : "success" , "state" : result}
    except Exception as e:
        return {"result" : "fail" , "state" : str(e)}


@app.route("/deleteSymbol")
def deleteSymbol():
    try:
        print("delete start")
        deleteSymbol = flaskRequest.args['symbol']
        print(deleteSymbol)
        df = pd.read_csv("symbol_names.csv")
        if deleteSymbol in df.symbol.values.tolist():
            df = df.loc[df["symbol"] != deleteSymbol ]
            df.to_csv("symbol_names.csv" , index= False)
            global symbols
            symbols = pd.read_csv("symbol_names.csv")["symbol"].tolist()
            return {"result" : "success" , "state" : "deleted"}
        else:
            return {"result" : "success" , "state" : "notExisting" }
    except exception as e:
        return {"result" : "fail" , "state" : str(e)}







def insertStockInfo():
    for i in range(len(symbols)):
        print(symbols[i])
        try:
            symbol = symbols[i]
            url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

            querystring = {"symbol":symbol ,"region":"US"}

            headers = {
                'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
                'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            if "longName" in data["price"]:
                longName = data["price"]["longName"]
            else:
                longName = "NULL"

            if "sector" in data["summaryProfile"]:
                sector =  data["summaryProfile"]["sector"]
            else:
                sector = "NULL"

            symbol = data["price"]["symbol"]

            if "phone" in data["summaryProfile"]:
                phone =  data["summaryProfile"]["phone"]
            else:
                phone = "NULL"
            if "website" in data["summaryProfile"]:
                website = data["summaryProfile"]["website"]
            else:
                website = "NULL"

            conn.execute("INSERT INTO GC_STOCK( SYMBOL , LONG_NAME  ,  SECTOR , PHONE , WEBSITE) VALUES ( :1 , :2, :3, :4, :5)", (symbol , longName  , sector , phone , website) )
        except Exception as e:
            print("error : {}".format(e) )
            try:
                print(data["summaryProfile"][e])
            except:
                continue




def insertSummary():
    cunix_time = int(time.time())
    for symbol in symbols:
        print(symbol)
        try:
            keys = []
            keys.append("unix_time")
            values = (cunix_time,)
            print("insert summary")
            url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
            querystring = {"symbol":symbol ,"region":"US"}
            headers = {
                'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
                'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            for x in gc_summary_stock_config.keys():
                ckey = x
                for j in gc_summary_stock_config[ckey].keys():
                    column = j
                    db_col = gc_summary_stock_config[ckey][column]
                    if column in data[ckey]:

                        if data[ckey][column] == {}:
                            continue
                        elif "raw" in data[ckey][column]:
                            try:
                                ele = float(data[ckey][column]["raw"])
                                values =  values + (ele , )
                                keys.append(db_col)
                            except:
                                continue;
                        else:
                            keys.append(db_col)
                            ele = data[ckey][column]
                            values =  values + (ele , )
            db_cols = ",".join(keys)
            params =  ",".join([ "?" for x in range(len(keys))  ])
            conn.execute("INSERT INTO GC_SUMMARY_STOCK({}) VALUES{}".format(db_cols , values)  )
        except Exception as e:
            print(symbol  + " ---------------------")
            print(e )
            print(" ---------------------")


def gc_realtime_stock_insert():
        try:
            quote_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"
            quote_querystring = {"region":"US","symbols": ",".join(symbols) }
            quote_headers = {
                'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
                'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
                }
            response = requests.request("GET", quote_url, headers=quote_headers, params=quote_querystring)
            data = json.loads(response.text)
            resultlen = len(data["quoteResponse"]["result"])
            gc_realtime_stock_keys =  list(gc_realtime_stock_config.keys())
            for i in range(resultlen):
                current_data = data["quoteResponse"]["result"][i]
                current_dict = {key: current_data[key] for key in gc_realtime_stock_keys if key in current_data.keys()}
                insertingDict = {}
                for key in current_dict.keys():
                    insertingDict[gc_realtime_stock_config[key]] = current_dict[key]
                if insertingDict["BID"] == 0:
                    insertingDict["BID"] = insertingDict["MARKET_PRICE"]
                if insertingDict["ASK"] == 0:
                    insertingDict["ASK"] =  insertingDict["MARKET_PRICE"]
                columns = ",".join(list(insertingDict.keys()))
                columns = columns + ",UNIX_time"
                values = str(tuple(insertingDict.values()) +(int(time.time()),))
                inserting_sql = "INSERT INTO GC_REALTIME_STOCK({}) VALUES{}".format(columns , values)
                result = conn.execute(inserting_sql)
            print("realtime inserting done")
        except Exception as e:
            print("unknown error : " + str(e))







if __name__ == '__main__':
    insertStock = BackgroundScheduler(timezone='Asia/Seoul', executors=executors)
    insertStock.add_job(gc_realtime_stock_insert, 'interval', seconds=15)

    insertSummary = BackgroundScheduler(timezone='Asia/Seoul', executors=executors)
    insertSummary.add_job(gc_summary_stock_insert, 'interval', seconds=3600)


    app.run(host='0.0.0.0', port=8000, debug=True, use_reloader=False)
