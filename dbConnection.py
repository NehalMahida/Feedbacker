import csv

values = (1, 2)
with open('createFiles/TRP.csv') as f:
        data=[tuple(line) for line in csv.reader(f)]
        data = data[0]
    
values = values + data
print(values)