import json

with open('input/country-codes.json', 'r') as infile:
	data = json.load(infile)
outputdata = {}

# For each of the countries in the list determine the name and code
i = 0
for country in data:
	outputdata[data[i]["country-code"]]  = data[i]["name"]
	i += 1

# save this dictionary for conversion between datasets using name or code as keys
with open('countrycode.json', 'wb') as outfile:
	json.dump(outputdata, outfile, indent=4, encoding="latin-1")

infile.close()
outfile.close()
