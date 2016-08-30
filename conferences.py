import csv

csvin = open('Conferences.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')
csvout = open('/usr/share/neo4j/import/conferences.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow(['ConfID:ID(Conference)','ConfName:String'])
for row in csvreader:
    b = '\"'+row[2]+'\"'
    csvwrite.writerow ([row[0],'"'+row[2]]+'"')

csvin.close()
csvout.close()
