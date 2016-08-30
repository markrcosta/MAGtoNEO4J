import csv
import io
import os

csvin = io.open('CleanPapers.txt', "r",encoding="utf-8")
csvreader = csv.reader(csvin, delimiter='\t')
csvout = open('/usr/share/neo4j/import/papers.csv',"w", encoding='utf-8')
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')
csvwrite.writerow(['PaperID:ID(Paper)','PaperTitle:String','PaperYear:INT','PaperDate:String','PaperDOI:String','VenueName:String','PaperRank:INT'])

for row in csvreader:
    csvwrite.writerow ([row[0],row[2],row[3],row[4],row[5],row[7],row[10]])

csvin.close()
csvout.close()
