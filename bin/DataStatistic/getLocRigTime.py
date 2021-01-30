import csv

#读取json文件 存储国家到大洲关系到字典里
country2continent = {}
import json
with open("countries.json",'r') as load_f:
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
with open('StaDatafile.csv') as f:
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

#输出存储的每个大洲的序列数的字典
rc = open('region_samples_count.txt','w')
rc.write(str(region_count))
rc.close()

#输出每个位点在各个大洲的序列数/每个大洲的序列数,即频率 #不存在南极洲的样本
vc = open('varint_frequency_of_continents.txt','w')
vc.write("variant\tfrequency_of_Africa\tfrequency_of_Asia\tfrequency_of_Europe\tfrequency_of_North_America\tfrequency_of_Oceania\tfrequency_of_South_America\n")
for variant in variant_count:
	vc.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (variant,str(variant_count[variant]['Africa']/region_count['Africa']),str(variant_count[variant]['Asia']/region_count['Asia']),str(variant_count[variant]['Europe']/region_count['Europe']),str(variant_count[variant]['North America']/region_count['North America']),str(variant_count[variant]['Oceania']/region_count['Oceania']),str(variant_count[variant]['South America']/region_count['South America'])))

vc.close()





