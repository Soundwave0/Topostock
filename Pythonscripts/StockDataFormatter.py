import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
import numpy as np
from CalculationFunctions import z_score, normalize_array

#Gets stock information from api
#gets period
#creates dataframe
#filters datafame for open CHANGE THIS make it a mean of the day and more frequent than the day
#Normalizes the data by plotting the z_score

userInput = input("what would you like to you check for: ")
monthsHistory = input("how many months: ")
mh = monthsHistory+"d"
stock = yf.Ticker(userInput)
historyDf = stock.history(period=mh, interval = "60m")
priceHistory = historyDf.get("Open")
normalizedArray = normalize_array(priceHistory)
plt.plot(normalizedArray)
plt.show()



    
















































