import numpy as np
import pycristoforo as pyc
import random

countriesList = ['AUT', 'BEL', 'BGR', 'CYP', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GRC', 'HRV', 'HUN', 'IRL', 'ITA',
              'LTU', 'LUX', 'LVA', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'SWE','CHE','BRA','CAN','NPL','PAK']


#This program includes the function that do calculations
def z_score(mean,std,value):#calculates the z score of certain value, to normalize the data
    return ((value - mean)/(std))

def z_score_to_value(mean,std,z_score):#converts the z score to a value
    return mean + (std * z_score)

def mean_array(array:list)->float:#returns the mean of a list
    npArray = np.array(array)
    mean = np.mean(npArray)
    return mean
def std_array(array:list)->float:#return the standard deviation of the array values
    npArray = np.array(array)
    sd = np.std(npArray)
    return sd
def normalize_array(array:list)->list:#normalizes each data point to a z_score and then returns the whole function as an array
    npArray = np.array(array)
    sd = np.std(npArray)
    mean = np.mean(npArray)
    normalizedArray = []
#   print(npArray)
    for dataentry in npArray:#
        z = z_score(mean=mean,std=sd,value=dataentry)
        normalizedArray.append(z)
    return normalizedArray
def calculate_ls_score(stockData,topoData)->float:#it checks how well one fits to the other   # fix this algorithm, actually just develop a nice algo
    score = 0
    #for topoarray in topoData:
    for index, value in enumerate(stockData):
        dif = topoData[index]-value
        score+=(dif**2)
    return score

def generate_random_coords(numofpoints):#generates coordinates
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



