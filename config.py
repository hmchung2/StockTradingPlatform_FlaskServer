DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'hmchung2' #enter your username
PASSWORD = '1234' #enter your password
HOST = '192.168.127.111' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
SERVICE = 'cdb1' # enter the oracle db service name


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
    "regularMarketDayLow" : "MARKET_DAY_LOW",
    "regularMarketVolume" : "MARKET_VOLUME"
}

gc_summary_stock_config= {
    "defaultKeyStatistics" : {"enterpriseToRevenue": "enterpriseToRevenue",
                              "enterpriseToEbitda" : "enterpriseToEbitda",
                              "52WeekChange" : "WeekChange52",
                              "forwardEps" : "forwardEps",
                              "sharesOutstanding" : "sharesOutstanding",
                              "bookValue" : "bookValue",
                              "sharesShort" : "sharesShort",
                              "lastFiscalYearEnd" : "lastFiscalYearEnd",
                              "heldPercentInstitutions" : "heldPercentInstitutions",
                              "netIncomeToCommon" : "netIncomeToCommon",
                              "trailingEps" : "trailingEps",
                              "SandP52WeekChange" : "SandP52WeekChange",
                              "shortRatio" : "shortRatio",
                              "sharesShortPreviousMonthDate" : "sharesShortPreviousMonthDate",
                              "floatShares" : "floatShares",
                              "earningsQuarterlyGrowth" : "earningsQuarterlyGrowth",
                              "forwardPE" : "forwardPE",
                              "sharesShortPriorMonth" : "sharesShortPriorMonth"
                              },
   "price" : {"averageDailyVolume3Month" : "averageDailyVolume3Month",
            "exchange" : "exchange",  #string
            "regularMarketChangePercent" : "regularMarketChangePercent",
            "regularMarketVolume" : "regularMarketVolume",
            "symbol" : "symbol"
              },
  "netSharePurchaseActivity" : {"netPercentInsiderShares" : "netPercentInsiderShares",
                                "netInfoShares": "netInfoShares",
                                "buyInfoShares" : "buyInfoShares",
                                "sellInfoShares" : "sellInfoShares"},
    "financialData" : {"ebitdaMargins" : "ebitdaMargins",
                       "profitMargins" : "profitMargins",
                       "grossMargins" : "grossMargins",
                       "operatingCashflow" : "operatingCashflow" ,
                       "revenueGrowth" :  "revenueGrowth" ,
                       "operatingMargins" : "operatingMargins",
                       "ebitda" : "ebitda",
                       "grossProfits" : "grossProfits",
                       "freeCashflow" : "freeCashflow",
                       "currentPrice" : "currentPrice",
                       "earningsGrowth" : "earningsGrowth",
                       "totalCash" : "totalCash",
                       "totalDebt" : "totalDebt",
                       "totalRevenue" : "totalRevenue"},
    "summaryDetail" : {"regularMarketPreviousClose" : "regularMarketPreviousClose",
                      "regularMarketOpen" : "regularMarketOpen",
                      "twoHundredDayAverage" : "twoHundredDayAverage",
                      "trailingAnnualDividendYield" : "trailingAnnualDividendYield",
                      "payoutRatio" : "payoutRatio",
                      "fiftyDayAverage" : "fiftyDayAverage",
                      "averageVolume10days" : "averageVolume10days",
                      "askSize" : "askSize",
                      "bidSize" : "bidSize"}
}
