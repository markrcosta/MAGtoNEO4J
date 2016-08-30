import csv
import sys

csv.field_size_limit(sys.maxsize)

csvin = open('PaperAuthorAffiliations.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')


csvout = open('/usr/share/neo4j/import/paperauthors.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow([':START_ID(Author)',':END_ID(Paper)'])

for row in csvreader:
    csvwrite.writerow ([row[1],row[0]])

csvin.close()
csvout.close()
