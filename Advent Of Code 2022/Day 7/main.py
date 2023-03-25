def main():
    dirDict = {'/':0}
    curCds = ['/']
    with open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 7\systemInput.txt", "r") as f:
        for line in f.readlines():
            l = line[:-1].split(" ")
            if l[0] == '$':
                if l[1] == 'cd':
                    if l[2] == '..':
                        curCds.pop()
                    elif l[2] == '/':
                        curCds = ['/']
                    else:
                        curCds.append(l[2])
            elif l[0] == 'dir':
                dirDict["".join(curCds)+l[1]] = 0
            else:
                dirDict["".join(curCds)] += int(l[0])
                for i in range(1, len(curCds)):
                    dirDict["".join(curCds[:-i])] += int(l[0])

    print(sum(v for v in dirDict.values() if v <= 100000)) # part 1
    print(min(directory for directory in dirDict.values() if directory >= 30000000-(70000000-(max(d for d in dirDict.values()))))) # part 2 (uglified cuz its 12:30pm)
if __name__=="__main__":
    main()