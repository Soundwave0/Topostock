import requests as r
import pandas as pd
import json
from CalculationFunctions import z_score, normalize_array, calculate_ls_score,generate_random_coords
import numpy as np


def topology_data_normal(longDistance = 0.5, longIncrement = 0.015, numberoftrials =1)->list:
    latPre = []
    longPre = []
    
    for trials in range(numberoftrials):
        coords = generate_random_coords(1)
        lat0 = round(coords[0][0],4)
        lo0 = round(coords[0][1],4)
        for k in np.arange(0,longDistance,longIncrement):
            latPre.append(lat0)
            longPre.append(lo0+k)

    lat = ",".join(map(str,latPre))
    long = ",".join(map(str,longPre))
                
    elevation_API = "https://api.open-meteo.com/v1/elevation?latitude={latitude}&longitude={longitude}"
    elevationRequest = elevation_API.format(latitude=lat,longitude=long)
    response = r.get(elevationRequest)
    elevationDict = json.loads(response.text)
    elevationArray = elevationDict['elevation']
    elevationArrayNorm = normalize_array(elevationArray)
    return elevationArrayNorm
def topology_data_raw(longDistance = 0.5, longIncrement = 0.015, numberoftrials =1)->list:
    latPre = []
    longPre = []
    
    for trials in range(numberoftrials):
        coords = generate_random_coords(1)
        lat0 = round(coords[0][0],4)
        lo0 = round(coords[0][1],4)
        for k in np.arange(0,longDistance,longIncrement):
            latPre.append(lat0)
            longPre.append(lo0+k)

    lat = ",".join(map(str,latPre))
    long = ",".join(map(str,longPre))
                
    elevation_API = "https://api.open-meteo.com/v1/elevation?latitude={latitude}&longitude={longitude}"
    elevationRequest = elevation_API.format(latitude=lat,longitude=long)
    response = r.get(elevationRequest)
    elevationDict = json.loads(response.text)
    elevationArray = elevationDict['elevation']
  
    return elevationArray
