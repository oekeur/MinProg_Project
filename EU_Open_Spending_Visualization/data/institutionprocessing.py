import json

with open('EC_institutions.json', 'r') as infile:
	conversion = json.load(infile)
infile.close()
with open('EC_institutions_dict.json', 'r') as infile:
	keys = json.load(infile)
infile.close()
with open('EC_2007_institutiontotal.json', 'r') as infile:
	data2007 = json.load(infile)
infile.close()
with open('EC_2008_institutiontotal.json', 'r') as infile:
	data2008 = json.load(infile)
infile.close()
with open('EC_2009_institutiontotal.json', 'r') as infile:
	data2009 = json.load(infile)
infile.close()
with open('EC_2010_institutiontotal.json', 'r') as infile:
	data2010 = json.load(infile)
infile.close()
with open('EC_2011_institutiontotal.json', 'r') as infile:
	data2011 = json.load(infile)
infile.close()
with open('EC_2012_institutiontotal.json', 'r') as infile:
	data2012 = json.load(infile)
infile.close()
with open('EC_2013_institutiontotal.json', 'r') as infile:
	data2013 = json.load(infile)

intermediate = dict()

i = 0
for institution in conversion:
	if conversion[i].keys()[0] in data2007.keys():
		value2007 = data2007[conversion[i].keys()[0].encode('latin-1')]
	else:
		value2007 = 0
	if conversion[i].keys()[0] in data2008.keys():
		value2008 = data2008[conversion[i].keys()[0].encode('latin-1')]
	else:
		value2008 = 0
	if conversion[i].keys()[0] in data2009.keys():
		value2009 = data2009[conversion[i].keys()[0].encode('latin-1')]
	else:
		value2009 = 0
	if conversion[i].keys()[0] in data2010.keys():
		value2010 = data2010[conversion[i].keys()[0].encode('latin-1')]
	else:
		value2010 = 0
	if conversion[i].keys()[0] in data2011.keys():
		value2011 = data2011[conversion[i].keys()[0]]
	else:
		value2011 = 0
	if conversion[i].keys()[0] in data2012.keys():
		value2012 = data2012[conversion[i].keys()[0]]
	else:
		value2012 = 0
	if conversion[i].keys()[0] in data2013.keys():
		value2013 = data2013[conversion[i].keys()[0]]
	else:
		value2013 = 0
	intermediate[conversion[i].keys()[0]] = {"2007" : value2007, "2008" : value2008, "2009" : value2009, "2010" : value2010, "2011" : value2011, "2012" : value2012, "2013" : value2013}
	i += 1

#########################################
# print json.dumps(intermediate, indent=4)
# print json.dumps(keys, indent=4)
######################################### 

output = dict.fromkeys(set(keys.values()), {"2007" : 0,"2008" : 0,"2009" : 0,"2010" : 0,"2011" : 0,"2012" : 0,"2013" : 0, "total" : 0})

for institution in intermediate:
	output[keys[institution]] = {"2007" : output[keys[institution]]["2007"] + intermediate[institution]["2007"], "2008" : output[keys[institution]]["2008"] + intermediate[institution]["2008"], "2009" : output[keys[institution]]["2009"] + intermediate[institution]["2009"], "2010" : output[keys[institution]]["2010"] + intermediate[institution]["2010"], "2011" : output[keys[institution]]["2011"] + intermediate[institution]["2011"], "2012" : output[keys[institution]]["2012"] + intermediate[institution]["2012"], "2013" : output[keys[institution]]["2013"] + intermediate[institution]["2013"], "total" : output[keys[institution]]["total"] + intermediate[institution]["2007"] + intermediate[institution]["2008"] + intermediate[institution]["2009"] + intermediate[institution]["2010"] + intermediate[institution]["2011"] + intermediate[institution]["2012"] + intermediate[institution]["2013"]}
print json.dumps(output, indent=4)


#########################################
# print json.dumps(output, indent=4)
#########################################

# with open('EC_institutiontotal.json', 'wb') as jsonfile:
# 	json.dump(intermediate, jsonfile, indent=4, encoding="latin-1")
# jsonfile.close()
with open('EC_categorytotal.json', 'wb') as jsonfile:
	json.dump(output, jsonfile, indent=4, encoding="latin-1")
jsonfile.close()