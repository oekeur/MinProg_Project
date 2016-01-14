import csv
import json
data = []

delimiter = ','


############################################################################# 
datafile = open("original/EC_2007_dirty.csv", "r")
csvdata = csv.reader(datafile, delimiter=';')
for row in csvdata:
	data.append(row)

# remove redundant data
for row in data:
	del row[12]
	del row[10]
	del row[9]
	del row[8]
	del row[7]
	del row[5]
	del row[3]
	del row[2]

# correct missing values
j = 0
for row in data:
	i = 0
	for column in row:
		if '\n' in column:
			data[j][i] = ' / '.join(column.split('\n'))
		if column == '' or column == ' ':
			data[j][i] = 'missing'
		i += 1
	j += 1

i = 0
for row in data:
	print json.dumps({data[0][0]: data[i+1][0], 
						data[0][1]: data[i+1][1],
						data[0][2]: data[i+1][2],
						data[0][3]: data[i+1][3],
						data[0][4]: data[i+1][4],
						data[0][5]: data[i+1][5],
						data[0][5]: data[i+1][6],
						data[0][7]: data[i+1][7],
						data[0][8]: data[i+1][8]}, indent=4, separators=(',', ': '), encoding="latin-1")
	i += 1
# ensure_ascii=False
# with open('EC_2007.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)
# 	for row in data:
# 		writer.writerow(row)
# datafile.close()
# csvfile.close()
# data = []
# #############################################################################
# datafile = open("original/EC_2008_dirty.csv", 'U')
# csvdata = csv.reader(datafile, delimiter=';',  quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# # remove redundant data
# for row in data:
# 	del row[12]
# 	del row[10]
# 	del row[9]
# 	del row[8]
# 	del row[7]
# 	del row[5]
# 	del row[3]
# 	del row[2]

# # correct missing values
# j = 0
# for row in data:
# 	i = 0
# 	for column in row:
# 		if '\n' in column:
# 			data[j][i] = ' / '.join(column.split('\n'))
# 		if column == '' or column == ' ':
# 			data[j][i] = 'missing'
# 		i += 1
# 	j += 1


# with open('EC_2008.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=delimiter)
# 	for row in data:
# 		writer.writerow(row)
# datafile.close()
# csvfile.close()
# data = []
# #############################################################################
# datafile = open("original/EC_2009_dirty.csv")
# csvdata = csv.reader(datafile, delimiter=';',  quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# # remove redundant data
# for row in data:
# 	del row[12]
# 	del row[10]
# 	del row[9]
# 	del row[8]
# 	del row[5]
# 	del row[3]
# 	del row[2]

# # correct missing values
# j = 0
# for row in data:
# 	i = 0
# 	for column in row:
# 		if '\n' in column:
# 			data[j][i] = ' / '.join(column.split('\n'))
# 		if column == '' or column == ' ':
# 			data[j][i] = 'missing'
# 		i += 1
# 	j += 1


# with open('EC_2009.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=delimiter)
# 	for row in data:
# 		writer.writerow(row)
# datafile.close()
# csvfile.close()
# data = []
# #############################################################################
# datafile = open("original/EC_2010_dirty.csv")
# csvdata = csv.reader(datafile, delimiter=';',  quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# # # remove redundant data
# 	del row[12]
# 	del row[11]
# 	del row[10]
# 	del row[7]
# 	del row[5]
# 	del row[4]
# 	del row[3]
# 	del row[0]

# # correct missing values
# j = 0
# for row in data:
# 	i = 0
# 	if row[0] == '' or row[0] == ' ':
# 		row[0] = data[j-1][0]
# 	if row[6] == '' or row[6] == ' ':
# 		row[5] = row[4]
# 	for column in row:
# 		if '\n' in column:
# 			data[j][i] = ' / '.join(column.split('\n'))
# 		if column == '' or column == ' ' or column == '-':
# 			data[j][i] = 'missing'
# 		i += 1
# 	j += 1

# for row in data:
# 	del row[4]
# 	del row[-1]

 
# with open('EC_2010.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=delimiter)
# 	for row in data:
# 		writer.writerow(row)
# datafile.close()
# csvfile.close()
# data = []
# #############################################################################
# datafile = open("original/EC_2011_dirty.csv")
# csvdata = csv.reader(datafile, delimiter=';',  quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# # # remove redundant data
# for row in data:
# 	del row[12]
# 	del row[11]
# 	del row[10]
# 	del row[7]
# 	del row[5]
# 	del row[4]
# 	del row[3]
# 	del row[0]

# # correct missing values
# j = 0
# for row in data:
# 	i = 0
# 	if row[0] == '' or row[0] == ' ':
# 		row[0] = data[j-1][0]
# 	if row[6] == '' or row[6] == ' ':
# 		row[5] = row[4]
# 	for column in row:
# 		if '\n' in column:
# 			data[j][i] = ' / '.join(column.split('\n'))
# 		if column == '' or column == ' ' or column == '-':
# 			data[j][i] = 'missing'
# 		i += 1
# 	j += 1

# for row in data:
# 	del row[4]
# 	del row[-1]
 
# with open('EC_2011.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=delimiter)
# 	for row in data:
# 		writer.writerow(row)
# datafile.close()
# csvfile.close()
# data = []
# #############################################################################
# datafile = open("original/EC_2012_dirty.csv")
# csvdata = csv.reader(datafile, delimiter=';',  quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# # remove redundant data
# for row in data:
# 	del row[13]
# 	del row[12]
# 	del row[11]
# 	del row[10]
# 	del row[7]
# 	del row[5]
# 	del row[4]
# 	del row[3]
# 	del row[0]

# # correct missing values
# j = 0
# for row in data:
# 	i = 0
# 	if row[0] == '' or row[0] == ' ':
# 		row[0] = data[j-1][0]
# 	if row[7] == "Office for Infrastructure and Logistics in Brussels" or row[5] == '' or row[5] == ' ':
# 		row[5] = row[4]
# 	for column in row:
# 		if '\n' in column:
# 			data[j][i] = ' / '.join(column.split('\n'))
# 		if column == '' or column == ' ' or column == '-':
# 			data[j][i] = 'missing'
# 		i += 1
# 	j += 1

# for row in data:
# 	del row[4]
# 	del row[-1]

 
# with open('EC_2012.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=delimiter)
# 	for row in data:
# 		writer.writerow(row)
# datafile.close()
# csvfile.close()
# data = []
# ############################################################################
# datafile = open("original/EC_2013_dirty.csv")
# csvdata = csv.reader(datafile, delimiter=';',  quoting=csv.QUOTE_MINIMAL)
# for row in csvdata:
# 	data.append(row)

# # remove redundant data
# for row in data:
# 	del row[12]
# 	del row[11]
# 	del row[10]
# 	del row[7]
# 	del row[5]
# 	del row[4]
# 	del row[3]
# 	del row[0]

# # correct missing values
# j = 0
# for row in data:
# 	i = 0
# 	if row[0] == '' or row[0] == ' ':
# 		row[0] = data[j-1][0]
# 	if row[7] == "Office for Infrastructure and Logistics in Brussels" or ((row[7] == '' or row[7] == ' ') and data[j-1][7] == "Office for Infrastructure and Logistics in Brussels"):
# 		row[5] = row[4]
# 		row[7] = "Office for Infrastructure and Logistics in Brussels"
# 	for column in row:
# 		if '\n' in column:
# 			data[j][i] = ' / '.join(column.split('\n'))
# 		if column == '' or column == ' ' or column == '-':
# 			data[j][i] = 'missing'
# 		i += 1
# 	j += 1

# for row in data:
# 	del row[4]
# 	del row[-1]

 
# with open('EC_2013.csv', 'wb') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=delimiter)
# 	for row in data:
# 		writer.writerow(row)
# datafile.close()
# csvfile.close()
# data = []