import numpy as np
import pycristoforo as pyc
import random

countriesList = ['AUT', 'BEL', 'BGR', 'CYP', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GRC', 'HRV', 'HUN', 'IRL', 'ITA',
              'LTU', 'LUX', 'LVA', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'SWE','CHE','BRA','CAN','NPL','PAK']



def z_score(mean,std,value):
    return ((value - mean)/(std))

def z_score_to_value(mean,std,z_score):
    return mean + (std * z_score)

def mean_array(array:list)->float:
    npArray = np.array(array)
    mean = np.mean(npArray)
    return mean
def std_array(array:list)->float:
    npArray = np.array(array)
    sd = np.std(npArray)
    return sd
def normalize_array(array:list)->list:
    npArray = np.array(array)
    sd = np.std(npArray)
    mean = np.mean(npArray)
    normalizedArray = []
#   print(npArray)
    for dataentry in npArray:
        z = z_score(mean=mean,std=sd,value=dataentry)
        normalizedArray.append(z)
    return normalizedArray
def calculate_ls_score(stockData,topoData)->float:   # fix this algorithm, actually just develop a nice algo 
    score = 0
    #for topoarray in topoData:
    for index, value in enumerate(stockData):
        dif = topoData[index]-value
        score+=(dif**2)
    return score

def generate_random_coords(numofpoints):
    coordslist= []
    for i in range(numofpoints):
        countryName = random.choice(countriesList)
        countryShape = pyc.get_shape(countryName)
        pointsSample = pyc.geoloc_generation(countryShape, 1, countryName)
        cur = pointsSample[0]
        coord = cur['geometry']['coordinates']
        coord=[coord[1],coord[0]]
        coordslist.append(coord)
    return coordslist



