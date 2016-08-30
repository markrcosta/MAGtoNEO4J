import csv
import io
import os
import sys

csv.field_size_limit(sys.maxsize)

csvin = io.open('Papers.txt', "r",encoding="utf-8")
csvreader = csv.reader(csvin, delimiter='\t')

csvout = open('paperjournal.csv',"w", encoding='utf-8')
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')
csvwrite.writerow([':START_ID(Paper)',':END_ID(Journal)'])

for row in csvreader:
    if row[8] !='':
        csvwrite.writerow ([row[0],row[8]])


csvin.close()
csvout.close()
