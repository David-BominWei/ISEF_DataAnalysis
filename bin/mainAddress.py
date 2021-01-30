''' 
    常引用——
    主要调用地址——

'''
print("正在调用mainAddress")

import os

#constant web address
file_statisticMain = "ftp://download.big.ac.cn/GVM/Coronavirus/vcf/2019-nCoV_total.tar.gz"
file_metaData = "https://bigd.big.ac.cn:443/ncov/genome/export/meta"

#tempfile address
temp = "temp"
temp_RAWMainDatafile = "temp/main.tar.gz"
temp_RAWMetaDatafile = "temp/meta.xlsx"
temp_MetaDatafile = "temp/meta.csv"
temp_MainDatafile = "temp/2019-nCoV_total.vcf"
temp_Maincsv = "temp/main.csv"

#datafile address
File_MainDataFile = "Files/dataFile/MainDataFile.csv"
File_StaDatafile = "Files/dataFile/StaDatafile.csv"