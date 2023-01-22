# Improved Linear Regression Bull and Bear Power (BBP) in Python

BBP is a tradingview indicator created by Nico.Muselle in pinescript, this indicator is quite good for scalping and I have taken the trouble to adapt the code to python

## Description

BBP is based on the Bull and Bear Power indicator, therefore it's a good indicator to detect microtrends in the asset's price, it can be a good complement to a scalping strategy in short timeframes.

## libraries required - Python 3.6 or later

- sklearn.
- talib.
- pandas.
- numpy.

## How to Use 

```python
# import the package
from Linear_regresion_BBP import makeBBP #this function returns a pandas series with the indicator values and the raw dataset

df =  pd.read_csv("dataframe.csv")  
bbp,sl = makeBBP(df,10) #(df,period) 
print(bbp)
```

## Sample Figure

![Sin título-1](https://user-images.githubusercontent.com/34092193/213946275-ebacfa69-9020-44cf-9afe-0fdf67b9dff9.png)
