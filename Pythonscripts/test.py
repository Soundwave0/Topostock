
import TopologyDataFormatter as TDF
import StockDataFormatter as SDF
stocktotest = 'AAPL'
def testtopology():
   
    TDFArray = TDF.topology_data_normal()
    assert TDFArray!= None
    print(TDFArray)
    print("the program has completed")
    print(len(TDFArray))
def teststockcalls():
    SDFArray = SDF.stock_data_normal(stockName=stocktotest)
    assert SDF!=None
    print(SDFArray)
    print("the program has completed")

def teststockdata():
    SDFArray = SDF.stock_data(stockName=stocktotest)
    assert SDF!=None
    print(SDFArray)
    print("the program has completed")
    print(len(SDFArray))



#testtopology()
teststockdata()#
#testtopology()#34




