'''
对导出的csv进行整理——
    你可以引用的库：
        getReformatMainDatafile():对csv整理输出老师要求的巨大格式文件，耗时较长

'''
print("正在调用getReformatFile")

import csv
import numpy as np
from tqdm import tqdm
import pandas as pd

from bin.mainAddress import temp_Maincsv
from bin.mainAddress import temp_RAWMetaDatafile
from bin.mainAddress import File_MainDataFile
from bin.mainAddress import File_StaDatafile

f = csv.reader(open(temp_Maincsv,'r'))

def getReformatMainDatafile():
    virList = []
    print("正在整理输出序列，消耗时间较长")
    for seq in tqdm(f):
        seqList = []
        seqList.append(seq[0])
        for i in range(29903):
            seqList.append("-")
        for i in seq[1:]:
            i = i.split('|')
            if i[2] in ["A","T","C","G"]:
                if i[0] in ["A","T","C","G"]:
                    seqList[int(i[1])] = str(i[0] + "->" + i[2])
        virList.append(seqList)

    with open(File_MainDataFile , 'w') as outputfile:
        csv_writer = csv.writer(outputfile)
        
        csv_writer.writerow(["sequence"] + list(range(1,29903)))
        csv_writer.writerows(virList)

def getReformatStaDatafile():
     #创建可以用于对照所有序列和地区信息的list
    MataList1 = []
    MataList2 = []
    print("正在读取list，消耗时间较长")
    MataData = pd.read_excel(temp_RAWMetaDatafile, index_col=0)
    for i in MataData.index.values:
        MataList1.append(i)

    for i in MataData.values:
        MataList2.append(i)

    print("正在写入文件，消耗时间较长")
    with open(File_StaDatafile , 'w') as outputfile:
        csv_writer = csv.writer(outputfile)
        loss = 0
        for seq in tqdm(f):
            seqList = [seq[0]]
            try:
                seqMata = list(MataList2[MataList1.index(seq[0])][9:11])
            except:
                seqMata = ['-', '-']
                loss += 1
            seqList = seqList + seqMata + seq[1:]
            try:
                csv_writer.writerow(seqList)
            except:
                pass

if __name__ == "__main__":
   getReformatStaDatafile()