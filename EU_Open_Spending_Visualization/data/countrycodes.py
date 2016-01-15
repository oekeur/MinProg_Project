import json

with open('input/country-codes.json', 'r') as infile:
	data = json.load(infile)
outputdata = []

i = 0
for country in data:
	outputdata.append({data[i]["name"] : data[i]["country-code"]})
	i += 1

# print outputdata

with open('countrycode.json', 'wb') as outfile:
	json.dump(outputdata, outfile, indent=4, encoding="latin-1")

infile.close()
outfile.close()
