import csv

csvin = open('ConferenceInstances.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')
csvout = open('/usr/share/neo4j/import/conferenceinstances.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

new_dat = []
csvwrite.writerow(['ConfInstID:ID(ConferenceInstance)','ConfInstName:String','Location:String','ConfURL:String','ConfStartDate:String','ConfEndDate:String'])
for row in csvreader:
    csvwrite.writerow ([row[1],row[3],row[4],row[5],row[6],row[7]])

csvin.close()
csvout.close()
