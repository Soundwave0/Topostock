
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

#possible uses and functions 
#https://github.com/opengeo-tech/GeoPicker
#https://github.com/cbrum11/elevate/wiki

import requests as r
import pandas as pd
import json
import CalculationFunctions as CF
import numpy as np
import matplotlib.pyplot as plt



latPre = []
longPre = []

#for i in np.arange(30,32,0.25):
#    for j in np.arange(81,82,0.25):
i=30
j=81
for k in np.arange(0,0.25,0.01):
    latPre.append(i)
    longPre.append(j+k)


lat = ",".join(map(str,latPre))
long = ",".join(map(str,longPre))
            
elevation_API = "https://api.open-meteo.com/v1/elevation?latitude={latitude}&longitude={longitude}"
elevationRequest = elevation_API.format(latitude=lat,longitude=long)
print(elevationRequest)
response = r.get(elevationRequest)
#print(response)
elevationDict = json.loads(response.text)
elevationArray = elevationDict['elevation']
print(elevationArray)
elevationArray = CF.normalize_array(elevationArray)
plt.plot(elevationArray)
plt.show()




#open file, then write these elevations






