import json

with open('countrycode.json', 'r') as infile:
	conversion = json.load(infile)
infile.close()
with open('EC_2007_countrytotal.json', 'r') as infile:
	data2007 = json.load(infile)
infile.close()
with open('EC_2008_countrytotal.json', 'r') as infile:
	data2008 = json.load(infile)
infile.close()
with open('EC_2009_countrytotal.json', 'r') as infile:
	data2009 = json.load(infile)
infile.close()
with open('EC_2010_countrytotal.json', 'r') as infile:
	data2010 = json.load(infile)
infile.close()
with open('EC_2011_countrytotal.json', 'r') as infile:
	data2011 = json.load(infile)
infile.close()
with open('EC_2012_countrytotal.json', 'r') as infile:
	data2012 = json.load(infile)
infile.close()
with open('EC_2013_countrytotal.json', 'r') as infile:
	data2013 = json.load(infile)

dictkeys = {}

for item in conversion:
	dictkeys[item] = 0
 
output = dict.fromkeys(dictkeys, {"2007" : 0,"2008" : 0,"2009" : 0,"2010" : 0,"2011" : 0,"2012" : 0,"2013" : 0, "total" : 0})

i = 0
for country in conversion:
	if conversion[country] in data2007.keys():
		value2007 = data2007[conversion[country]]
	else:
		value2007 = 0
	if conversion[country] in data2008.keys():
		value2008 = data2008[conversion[country]]
	else:
		value2008 = 0
	if conversion[country] in data2009.keys():
		value2009 = data2009[conversion[country]]
	else:
		value2009 = 0
	if conversion[country] in data2010.keys():
		value2010 = data2010[conversion[country]]
	else:
		value2010 = 0
	if conversion[country] in data2011.keys():
		value2011 = data2011[conversion[country]]
	else:
		value2011 = 0
	if conversion[country] in data2012.keys():
		value2012 = data2012[conversion[country]]
	else:
		value2012 = 0
	if conversion[country] in data2013.keys():
		value2013 = data2013[conversion[country]]
	total = value2007 + value2008 + value2009 + value2010 + value2011 + value2012 + value2013
	output[country] = {"total": value2007 + value2008 + value2009 + value2010 + value2011 + value2012 + value2013, "2007" : value2007,  "2008" :  value2008, "2009" : value2009, "2010" : value2010, "2011" : value2011, "2012" : value2012, "2013" : value2013}
	i += 1
# print json.dumps(output, indent=4)

with open('EC_countrytotal_dict.json', 'wb') as jsonfile:
	json.dump(output, jsonfile, indent=4, encoding="latin-1")

########################################################################