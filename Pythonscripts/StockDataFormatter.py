import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
import numpy as np
import math
from CalculationFunctions import z_score
import sys

#Gets stock information from api
#gets period
#creates dataframe
#filters datafame for open CHANGE THIS make it a mean of the day and more frequent than the day
#Normalizes the data by plotting the z_score

userInput = input("what would you like to you check for: ")
monthsHistory = input("how many months: ")
mh = monthsHistory+"mo"
stock = yf.Ticker(userInput)
historyDf = stock.history(period=mh)
priceHistory = historyDf.get("Open")

priceHistoryArray = priceHistory.to_numpy()
sd = np.std(priceHistoryArray)
mean = np.mean(priceHistoryArray)
normalizedArray = []
#print(priceHistoryArray)
for dataentry in priceHistoryArray:
    z = z_score(mean=mean,std=sd,value=dataentry)
    normalizedArray.append(z)
#print(normalizedArray)
plt.plot(normalizedArray)
plt.show()



    















































