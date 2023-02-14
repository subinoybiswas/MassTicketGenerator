import csv
with open('abcde.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for lims in spamreader:
        print(lims[0])