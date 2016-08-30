import csv

csvin = open('PaperKeywords.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')
csvout = open('/usr/share/neo4j/import/keywords.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow([':START_ID(Paper]',':END_ID(FoS)'])
for row in csvreader:
    csvwrite.writerow ([row[0],row[2]])

csvin.close()
csvout.close()
