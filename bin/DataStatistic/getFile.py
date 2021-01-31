'''
下载序列文件以及整理导出csv——
    你可以引用的库：
        getDownload() : 下载文件
        downloadUntar() : 解压文件
        getFormat() : 整理文件

'''
print("正在调用getFile")

import urllib.request as ub
import csv
from tqdm import tqdm
import tarfile
import pandas as pd

from bin.mainAddress import file_statisticMain as downloadPathmain
from bin.mainAddress import file_metaData as downloadPathmeta
from bin.mainAddress import temp_RAWMetaDatafile
from bin.mainAddress import temp_RAWMainDatafile
from bin.mainAddress import temp_MainDatafile
from bin.mainAddress import temp_Maincsv
from bin.mainAddress import temp

def downloadDownload():
    ub.urlretrieve(downloadPathmain , temp_RAWMainDatafile)
    print("main下载完成，地址" + temp_RAWMainDatafile)

    ub.urlretrieve(downloadPathmeta , temp_RAWMetaDatafile)
    print("meta下载完成，地址" + temp_RAWMetaDatafile)
    

def downloadUntar():
    file = tarfile.open(temp_RAWMainDatafile)
    file.extractall(path = temp)
    print("解压完成，地址" + temp_MainDatafile)

def getDownload():
    downloadDownload()
    downloadUntar()

def getFormat():
    
    with open(temp_MainDatafile,'r') as f:
        #跳过不必要行
        for i in range(4):
            f.readline()

        #第一列病毒名获取
        virName = f.readline()
        virName = virName.split('\t')
        virName = virName[10:]
        virList = []
        for i in virName:
            virList.append([i])
        
        print("正在写入数据，消耗时间较长")
        for data in tqdm(f):
            data = data.split('\t')
            ID_ = data[1]
            REF_ = data[3]
            ALT_ = data[4]
            ALT_ = ALT_.split(',')

            num = 0
            for i in data[10:]:
                if i != "0":
                    if i != ".":
                        try:
                            virList[num].append(REF_ + "|" + ID_ + "|" + ALT_[int(i)-1])
                        except:
                            pass
                num += 1

    with open(temp_Maincsv , 'w' , newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(virList)

                

if __name__ == "__main__":
    downloadDownload()
