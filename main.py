#parsing a csv file 
import parser
import os
import re
import seleniumChecker
import time
import random
import isbn


def main():
    worked = False
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
        
        for row in csvlist:
            rowisbn = isbn.getisbn(row[0],row[1],row[2])
            row.append(rowisbn)
            print(f'{rowisbn} is isbn for {row[0]}')
            print(row[5])
            sad_loop = True
            while sad_loop == True:
                try:
                    row_to_append = seleniumChecker.getstats(row[5])
                    sad_loop = False
                except:
                    pass
            row.extend(row_to_append)
            print(row)
            time.sleep(random.randint(1,3))
        parser.writeBackToFile(syslist[filename],csvlist)

    


    #csv file is in layout title,surname,firstname,choice of (Ok,Maybe,Yes),read TRUE or FALSE

    print(csvlist)
if __name__ == "__main__":
    main()