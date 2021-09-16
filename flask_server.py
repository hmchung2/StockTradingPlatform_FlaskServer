from flask import Flask
app = Flask(__name__)

import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

querystring = {"region":"US","symbols":"AAPL"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "886154e1cemsh2cd846fa2cb5bd4p100be8jsn6237c6c8a470"
    }



@app.route('/')
def hello_world():
    print("1")
    response = requests.request("GET", url, headers=headers, params=querystring)
    print("2")
    return response.text



# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port=8000)






# import time
# import atexit
#
# from apscheduler.schedulers.background import BackgroundScheduler
#
#
# def print_date_time():
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
#
#
# scheduler = BackgroundScheduler()
# scheduler.add_job(func=print_date_time, trigger="interval", seconds=1)
# scheduler.start()
# scheduler.state
# scheduler.shutdown()
# # Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())
