import numpy as np

def z_score(mean,std,value):
    return ((value - mean)/(std))

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