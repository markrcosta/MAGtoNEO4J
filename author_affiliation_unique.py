import csv
import sys

csv.field_size_limit(sys.maxsize)

csvin = open('PaperAuthorAffiliations.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')

authaffil_list = list()
for row in csvreader:
	if row[2] != '':
		authaffil_list.append(row[1]+row[2])

authaffil_set = set(authaffil_list)
authaffil_list = list(authaffil_set)

csvout = open('authoraffiliations.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow(['AuthorAffiliationID:ID(AuthorAffiliation)'])

for dat in authaffil_list:
    csvwrite.writerow ([dat])

csvin.close()
csvout.close()