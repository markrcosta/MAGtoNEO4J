import csv

csvin = open('Affiliations.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')
csvout = open('/usr/share/neo4j/import/affiliations.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow(['AffiliationID:ID(Affiliation)','AffiliationName:String'])
for row in csvreader:
    csvwrite.writerow ([row[0],row[1]])

csvin.close()
csvout.close()
