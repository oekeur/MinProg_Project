#!/usr/bin/env python
# -*- coding: latin-1 -*-

# import json

# with open('countrycode.json', 'r') as infile:
# 	conversion = json.load(infile)
# infile.close()
# with open('EC_2007_countrytotal.json', 'r') as infile:
# 	data2007 = json.load(infile)
# infile.close()
# with open('EC_2008_countrytotal.json', 'r') as infile:
# 	data2008 = json.load(infile)
# infile.close()
# with open('EC_2009_countrytotal.json', 'r') as infile:
# 	data2009 = json.load(infile)
# infile.close()
# with open('EC_2010_countrytotal.json', 'r') as infile:
# 	data2010 = json.load(infile)
# infile.close()
# with open('EC_2011_countrytotal.json', 'r') as infile:
# 	data2011 = json.load(infile)
# infile.close()
# with open('EC_2012_countrytotal.json', 'r') as infile:
# 	data2012 = json.load(infile)
# infile.close()
# with open('EC_2013_countrytotal.json', 'r') as infile:
# 	data2013 = json.load(infile)

# output = []

# i = 0
# for country in conversion:
# 	try:
# 		output.append({conversion[i].values()[0] : {"total": data2007[conversion[i].keys()[0]] + data2008[conversion[i].keys()[0]] + data2009[conversion[i].keys()[0]] + data2010[conversion[i].keys()[0]] + data2011[conversion[i].keys()[0]] + data2012[conversion[i].keys()[0]] + data2013[conversion[i].keys()[0]], 
# 			"2007" : data2007[conversion[i].keys()[0]], "2008" :  data2008[conversion[i].keys()[0]],"2009" : data2009[conversion[i].keys()[0]],"2010" : data2010[conversion[i].keys()[0]],"2011" : data2011[conversion[i].keys()[0]],"2012" : data2012[conversion[i].keys()[0]],"2013" : data2013[conversion[i].keys()[0]]}})
# 	except:
# 		pass
# 	i += 1

# with open('EC_countrytotal.json', 'wb') as jsonfile:
# 	json.dump(output, jsonfile, indent=4, encoding="latin-1")

#########################################################################