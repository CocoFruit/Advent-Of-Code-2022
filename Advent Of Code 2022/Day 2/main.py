def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 2\moveInput.txt")
    total = 0
    comboDict = {
                 "A X":1+3,"A Y":2+6,"A Z":3+0,
                 "B X":1+0,"B Y":2+3,"B Z":3+6,
                 "C X":1+6,"C Y":2+0,"C Z":3+3
                 }
    comboDict2 = {
                 "A X":3,"A Y":6,"A Z":0,
                 "B X":0,"B Y":3,"B Z":6,
                 "C X":6,"C Y":0,"C Z":3
                 }
                  
    for line in f:
        if line[2]=="X":
            for key in comboDict:
                if key[0] == line[0] and comboDict2[key]==0:    
                    total+=comboDict[key]
        elif line[2]=="Y":
            for key in comboDict:
                if key[0] == line[0] and comboDict2[key]==3:    
                    total+=comboDict[key]
        elif line[2]=="Z":
            for key in comboDict:
                if key[0] == line[0] and comboDict2[key]==6:    
                    total+=comboDict[key]

    print(total)

if __name__=="__main__":
    main()