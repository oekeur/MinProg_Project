import json

with open('EC_categorytotal.json', 'r') as infile:
	data = json.load(infile)
infile.close()

i = 0
for category in data:
	print data[category]