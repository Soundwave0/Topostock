from TopologyDataFormatter import topology_data_normal
from StockDataFormatter import stock_data_normal, stock_data
from CalculationFunctions import calculate_ls_score,z_score_to_value, mean_array, std_array
import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np

if __name__ == '__main__':
    print("started running at: "+str(time.time()))
    stockName = input("stockNormal name: ")
   
    minscore:int = 100
    count:int = 0
    goodDataCount:int = 0
    satisfactorydatapoints:int = 10
    scoreThreshold:int =12
    predictionArray = np.array([])
    goodDataList = np.array([])
    stock = stock_data(stockName=stockName)
    stockNormal= stock_data_normal(stockName=stockName)
    mean  = mean_array(stock)
    std = std_array(stock)
    print(mean)
    print(std)

    while(satisfactorydatapoints> goodDataCount):
       topo = topology_data_normal()
       curscore =  calculate_ls_score(stockData=stockNormal,topoData=topo)
       if curscore < minscore: minscore = curscore
       if curscore < scoreThreshold:
         predictionArray=np.append(predictionArray,topo[-(len(topo)-len(stockNormal)):])
         goodDataList = np.append(goodDataList, topo)
         goodDataCount+=1
       count+=1
    predictionZscoreMean = predictionArray.mean()
    predictionVal = z_score_to_value(mean = mean, std= std, z_score=predictionArray.mean())   
    print(f"prediction is around {predictionVal} ")
    print(f"last point of stockNormal was: {z_score_to_value(mean=mean,std=std,z_score=stockNormal[-1])}")
    print(f"data went through {count} sets")
    print(f"this is the prediction z_score average {predictionZscoreMean}")
    print(len(topo)-len(stock))
    print(minscore)
   

   #  plt.plot(stockNormal)
   #  plt.show()
   #  plt.plot(topo)
   #  plt.show()
   #  plt.plot(stockNormal)
   #  plt.plot(topo[:len(stockNormal)])
   #  plt.show()



