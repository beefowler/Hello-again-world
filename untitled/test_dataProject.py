__author__ = 'beefowler'

import csv

f = open("test_data.csv")
csv_f = csv.reader(f)
next(f)

counter = 0
for row in csv_f:
       print (row[0], row[2])
       counter = counter + int(row[2])
print counter

f.close()
