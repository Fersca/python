import csv

#Open de file and store it in memory
with open('/Users/Fernando.Scasserra/Downloads/base_extraction.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(row)
        break
