import json

with open('gdp_world.json', 'r') as infile:
	data = json.load(infile)
infile.close()
with open('countrycode.json', 'r') as infile:
	conversion = json.load(infile)
infile.close()

# print json.dumps(data, indent=4)
print json.dumps(conversion, indent=4)

dictkeys = {}

for item in conversion:
	dictkeys[item] = 0
 
output = dict.fromkeys(dictkeys, {"2007" : 0,"2008" : 0,"2009" : 0,"2010" : 0,"2011" : 0,"2012" : 0,"2013" : 0, "avg": 0})

i = 0
for country in conversion:
	try:
		output[country] = {"avg": , "2007" : data[conversion[country]],  "2008" :  data[conversion[country]], "2009" : data[conversion[country]], "2010" : data[conversion[country]], "2011" : data[conversion[country]], "2012" : data[conversion[country]], "2013" : data[conversion[country]]}
	except:
		pass
	i += 1