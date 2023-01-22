import math
import talib 

def HMA(df,sl): #hull moving average
     
    period = 6
    sl["bbp"] =  df
    sl['WMA']= talib.WMA(sl["bbp"],period // 2)
    sl['WMA2']= talib.WMA(sl["bbp"],period)

    sl['SBBP'] = talib.WMA(2 *sl['WMA'] - sl['WMA2'], int(math.sqrt(period))) 
    
    return sl['SBBP']