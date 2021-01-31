'''
导出各个位点的频率以及高发位点——
    你可以引用的库：
        getMutationDatafile():对所有mutation文件整理输出，耗时较短所以同时进行

'''
print("正在调用getLocRig")

import csv
import json
import numpy as np

from bin.mainAddress import File_StaDatafile as dataFile
from bin.mainAddress import sta_countries as countries
from bin.mainAddress import File_Mutation_MainDataFile
from bin.mainAddress import File_Mutation_RegionSamplesCount
from bin.mainAddress import File_Mutation_LocusDataFile
from bin.mainAddress import File_Mutation_HighRateLocus

#读取json文件 存储国家到大洲关系到字典里
country2continent = {}
with open(countries,'r') as load_f:
	load_list = json.load(load_f)
	for i  in load_list:
		i =dict(i)
		country2continent[i['countryName']] = i['continentName']
#补充不存在json里的国家和大洲关系到字典里
country2continent["Palestine"] = 'Asia'
country2continent["United States"] = 'North America'
country2continent["CotedIvoire"] = 'Africa'
country2continent["Crimea"] = 'Europe'
country2continent["ISRAEL"] = 'Asia' 
country2continent["North Macedonia"] = 'Europe'
country2continent["South korea"] = 'Asia'
country2continent["Viet Nam"] = 'Asia'


#读取csv计算频率
variant_count = {} #存储每个位点在各个大洲的序列数到字典里
region_count = {} #存储每个大洲的序列数到字典里
with open(dataFile) as f:
	f_csv = csv.reader(f)
	for line in f_csv:
		if line:
			country = line[2].split('/')[0].strip()
			if country != '-':
				if country not in country2continent:
					raise
				else:
					continent = country2continent[country]
					if continent not in region_count:
						region_count[continent] = 0
					region_count[continent] += 1
					for variant in line[3:]:
						if variant not in variant_count:
							variant_count[variant] = {'Africa':0,'Asia':0,'Europe':0,'North America':0,'Oceania':0,'South America':0}
						variant_count[variant][continent] += 1

locus_var_list = []
for i in range(30000):
	locus_var_list.append({'Africa':0,'Asia':0,'Europe':0,'North America':0,'Oceania':0,'South America':0})

for i in list(variant_count.keys()):
	locus = i.split('|')
	locus = int(locus[1])
	for j in list(variant_count[i].keys()):
		locus_var_list[locus][j] += variant_count[i][j]

def getMutationDatafile():

	#输出 存储的每个大洲的序列数的字典
	rc = open(File_Mutation_RegionSamplesCount,'w')
	rc.write(str(region_count))
	rc.close()

	#输出 每个位点上的变异频率 按照位点顺序
	lc = open(File_Mutation_LocusDataFile,'w')
	hc = open(File_Mutation_HighRateLocus,'w')

	highratecount = {'Africa':[],'Asia':[],'Europe':[],'North America':[],'Oceania':[],'South America':[],'Total':[]}
	for i in range(30000):
		lc.write(str(i) + ',' +  str(int(locus_var_list[i]['Africa'])/region_count['Africa']) + ',' +  str(int(locus_var_list[i]['Asia'])/region_count['Asia']) +  ',' +  str(int(locus_var_list[i]['Europe'])/region_count['Europe']) + ',' + str(int(locus_var_list[i]['North America'])/region_count['North America']) + ',' +  str(int(locus_var_list[i]['Oceania'])/region_count['Oceania']) + ',' + str(int(locus_var_list[i]['South America'])/region_count['South America']) + '\n')
	
		entire = [0,0]
		for j in list(locus_var_list[i].keys()):
			if int(locus_var_list[i][j]) / region_count[j] >= 0.01:
				highratecount[j].append(i)
			entire[0] += locus_var_list[i][j]
			entire[1] += region_count[j]
		if entire[0] / entire[1] >= 0.01:
			highratecount['Total'].append(i)

	for i in list(highratecount.keys()):
		hc.write(i + ',' + str(highratecount[i])[1:-1] +'\n')


	hc.close()
	lc.close()

	#输出 每个位点在各个大洲的序列数/每个大洲的序列数,即频率 #不存在南极洲的样本
	vc = open(File_Mutation_MainDataFile,'w')
	vc.write("variant,frequency_of_Africa,frequency_of_Asia,frequency_of_Europe,tfrequency_of_North_America,frequency_of_Oceania,frequency_of_South_America\n")
	for variant in variant_count:
		vc.write('%s,%s,%s,%s,%s,%s,%s\n' % (variant,str(variant_count[variant]['Africa']/region_count['Africa']),str(variant_count[variant]['Asia']/region_count['Asia']),str(variant_count[variant]['Europe']/region_count['Europe']),str(variant_count[variant]['North America']/region_count['North America']),str(variant_count[variant]['Oceania']/region_count['Oceania']),str(variant_count[variant]['South America']/region_count['South America'])))
	vc.close()

if __name__ == "__main__":
	getMutationDatafile()
