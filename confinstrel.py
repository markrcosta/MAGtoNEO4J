import csv

csvin = open('ConferenceInstances.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')
csvout = open('/usr/share/neo4j/import/confinstrelations.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow([':START_ID(Conference)',':END_ID(ConferenceInstance'])
for row in csvreader:
    csvwrite.writerow ([row[0],row[1]])

csvin.close()
csvout.close()
