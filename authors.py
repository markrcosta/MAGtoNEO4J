import csv

csvin = open('Authors.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')
csvout = open('/usr/share/neo4j/import/authors.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow(['AuthorID:ID(Author)','AuthorName:String'])
for row in csvreader:
    csvwrite.writerow ([row[0],row[1]])

csvin.close()
csvout.close()
