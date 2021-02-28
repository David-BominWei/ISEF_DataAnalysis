'''
画图，生成各个高发位点的时间频率变化图——
    你可以引用的库：
        getOutPutFigureData(continent):导出所有高爆发频率位点的图片以及

'''
print("正在调用outputTimeLocFigure")

import os
import csv
import numpy as np
import numpy
import matplotlib.pyplot as plt
from tqdm import tqdm

from bin.mainAddress import FigFolder_Mutation_HighRateMutationFig
from bin.mainAddress import Folder_Mutation_RigionClassified as rigionFilePath
from bin.mainAddress import File_Mutation_HighRateLocus
from bin.mainTimedate import getTime1
from bin.mainTimedate import Lastday

continent = "Europe"



locus_time_count = {}
total_variant_count = np.zeros(Lastday)
with open(File_Mutation_HighRateLocus) as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        if i[0] == continent:
            for j in i[1:]:
                if j[1:] == '':
                    continue
                locus_time_count[int(j[1:])] = np.zeros(Lastday)

with open(rigionFilePath + continent + ".csv") as f:
    fcsv = csv.reader(f)
    for line in tqdm(fcsv):
        time = line[1]
        time = getTime1(time)
        if time <= 0:
            continue

        for i in range(time,Lastday):
            total_variant_count[i] += 1

        for i in line[3:]:
            if len(i) >= 3:
                i = int(i.split('|')[1])
            else:
                continue
            if locus_time_count.__contains__(int(i)):
                for j in range(time,Lastday):
                    locus_time_count[int(i)][j] += 1

if os.path.exists(FigFolder_Mutation_HighRateMutationFig + continent) is False:
    os.mkdir(FigFolder_Mutation_HighRateMutationFig + continent)

with open(FigFolder_Mutation_HighRateMutationFig + continent + '/' + "total.csv",'w') as dc:
    totalwriter  = csv.writer(dc)
    totalwriter.writerow(total_variant_count)

plt.plot(total_variant_count)
plt.savefig(FigFolder_Mutation_HighRateMutationFig + continent + '/totalcount.jpg')
plt.cla()

fc = open(FigFolder_Mutation_HighRateMutationFig + continent + '/' + "data.csv",'w')
writer  = csv.writer(fc)

for i in list(locus_time_count.keys()):
    path = FigFolder_Mutation_HighRateMutationFig + continent + '/' + str(i) + '.jpg'
    rate_ = []
    n_ = 0
    for j in locus_time_count[i]:
        if total_variant_count[n_] != 0:
            rate_.append(j/total_variant_count[n_])
        else:
            rate_.append(np.nan)
        n_ += 1

    if np.nanmax(rate_) >= 0.1:
        writer.writerow([i] + rate_)
        plt.plot(rate_)
        plt.savefig(path)
        plt.cla()
