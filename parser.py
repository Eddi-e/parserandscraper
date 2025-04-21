import csv
def parseFile(filename):
    list_to_return = []
    with open(filename, newline='',encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            list_to_return.append(row)
    return list_to_return

def writeBackToFile(filename,file_as_list):
    with open("edited"+filename, 'w',newline='',encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Title","Author surname","Author firstname","Interest level","READ??","isbn","rating","number of ratings","number of reviews"])
        for row in file_as_list:
            csvwriter.writerow(row)