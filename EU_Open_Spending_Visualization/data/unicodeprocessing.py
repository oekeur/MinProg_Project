import csv
import json
import unicodedata
data = []
countries = []
institutions = []


# if unicodedata.normalize('NFKD', row[3].strip()).encode('ascii', 'ignore') not in countries and '/' not in row[3]:
# 		countries.append(unicodedata.normalize('NFKD', row[3].strip()).encode('ascii', 'ignore'))
# 	if unicodedata.normalize('NFKD', row[6].strip()).encode('ascii', 'ignore') not in institutions:
# 		institutions.append(unicodedata.normalize('NFKD', row[6].strip()).encode('ascii', 'ignore'))


########################################################################################

# datafile = open("EC_2007.csv", "r")
# csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# for row in data:
# 	if type(row[3]) == str:
# 		if row[3].strip() not in countries and '/' not in row[3]:
# 						countries.append(row[3].strip())
# 	else:
# 		if unicodedata.normalize('NFKD', row[3].strip()).encode('ascii', 'ignore') not in countries and '/' not in row[3]:
# 			countries.append(unicodedata.normalize('NFKD', row[3].strip()).encode('ascii', 'ignore'))
# 	if type(row[6]) == str:
# 		if row[6].strip() not in institutions:
# 			institutions.append(row[6].strip())
# 	else:
# 		if unicodedata.normalize('NFKD', row[6].strip()).encode('ascii', 'ignore') not in institutions:
# 			institutions.append(unicodedata.normalize('NFKD', row[6].strip()).encode('ascii', 'ignore'))

# institutions.sort()
# countries.sort()
# outputdata = dict.fromkeys(countries, 0)

# for row in data:
# 	if type(row[3]) == str:
# 		if outputdata.has_key(row[3].strip()):
# 			outputdata[row[3].strip()] += float(row[4])
# 	else:
# 		if outputdata.has_key(unicodedata.normalize('NFKD', row[3].strip()).encode('ascii', 'ignore')):
# 			outputdata[unicodedata.normalize('NFKD', row[3].strip()).encode('ascii', 'ignore')] += float(row[4])

print unicodedata.normalize('NFKD', 'R\xe9union').encode('ascii', 'ignore')

# with open('EC_2007_countrytotal.json', 'wb') as jsonfile:
# 	json.dump(outputdata, jsonfile)

# with open('EC_2007_institutions.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=',')
# 	for row in outputdata:
# 		writer.writerow(row)

# datafile.close()
# # csvfile.close()
# data = []
########################################################################################

# datafile = open("EC_2008.csv", "r")
# csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# for row in data:
# 		if row[3].strip() not in countries and '/' not in row[3]:
# 			countries.append(row[3].strip())
# 		if row[6].strip() not in institutions:
# 			institutions.append(row[6].strip())


# institutions.sort()
# countries.sort()
# outputdata = dict.fromkeys(countries, 0)

# for row in data:
# 	if outputdata.has_key(row[3].strip()):
# 		outputdata[row[3].strip()] += float(row[4])

# print outputdata

# # with open('EC_2007_countrytotal.json', 'wb') as jsonfile:
# # 	json.dump(outputdata, jsonfile)

# with open('EC_2008_institutions.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=',')
# 	for row in outputdata:
# 		writer.writerow(row)

# datafile.close()
# csvfile.close()
# data = []