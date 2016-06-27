import csv

f = open("scripts/sheet.csv")
csv_f = csv.reader(f)

for row in csv_f:
    print row
