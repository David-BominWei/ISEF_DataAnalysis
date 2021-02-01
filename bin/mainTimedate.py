'''
转换每条序列的时间信息成指定的格式——
    为了方便拟合，默认19年12月1号为第0天
    你可以引用的库：
        

'''
print("常调用: mainTimedate")

import numpy as np
import time
from datetime import datetime

d0 = datetime.strptime('2019-12-1', '%Y-%m-%d')
dn = datetime.strptime('2021-2-1', '%Y-%m-%d')

Lastday = (dn-d0).days

def getTime1(date):
    try:
        dd = datetime.strptime(date, '%Y-%m-%d')
    except:
        return -1
    return (dd-d0).days

if __name__ == "__main__":
    print(getTime1("2020/1/2"))