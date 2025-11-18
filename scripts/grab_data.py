# data_collection.py
import yfinance as yf
import pandas as pd

# 1. Get data from yfinance
# 2. Iterate through each symbol in the list of tickers
# 3. Extract the adjusted closing value and date column
# 4. Merge with the data in the csv if file if not already there

def fetch_data(symbol, start_date, end_date):
    data = yf.download(symbol, start = start_date, end= end_date, auto_adjust= False)
    return data

def collect_adjclose(portfolio_symbols, start_date, end_date):
    result = pd.DataFrame()
    # Iterate through portfolio symbols and fetch data
    for symbol in portfolio_symbols:
        asset_data = yf.download(symbol, start= start_date, end= end_date, auto_adjust= False)

        adj_close = asset_data[["Adj Close"]]

        if result.empty:
            result = adj_close
        else:
            result = result.join(adj_close, how="outer")
    return result
