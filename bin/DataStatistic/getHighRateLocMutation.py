
'''
导出高变异频率位点是什么变到什么——
    你可以引用的库：

'''
print("正在调用：getHighRateLocMutation")

import csv
from tqdm import tqdm

from bin.mainAddress import Folder_Mutation_RigionClassified as mutation_Dat
from bin.mainAddress import File_Mutation_HighRateLocus as important_Loc1
from bin.mainAddress import FigFolder_Mutation_HighRateMutationFig as important_Loc2
from bin.mainAddress import Folder_Mutation_RigionHighRate as out_put

continent = "Europe"

#读取高频率位点1：
def _getHighRate1():
    highRate_ = {}
    with open(important_Loc1,'r') as f:
        fcsv = csv.reader(f)
        for i in fcsv:
            if i[0] == continent:
                for j in i[1:]:
                    highRate_[int(j)] = {}

                return highRate_

    raise "NotFound"

#读取高频率位点2：
def _getHighRate2():
    highRate_ = {}
    with open(important_Loc2 + continent + "/data.csv",'r') as f:
        fcsv = csv.reader(f)
        for i in fcsv:
            if i != []:
                highRate_[int(i[0])] = {}
        return highRate_

HighRateMutation = _getHighRate2()

with open(mutation_Dat + continent + ".csv", 'r') as f:
    fcsv = csv.reader(f)
    for i in tqdm(fcsv):
        for j in i[3:]:
            if('|' not in j):
                continue
            if j != "":
                j = j.split('|')
                mloc = int(j[1])
                mfrom = j[0]
                mto = j[2]
                if HighRateMutation.__contains__(mloc):
                    if mfrom in ['A','T','C','G']:
                        if mto in ['A','T','C','G']:
                            if HighRateMutation[mloc].__contains__((mfrom,mto)):
                                HighRateMutation[mloc][(mfrom,mto)] += 1
                            else:
                                HighRateMutation[mloc][(mfrom,mto)] = 1

#写入
with open(out_put + continent + '.csv', 'w') as f:
    f.write("loc,from,to,mutcount" + '\n')
    for loc_ in HighRateMutation.keys():
        for mut_ in HighRateMutation[loc_].keys():
            count_ = HighRateMutation[loc_][mut_]
            f.write(str(loc_) + ',' + mut_[0] + ',' + mut_[1] + ',' + str(count_) + '\n')

