import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
import numpy as np
from CalculationFunctions import normalize_array

#some error in this file!!!!!
#with dayshistoryc = "4d" and interval = "60m" the array is 22 long

daysHistoryc ="25d"
intervalc = "1d"
def stock_data_normal(stockName, daysHistory = daysHistoryc):#normalizes the stock data
   
    stock = yf.Ticker(stockName)
    historyDf = stock.history(period=daysHistory, interval = intervalc)
    priceHistory = historyDf.get("Open")#change thisssss open to somethings better
    normalizedArray = normalize_array(priceHistory)
    return normalizedArray
    
def stock_data(stockName, daysHistory =daysHistoryc):#stock data choices should be more dynamic 
    
    stock = yf.Ticker(stockName)
    historyDf = stock.history(period=daysHistory, interval = intervalc)
    priceHistory = historyDf.get("Open")
    return priceHistory





    
















































