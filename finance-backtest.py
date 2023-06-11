import yfinance as yf
import pandas as pd
from flask import Flask, request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/', methods=['GET'])
def health_check():
    return 'Finance Python flask application running successfully!'

@app.route('/finance/details', methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def finance_details():
    return derive_finance_details(request.args.get('ticker'), request.args.get('period'), request.args.get('interval'))

def derive_finance_details(ticker, period, interval):
    stk = yf.Ticker(ticker) #HDFCBANK.NS
    hist = stk.history(period=period,  interval=interval) # "2y" and # "1d"
    df = pd.DataFrame()
    print(hist.to_string())
    return hist.to_string()

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

# df['ds'] = hist.index
# df['Open'] = hist['Open'].values
# df['High'] = hist['High'].values
# df['Low'] = hist['Low'].values
# df['Close'] = hist['Close'].values
# df['Volume'] = hist['Volume'].values

# print(df)