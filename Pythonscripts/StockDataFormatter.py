import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
import numpy as np
from CalculationFunctions import normalize_array

def stock_data_normal(stockName, daysHistory = 4)->list:
    mh = str(daysHistory)+"d"
    stock = yf.Ticker(stockName)
    historyDf = stock.history(period=mh, interval = "60m")
    priceHistory = historyDf.get("Open")#change thisssss open to somethings better
    normalizedArray = normalize_array(priceHistory)
    return normalizedArray
    
def stock_data(stockName, daysHistory =4)->list:
    mh = str(daysHistory)+"d"
    stock = yf.Ticker(stockName)
    historyDf = stock.history(period=mh, interval = "60m")
    priceHistory = historyDf.get("Open")
    return priceHistory





    
















































