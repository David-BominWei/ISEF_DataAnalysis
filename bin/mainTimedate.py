'''
转换每条序列的时间信息成指定的格式——
    为了方便拟合，默认19年12月1号为第0天
    你可以引用的库：
        getTime1(date): 标准获取时间，这是第几天
    你可以引用的变量：
        pdtimer: pandas时间戳

'''
print("常调用: mainTimedate")

import numpy as np
import time
import pandas as pd
from datetime import datetime

d0 = datetime.strptime('2019-12-1', '%Y-%m-%d')
#dn = datetime.now()
dn = datetime.strptime('2021-2-13', '%Y-%m-%d')

Lastday = (dn-d0).days

def getTime1(date):
    try:
        dd = datetime.strptime(date, '%Y-%m-%d')
    except:
        return -1
    return (dd-d0).days

#pandas时间戳
pdtimer = pd.date_range('2019-12-01', periods = Lastday, freq = 'D')


if __name__ == "__main__":
    print(getTime1("2021-1-8"))
    print(Lastday)