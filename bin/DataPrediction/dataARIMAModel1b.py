
'''
预测模型1b——
    你可以引用的库：
        

'''
print("正在调用：dataARIMAModel1b")

import itertools
import pandas as pd
import numpy as np
import csv
import matplotlib.pylab as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from tqdm import tqdm
import os
from sklearn.metrics import mean_squared_error, r2_score


from bin.mainAddress import Folder_Mutation_RigionClassified as rigionFilePath
from bin.mainAddress import File_Mutation_HighRateLocus
from bin.mainAddress import FigFolder_Mutation_HighRateMutationFig
from bin.mainAddress import FigFolder_Mutation_PredictionARIMA1 as outputaddress
from bin.mainTimedate import pdtimer as timer

#======================================ARIMA==================================================#

def ARIMA_get(data_,order_,predict_start,predict_end):
    recent_model = sm.tsa.SARIMAX(data_, order=order_)
    resent_result = recent_model.fit()
    resent_predict = resent_result.predict(predict_start, predict_end, dynamic=True, typ='levels')
    resent_MSE = mean_squared_error(data_[predict_start:predict_end],resent_predict)

    return resent_predict, resent_MSE

#=============================================================================================#


continent = "Asia"

#read data
with open(FigFolder_Mutation_HighRateMutationFig + continent + '/' + "data.csv",'r') as f:
    datafile = csv.reader(f)
    data = []
    for i in datafile:
        if len(i) >= 5:
            i = [ float(x_) for x_ in i ]
            data.append(i)

parameters = {}
with open(outputaddress+ continent + "/parameter.csv",'r') as f:
    datafile = csv.reader(f)
    for i in datafile:
        parameters[i[0]] = (int(i[1]),int(i[2]),int(i[3]))


fc = open(outputaddress+ continent + "/predictions.csv",'w')
fc.write("locus,MSE,predictions"+'\n')

for locdata in tqdm(data):

    #数据导入时间序列
    df = pd.Series(locdata[1:], index = timer)
    df = df.dropna(axis=0, how='any')

    prediction,mse_var = ARIMA_get(df[1:],parameters[str(int(locdata[0]))],'2020-11-1','2021-2-11')

    fc.write(str(locdata[0]) + ','+ str(mse_var)+ ',')
    for i in prediction.values:
       fc.write(str(i) + ',')

    fc.write('\n')



    