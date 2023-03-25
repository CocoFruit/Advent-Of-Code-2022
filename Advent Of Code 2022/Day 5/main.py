def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 5\crateInput.txt")
    dataStructure = [["N","W","F","R","Z","S","M","D"],["S","G","Q","P","W"],["C","J","N","F","Q","V","R","W"],["L","D","G","C","P","Z","F"],["S","P","T"],["L","R","W","F","D","H"],["C","D","N","Z"],["Q","J","S","V","F","R","N","W"],["V","W","Z","G","S","M","R"]]
    # dataStructure = [["N","Z"],["D","C","M"],["P"]]
    out = ""
    for line in f:
        line = line.split(" ")
        count = int(line[1])
        start = int(line[3])
        end = int(line[5])
        print(count,start,end)
        thingy = []
        for i in range(count):
            # dataStructure[end-1].insert(0,dataStructure[start-1][0])
            thingy.insert(0,dataStructure[start-1][0])
            del dataStructure[start-1][0]
        for j in range(count):
            dataStructure[end-1].insert(0,thingy[j])

        print(dataStructure)

    for col in dataStructure:
        out += col[0]
    print(out)
if __name__=="__main__":
    main()