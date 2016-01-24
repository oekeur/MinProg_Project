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
	try:
		output[country] = {"total": data2007[conversion[country]] + data2008[conversion[country]] + data2009[conversion[country]] + data2010[conversion[country]] + data2011[conversion[country]] + data2012[conversion[country]] + data2013[conversion[country]], "2007" : data2007[conversion[country]],  "2008" :  data2008[conversion[country]], "2009" : data2009[conversion[country]], "2010" : data2010[conversion[country]], "2011" : data2011[conversion[country]], "2012" : data2012[conversion[country]], "2013" : data2013[conversion[country]]}
	except:
		pass
	i += 1
# print json.dumps(output, indent=4)

with open('EC_countrytotal_dict.json', 'wb') as jsonfile:
	json.dump(output, jsonfile, indent=4, encoding="latin-1")

########################################################################