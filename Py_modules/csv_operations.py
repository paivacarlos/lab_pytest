import csv

with open('my_csv_file.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        print(line)

print("==========//===============================")


#  read a csv file like a dictionary
with open('my_csv_file.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    for line in csvFile:
        print(line)
