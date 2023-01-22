#Linear-Regression-Bull-and-Bear-Power-indicator
from helpfunctions import f_exp_lr,highestbars
from Hull_moving_average import HMA
from  matplotlib  import pyplot as plt
from sklearn import preprocessing
import pandas as pd
import numpy as np
import talib


def makeBBP (slice,period):
    
    realdata = slice.copy()
    high = realdata["Close"].astype(float)
    output = talib.MAX(high.to_numpy(),timeperiod = period)
    realdata["Highmax"]=pd.Series(output)
    low = realdata["Close"].astype(float)
    output = talib.MIN(low.to_numpy(),timeperiod = period)
    realdata["Lowmax"]=pd.Series(output)
    realdata['Aroon Up'], realdata['Aroon Down']  = highestbars(realdata, lb=period)
    minmax_scale = preprocessing.MinMaxScaler(feature_range=(-9, 0.1))
    x_scale = minmax_scale.fit_transform(realdata["Aroon Up"].values.reshape(-1,1))
    realdata["Aroon Up"] = x_scale
    realdata = realdata.replace(np.nan, 0)

    minmax_scale = preprocessing.MinMaxScaler(feature_range=(-9, 0.1))
    x_scale = minmax_scale.fit_transform(realdata["Aroon Down"].values.reshape(-1,1))
    realdata["Aroon Down"] = x_scale
    realdata = realdata.replace(np.nan, 0)

    bear = 0-(f_exp_lr(realdata["Highmax"]-realdata["Close"], realdata["Aroon Up"]))
    bull = 0+(f_exp_lr(realdata["Close"]-realdata["Lowmax"], realdata["Aroon Down"]))

    realdata = (bull*2 + bear*2)
    realdata.replace([np.inf, -np.inf], np.nan, inplace=True)
    bbp = HMA(realdata,slice)
    
    return bbp,slice


def plot (bbp,slice):

    plt.figure(figsize=(24,18))
    green =  np.where(bbp.shift(-1, axis = 0) > bbp, bbp,np.nan)
    red =  np.where(bbp.shift(-1, axis = 0) < bbp, bbp,np.nan)
    ax1 = plt.subplot2grid((9,1), (1,0), rowspan=4, colspan=1)
    plt.title('BTC Price Chart (12-01-2022 - 24-01-2022)')
    plt.xlabel('Date')
    ax1.set_facecolor((0.09, 0.11, 0.18))
    ax1.grid(color=(0.55, 0.58, 0.68), alpha=0.15 )
    ax1.plot(slice["Close"],color='white',linewidth=1)
    
    ax2 = plt.subplot2grid((9,1), (5,0), rowspan=2, colspan=1 , sharex = ax1)
    ax2.plot(bbp, color='orange')  
    ax2.plot(green, color='green')  
    ax2.plot(red, color='red')  
    plt.show()
    
    
    
    
df =  pd.read_csv("dataframe.csv")  
print(df)  
df,sl = makeBBP(df,10) #(df,period)
plot(df,sl)    