import time

import numpy as np
import pandas as pd
import yfinance as yf

pd.set_option('display.max_rows', None)
#also display all columns
pd.set_option('display.max_columns', None)

data = yf.Ticker("BIMAS.IS")
#obttain EUR USD exchange rate

PERIOD= "10Y"

usdtry = yf.Ticker("USDTRY=X")
usdtry = usdtry.history(period=PERIOD)
# Get the historical data for the last day
hist = data.history(period=PERIOD)
#denominate in USD

hist = hist[hist['Close'] > 0]
hist = hist.iloc[1:]
hist.index = hist.index.date
usdtry.index = usdtry.index.date
usdtry_close_aligned = usdtry['Close'].reindex(hist.index)
hist['Close'] = hist['Close'] / usdtry_close_aligned
hist['Dividends'] = hist['Dividends'] / usdtry_close_aligned






hist['Shares'] = (hist['Dividends']/hist['Close'].shift(-1) +1).cumprod()
hist['Shares'].fillna(method='ffill', inplace=True)

print(hist[['Close', 'Dividends','Shares']])

price_return=hist['Close'][-1]/hist['Close'][0]
dividend_return=hist['Shares'][-1]
total_return=price_return*dividend_return

years=(hist.index[-1]-hist.index[0]).days/365

annualized_price_return=price_return**(1/years)
annualized_dividend_return=dividend_return**(1/years)
annualized_total_return=annualized_price_return*annualized_dividend_return


print("\n\n")
print("Total Price return: ", price_return)
print("Total Dividend return: ", dividend_return)
print("Total return: ", total_return)
print("\n\n")
print("Annualized Price return: %",annualized_price_return*100-100)
print("Annualized Dividend return: % ", annualized_dividend_return*100-100)
print("Annualized Total return: %", annualized_total_return*100-100)

