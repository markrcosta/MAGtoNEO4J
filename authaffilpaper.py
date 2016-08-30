import csv
import sys

csv.field_size_limit(sys.maxsize)

csvin = open('PaperAuthorAffiliations.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')

csvout = open('authaffilpaper.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow([':START_ID(AuthorAffiliation)',':END_ID(Paper)'])


for row in csvreader:
    if row[1] != '' and row[2] !='':
        csvwrite.writerow ([row[1]+row[2],row[0]])

csvin.close()
csvout.close()
