import csv
import json
import unicodedata
countries = []
institutions = []

# for each year the same prcedure is applied
# from the list of data construct a list of institutions and a list of countries
# from these two lists, build two separate dictionaries
# for each row in the data check to which country and which institution this amount belongs
# add this amount to the associated country / institution
# (a try/except is used because row[4] cannot always be converted to a number because of missing values for example )
# save this data


########################################################################################

data =[]
datafile = open("cleaned/EC_2007.csv", "r")
csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)
datafile.close()

for row in data:
	if row[3].strip() not in countries and '/' not in row[3]:
		countries.append(row[3].strip())
	if row[6].strip() not in institutions:
		institutions.append(row[6].strip())

institutions.sort()
countries.sort()
countrydata = dict.fromkeys(countries, 0)
institutiondata = dict.fromkeys(institutions, 0)

for row in data:
	if countrydata.has_key(row[3].strip()):
		countrydata[row[3].strip()] += float(row[4])
	if institutiondata.has_key(row[6].strip()):
		try:
			institutiondata[row[6].strip()] += float(row[4])
		except:
			pass


with open('processed/EC_2007_countrytotal.json', 'wb') as jsonfile:
	json.dump(countrydata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()
with open('processed/EC_2007_institutiontotal.json', 'wb') as jsonfile:
	json.dump(institutiondata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()

countries = []
institutions = []
del countrydata
del institutiondata
#####################################################################################
data =[]# 
datafile = open("cleaned/EC_2008.csv", "r")
csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)
datafile.close()

for row in data:
	if row[3].strip() not in countries and '/' not in row[3]:
		countries.append(row[3].strip())
	if row[6].strip() not in institutions:
		institutions.append(row[6].strip())

institutions.sort()
countries.sort()
countrydata = dict.fromkeys(countries, 0)
institutiondata = dict.fromkeys(institutions, 0)

for row in data:
	if countrydata.has_key(row[3].strip()):
		countrydata[row[3].strip()] += float(row[4])
	if institutiondata.has_key(row[6].strip()):
		try:
			institutiondata[row[6].strip()] += float(row[4])
		except:
			pass

with open('processed/EC_2008_countrytotal.json', 'wb') as jsonfile:
	json.dump(countrydata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()
with open('processed/EC_2008_institutiontotal.json', 'wb') as jsonfile:
	json.dump(institutiondata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()

countries = []
institutions = []
del countrydata
del institutiondata
#####################################################################################
data =[]
datafile = open("cleaned/EC_2009.csv", "r")
csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)
datafile.close()

for row in data:
	if row[3].strip() not in countries and '/' not in row[3]:
		countries.append(row[3].strip())
	if row[7].strip() not in institutions:
		institutions.append(row[7].strip())

institutions.sort()
countries.sort()
countrydata = dict.fromkeys(countries, 0)
institutiondata = dict.fromkeys(institutions, 0)

for row in data:
	if countrydata.has_key(row[3].strip()):
		countrydata[row[3].strip()] += float(row[5])
	if institutiondata.has_key(row[7].strip()):
		if row[5] != "missing" and  row[5] != "Amount":
			institutiondata[row[7].strip()] += float(row[5])

print json.dumps(countrydata, indent=4, encoding="latin-1")
with open('processed/EC_2009_countrytotal.json', 'wb') as jsonfile:
	json.dump(countrydata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()
with open('processed/EC_2009_institutiontotal.json', 'wb') as jsonfile:
	json.dump(institutiondata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()

countries = []
institutions = []
del countrydata
del institutiondata
#####################################################################################
data =[]
datafile = open("cleaned/EC_2010.csv", "r")
csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)
datafile.close()

for row in data:
	if row[3].strip() not in countries and '/' not in row[3]:
		countries.append(row[3].strip())
	if row[6].strip() not in institutions:
		institutions.append(row[6].strip())

institutions.sort()
countries.sort()
countrydata = dict.fromkeys(countries, 0)
institutiondata = dict.fromkeys(institutions, 0)

for row in data:
	if countrydata.has_key(row[3].strip()):
		countrydata[row[3].strip()] += float(row[4])
	if institutiondata.has_key(row[6].strip()):
		if row[4] != "missing" and  row[4] != "Total amount":
			institutiondata[row[6].strip()] += float(row[4])

with open('processed/EC_2010_countrytotal.json', 'wb') as jsonfile:
	json.dump(countrydata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()
with open('processed/EC_2010_institutiontotal.json', 'wb') as jsonfile:
	json.dump(institutiondata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()

countries = []
institutions = []
del countrydata
del institutiondata
#######################################################################################
data =[]
datafile = open("cleaned/EC_2011.csv", "r")
csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)
datafile.close()

for row in data:
	if row[3].strip() not in countries and '/' not in row[3]:
		countries.append(row[3].strip())
	if row[6].strip() not in institutions:
		institutions.append(row[6].strip())

institutions.sort()
countries.sort()
countrydata = dict.fromkeys(countries, 0)
institutiondata = dict.fromkeys(institutions, 0)

for row in data:
	if countrydata.has_key(row[3].strip()):
		countrydata[row[3].strip()] += float(row[4])
	if institutiondata.has_key(row[6].strip()):
		if row[4] != "missing":
			try:
				institutiondata[row[6].strip()] += float(row[4])
			except:
				pass

with open('processed/EC_2011_countrytotal.json', 'wb') as jsonfile:
	json.dump(countrydata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()
with open('processed/EC_2011_institutiontotal.json', 'wb') as jsonfile:
	json.dump(institutiondata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()

countries = []
institutions = []
del countrydata
del institutiondata
#######################################################################################
data =[]
datafile = open("cleaned/EC_2012.csv", "r")
csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)
datafile.close()

for row in data:
	if row[3].strip() not in countries and '/' not in row[3]:
		countries.append(row[3].strip())
	if row[6].strip() not in institutions:
		institutions.append(row[6].strip())

institutions.sort()
countries.sort()
countrydata = dict.fromkeys(countries, 0)
institutiondata = dict.fromkeys(institutions, 0)

for row in data:
	if countrydata.has_key(row[3].strip()):
		if row[4] != "missing":
			countrydata[row[3].strip()] += float(row[4])
	if institutiondata.has_key(row[6].strip()):
		if row[4] != "missing":
			try:
				institutiondata[row[6].strip()] += float(row[4])
			except:
				pass

with open('processed/EC_2012_countrytotal.json', 'wb') as jsonfile:
	json.dump(countrydata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()
with open('processed/EC_2012_institutiontotal.json', 'wb') as jsonfile:
	json.dump(institutiondata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()

countries = []
institutions = []
del countrydata
del institutiondata
#######################################################################################
data =[]
datafile = open("cleaned/EC_2013.csv", "r")
csvdata = csv.reader(datafile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)
datafile.close()

for row in data:
	if row[3].strip() not in countries and '/' not in row[3]:
		countries.append(row[3].strip())
	if row[6].strip() not in institutions:
		institutions.append(row[6].strip())

institutions.sort()

countries.sort()
countrydata = dict.fromkeys(countries, 0)
institutiondata = dict.fromkeys(institutions, 0)

for row in data:
	if countrydata.has_key(row[3].strip()):
		countrydata[row[3].strip()] += float(row[4])
	if institutiondata.has_key(row[6].strip()):
		try:
			institutiondata[row[6].strip()] += float(row[4])
		except:
			pass

with open('processed/EC_2013_countrytotal.json', 'wb') as jsonfile:
	json.dump(countrydata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()
with open('processed/EC_2013_institutiontotal.json', 'wb') as jsonfile:
	json.dump(institutiondata, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()

countries = []
institutions = []
del countrydata
del institutiondata
#######################################################################################