import csv
import io
import os
import sys

csv.field_size_limit(sys.maxsize)


csvin = io.open('Papers.txt', "r",encoding="utf-8")
csvreader = csv.reader(csvin, delimiter='\t')

csvout = io.open('paperconference.csv',"w", encoding='utf-8')
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')
csvwrite.writerow([':START_ID(Paper)',':END_ID(Conference)'])

for row in csvreader:
    if row[9] !='':
        csvwrite.writerow ([row[0],row[9]])

csvin.close()
csvout.close()
