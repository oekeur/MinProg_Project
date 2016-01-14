import csv
import json
import unicodedata
data = []
countries = []
institutions = []


# # ########################################################################################

datafile = open("EC_2007.csv", "r")
csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)

for row in data:
	if row[3].strip() not in countries and '/' not in row[3]:
		countries.append(row[3].strip())
	if row[6].strip() not in institutions:
		institutions.append(row[6].strip())


institutions.sort()
countries.sort()
outputdata = dict.fromkeys(countries, 0)

for row in data:
	if outputdata.has_key(row[3].strip()):
		outputdata[row[3].strip()] += float(row[4])

print outputdata

with open('EC_2007_countrytotal.json', 'wb') as jsonfile:
	json.dump(outputdata, jsonfile)

# with open('EC_2007_countrytotal.csv', 'wb') as csvfile:
# 	writer = csv.DictWriter(csvfile, outputdata.keys(), delimiter=',')
# 	writer.writeheader()
# 	writer.writerow(outputdata)

datafile.close()
csvfile.close()
data = []
# #######################################################################################
# datafile = open("EC_2008.csv", "r")
# csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# for row in data:
# 	if row[3].strip() not in countries and '/' not in row[3]:
# 		countries.append(row[3].strip())
# 	if row[6].strip() not in institutions:
# 		institutions.append(row[6].strip())


# institutions.sort()
# countries.sort()
# outputdata = dict.fromkeys(countries, 0)

# for row in data:
# 	if outputdata.has_key(row[3].strip()):
# 		outputdata[row[3].strip()] += float(row[4])

# # print outputdata

# # with open('EC_2008_countrytotal.json', 'wb') as jsonfile:
# # 	json.dump(outputdata, jsonfile)

# with open('EC_2008_countrytotal.csv', 'wb') as csvfile:
# 	writer = csv.DictWriter(csvfile, outputdata.keys(), delimiter=',')
# 	writer.writeheader()
# 	writer.writerow(outputdata)

# datafile.close()
# csvfile.close()
# data = []
# ########################################################################################
# datafile = open("EC_2009.csv", "r")
# csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# for row in data:
# 	if row[3].strip() not in countries and '/' not in row[3]:
# 		countries.append(row[3].strip())
# 	if row[6].strip() not in institutions:
# 		institutions.append(row[6].strip())


# institutions.sort()
# countries.sort()
# outputdata = dict.fromkeys(countries, 0)

# for row in data:
# 	if outputdata.has_key(row[3].strip()):
# 		try:
# 			outputdata[row[3].strip()] += float(row[5])
# 		except:
# 			outputdata[row[3].strip()] += 0

# # print outputdata

# # with open('EC_2009_countrytotal.json', 'wb') as jsonfile:
# # 	json.dump(outputdata, jsonfile)

# with open('EC_2009_countrytotal.csv', 'wb') as csvfile:
# 	writer = csv.DictWriter(csvfile, outputdata.keys(), delimiter=',')
# 	writer.writeheader()
# 	writer.writerow(outputdata)

# datafile.close()
# csvfile.close()
# data = []
# ########################################################################################
# datafile = open("EC_2010.csv", "r")
# csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# for row in data:
# 	if row[3].strip() not in countries and '/' not in row[3]:
# 		countries.append(row[3].strip())
# 	if row[6].strip() not in institutions:
# 		institutions.append(row[6].strip())


# institutions.sort()
# countries.sort()
# outputdata = dict.fromkeys(countries, 0)

# for row in data:
# 	if outputdata.has_key(row[3].strip()):
# 		outputdata[row[3].strip()] += float(row[4])

# # print outputdata

# # with open('EC_2010_countrytotal.json', 'wb') as jsonfile:
# # 	json.dump(outputdata, jsonfile)

# with open('EC_2010_countrytotal.csv', 'wb') as csvfile:
# 	writer = csv.DictWriter(csvfile, outputdata.keys(), delimiter=',')
# 	writer.writeheader()
# 	writer.writerow(outputdata)

# datafile.close()
# csvfile.close()
# data = []
# ########################################################################################
# datafile = open("EC_2011.csv", "r")
# csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# for row in data:
# 	if row[3].strip() not in countries and '/' not in row[3]:
# 		countries.append(row[3].strip())
# 	if row[6].strip() not in institutions:
# 		institutions.append(row[6].strip())


# institutions.sort()
# countries.sort()
# outputdata = dict.fromkeys(countries, 0)

# for row in data:
# 	if outputdata.has_key(row[3].strip()):
# 		outputdata[row[3].strip()] += float(row[4])

# # print outputdata

# # with open('EC_2011_countrytotal.json', 'wb') as jsonfile:
# # 	json.dump(outputdata, jsonfile)

# with open('EC_2011_countrytotal.csv', 'wb') as csvfile:
# 	writer = csv.DictWriter(csvfile, outputdata.keys(), delimiter=',')
# 	writer.writeheader()
# 	writer.writerow(outputdata)

# datafile.close()
# csvfile.close()
# data = []
# ########################################################################################
# datafile = open("EC_2012.csv", "r")
# csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# for row in data:
# 	if row[3].strip() not in countries and '/' not in row[3]:
# 		countries.append(row[3].strip())
# 	if row[6].strip() not in institutions:
# 		institutions.append(row[6].strip())


# institutions.sort()
# countries.sort()
# outputdata = dict.fromkeys(countries, 0)

# for row in data:
# 	if outputdata.has_key(row[3].strip()):
# 		outputdata[row[3].strip()] += float(row[4])

# # print outputdata

# # with open('EC_2012_countrytotal.json', 'wb') as jsonfile:
# # 	json.dump(outputdata, jsonfile)

# with open('EC_2012_countrytotal.csv', 'wb') as csvfile:
# 	writer = csv.DictWriter(csvfile, outputdata.keys(), delimiter=',')
# 	writer.writeheader()
# 	writer.writerow(outputdata)

# datafile.close()
# csvfile.close()
# data = []
# ########################################################################################
# datafile = open("EC_2013.csv", "r")
# csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# for row in data:
# 	if row[3].strip() not in countries and '/' not in row[3]:
# 		countries.append(row[3].strip())
# 	if row[6].strip() not in institutions:
# 		institutions.append(row[6].strip())


# institutions.sort()
# countries.sort()
# outputdata = dict.fromkeys(countries, 0)

# for row in data:
# 	if outputdata.has_key(row[3].strip()):
# 		outputdata[row[3].strip()] += float(row[4])

# # print outputdata

# # with open('EC_2013_countrytotal.json', 'wb') as jsonfile:
# # 	json.dump(outputdata, jsonfile)

# with open('EC_2013_countrytotal.csv', 'wb') as csvfile:
# 	writer = csv.DictWriter(csvfile, outputdata.keys(), delimiter=',')
# 	writer.writeheader()
# 	writer.writerow(outputdata)

# datafile.close()
# csvfile.close()
# data = []
# ########################################################################################
