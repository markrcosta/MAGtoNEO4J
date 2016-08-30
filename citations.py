import csv
import sys
import io
import os

csv.field_size_limit(sys.maxsize)

for filename in os.listdir("."):
    if filename.startswith('Paper'):
        print (filename)
        csvin = io.open(filename, "r",encoding="utf-8")
        csvreader = csv.reader(csvin, delimiter='\t')
        outname = os.path.splitext(filename)[0]
        outname = '/usr/share/neo4j/import/'+outname + '.csv'
        csvout = open(outname,"w", encoding='utf-8')
        csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

        csvwrite.writerow([':START_ID(Paper)',':END_ID(Paper)'])
        for row in csvreader:
            csvwrite.writerow ([row[0],row[1]])

        csvin.close()
        csvout.close()
