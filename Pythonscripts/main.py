from TopologyDataFormatter import topology_data_normal
from StockDataFormatter import stock_data_normal, stock_data,intervalc,daysHistoryc
from CalculationFunctions import calculate_ls_score,z_score_to_value, mean_array, std_array
import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np
import sys


if __name__ == '__main__':
    done = False
    firstframe = True
    print("started running at: "+str(time.time()))#prints time it starts running
    
    stockName = input("stockNormal name: ")#prompts user for stock name
    scoreThreshold = 20-int(input("please enter strenght of correlation 1(low) - 15(extremely high): "))
    
    minscore:int = 100#sets min score to 100
    count:int = 0 
    goodDataCount:int = 0
    satisfactorydatapoints:int = 10
    #scoreThreshold:int =12#in production should be around 12 for good results
    predictionArray = np.array([])
    goodDataList = np.array([])
    stock = stock_data(stockName=stockName)
    stockNormal= stock_data_normal(stockName=stockName)
    mean  = mean_array(stock)
    std = std_array(stock)
    print(mean)
    print(std)
    # while(done==False):
    #   for i in range(3):
    #     time.sleep(.5)
    #     sys.stdout.write('.')
    #     sys.stdout.write('\b \b \b')

    while(satisfactorydatapoints> goodDataCount):
       topo = topology_data_normal()
       curscore =  calculate_ls_score(stockData=stockNormal,topoData=topo)
       if curscore < minscore: 
         minscore = curscore
         print("score was not satisfactory")
       if curscore < scoreThreshold:
         predictionArray=np.append(predictionArray,topo[-(len(topo)-len(stockNormal)):])
         goodDataList = np.append(goodDataList, topo)
         goodDataCount+=1
         print(f"good fit mined! #{goodDataCount}")
         '''if firstframe:#print first frame to check viability
           print(goodDataList)
           firstframe=False'''
       count+=1
    predictionZscoreMean = predictionArray.mean()
    predictionVal = z_score_to_value(mean = mean, std= std, z_score=predictionZscoreMean)   
    done = True
    print(f"prediction is around {predictionVal} ")
    print(f"last point of stockNormal was: {z_score_to_value(mean=mean,std=std,z_score=stockNormal[-1])}")
    #print('Loading')
    print(f"data went through {count} sets")
    print(f"this is  the prediction z_score average {predictionZscoreMean}")
    toptostockdif = len(topo)-len(stock)
    print(f"time interval was {intervalc}")
    print(f"the total experiment day was {daysHistoryc}")
    print(f"difference in # of elements in topo vs stock is {toptostockdif}")
    print(f"lowest minsquare fit is {minscore}")
   

    plt.plot(stockNormal)
    plt.show()
    plt.plot(topo)
    plt.show()
    plt.plot(stockNormal)
    plt.plot(topo[:len(stockNormal)])
    plt.show()



