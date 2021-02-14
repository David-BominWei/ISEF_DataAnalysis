'''
预测模型1a——
    你可以引用的库：
        

'''
print("正在调用：dataARIMAModel1a")

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

def ARIMA(data_,predict_start,predict_end):
    p_min = 0
    d_min = 1
    q_min = 0
    p_max = 4
    d_max = 2
    q_max = 4

    resent_best_result = sm.tsa.SARIMAX(data_, order=(20, 1, 5)).fit()
    #resent_best_bic = resent_best_result.bic
    resent_best_MSE = mean_squared_error(df[predict_start:predict_end],resent_best_result.predict(predict_start, predict_end, dynamic=True, typ='levels'))
    bestpdq = [20,1,5]
    for p,d,q in itertools.product(range(p_min,p_max+1),
                                   range(d_min,d_max+1),
                                   range(q_min,q_max+1)):
        
        model = sm.tsa.SARIMAX(data_, order=(p, d, q))
        results = model.fit()
        #resent_bic = results.bic
        resent_predict = results.predict(predict_start, predict_end, dynamic=True, typ='levels')
        resent_MSE = mean_squared_error(df[predict_start:predict_end],resent_predict)

        if resent_MSE < resent_best_MSE:
            arima_predict_ori = resent_best_result.predict(predict_start, predict_end, dynamic=True, typ='levels')
            #resent_best_bic = resent_bic
            resent_best_result = results
            resent_best_MSE = resent_MSE
            bestpdq = [p,d,q]

            arima_predict_imp = resent_best_result.predict(predict_start, predict_end, dynamic=True, typ='levels')

            '''
            plt.plot(arima_predict_imp, color = 'red')
            plt.plot(arima_predict_ori, color = 'blue')
            plt.plot(df, color = 'black')
            plt.savefig('temp/'+ str(locdata[0]) + ",," + str(resent_best_MSE) + '.png')
            plt.cla()
            '''

            


    arima_predict = resent_best_result.predict(predict_start, predict_end, dynamic=True, typ='levels')

    return arima_predict, bestpdq

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

paralist = []
for locdata in tqdm(data):
    try:
        #数据导入时间序列
        df = pd.Series(locdata[1:], index = timer)
        df = df.dropna(axis=0, how='any')
        prediction,para = ARIMA(df[1:],'2020-11-1','2021-2-11')
        paralist.append([int(locdata[0])] + para)

        #print(prediction)
        plt.plot(prediction, color = 'red')
        plt.plot(df, color = 'black')
        plt.savefig(outputaddress + continent +'/' + str(int(locdata[0]))+'.png')
        plt.cla()
    except:
        paralist.append(str(int(locdata[0])) + 'ERROR')


with open(outputaddress+ continent + "/parameter.csv",'w+') as f:
    for i in paralist:
        if len(i) >= 3:
            f.write(str(int(i[0])) + ',' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + '\n')
        else:
            f.write(str(int(i[0])) + ',' + str(i[1]) + '\n')
    