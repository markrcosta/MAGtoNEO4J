import csv

csvin = open('Journals.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')
csvout = open('/usr/share/neo4j/import/journals.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow(['JournalID:ID(Journal)','JournalName:String'])
for row in csvreader:
    csvwrite.writerow ([row[0],row[1]])

csvin.close()
csvout.close()
