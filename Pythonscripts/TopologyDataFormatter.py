import pandas as pd
import numpy as np
import CalculationFunctions
import sys
import math
import matplotlib.pyplot

print("this file works right now")

#get topological data API
#save the topological data in some format 
#normalize the data and turn it into a data frame or an array of arrays
#later implement some sort of algorithm that will find the most compatible array with
#the StockData that is normalized
#ideas for this
# least squared simmilarities algorithm- the data points are compared and the difference squared
#the sum of these differnce squared should be minimized, if there are 2 with the same score, choose the one with the lower index
#use a neural network that trains off mountain z_score normalized data then goes on and tries the same thing with the stock z_score
#normalized data
