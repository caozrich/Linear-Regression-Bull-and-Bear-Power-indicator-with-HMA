def f_exp_lr(_height, _length): #?--------------------
    
    _ret = _height + (_height/_length)
    return _ret


def highestbars(data, lb=25):
    df = data.copy()
    df['Aroon Up'] =  100*df.Close.rolling(lb + 1).apply(lambda x: x.argmax()) / lb
    df['Aroon Down'] = 100*df.Close.rolling(lb + 1).apply(lambda x: x.argmin()) / lb
    return df['Aroon Up'], df['Aroon Down'] 