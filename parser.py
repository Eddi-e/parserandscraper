import csv
def parseFile(filename):
    list_to_return = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            list_to_return.append(row)
    return list_to_return