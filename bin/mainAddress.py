''' 
    常引用——
    主要调用地址——

'''
print("常mainAddress")

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
File_Mutation_MainDataFile = "Files/dataFile/mutationdataFile/mutationMainDataFile.csv"
File_Mutation_RegionSamplesCount = "Files/dataFile/mutationdataFile/samplesCount.dict"
File_Mutation_LocusDataFile = "Files/dataFile/mutationdataFile/mutationLocusDataFile.csv"
File_Mutation_HighRateLocus = "Files/dataFile/mutationdataFile/mutationHighRateLocus.csv"
Folder_Mutation_RigionClassified = "Files/dataFile/regiondataFile/"
Folder_Mutation_RigionHighRate = "Files/dataFile/regiondataFile/highRate/"

#stafile address
sta_countries = "Files/staFile/countries.json"

#fig output address
FigFolder_Mutation_HighRateMutationFig = "Files/stafigureOutPut/"
FigFolder_Mutation_PredictionARIMA1 = "Files/prefigureOutPut_1a/"
