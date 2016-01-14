import os
import sys
import codecs
import cStringIO
import errno
import json
import csv

data =[]

class UTF8Recoder(object):
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("latin-1")


class UnicodeReader(object):
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="latin-1", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "latin-1") for s in row]

    def __iter__(self):
        return self


class UnicodeWriter(object):
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="latin-1", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("latin-1") for s in row])
        # Fetch latin-1 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("latin-1")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

############################################################################
datafile = open("original/EC_2010_dirty.csv")
csvdata = csv.reader(datafile, delimiter=';',  quoting=csv.QUOTE_MINIMAL)
for row in csvdata:
	data.append(row)

# # remove redundant data
	del row[12]
	del row[11]
	del row[10]
	del row[7]
	del row[5]
	del row[4]
	del row[3]
	del row[0]

# correct missing values
j = 0
for row in data:
	i = 0
	if row[0] == '' or row[0] == ' ':
		row[0] = data[j-1][0]
	if row[6] == '' or row[6] == ' ':
		row[5] = row[4]
	for column in row:
		if '\n' in column:
			data[j][i] = ' / '.join(column.split('\n'))
		if column == '' or column == ' ' or column == '-':
			data[j][i] = 'missing'
		i += 1
	j += 1

for row in data:
	del row[4]
	del row[-1]

 
with open('EC_2010.csv', 'wb') as csvfile:
	writer = UnicodeWriter(csvfile)
	for row in data:
		writer.writerow(row)
datafile.close()
csvfile.close()
data = []