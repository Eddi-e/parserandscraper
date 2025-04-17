#parsing a csv file 
import parser
import os
import re


def main():
    syslist = os.listdir()
    optionlist = []
    for i,filechoice in enumerate(syslist):       
        match = re.search(r'\.csv$',filechoice)
        if match:
            print(i,filechoice)
            optionlist.append(i)

    filename = int(input("input file number:\n"))
    if filename in optionlist:
        csvlist = parser.parseFile(syslist[filename])


    #csv file is in layout title,surname,firstname,choice of (Ok,Maybe,Yes),read TRUE or FALSE

    print(csvlist)
if __name__ == "__main__":
    main()