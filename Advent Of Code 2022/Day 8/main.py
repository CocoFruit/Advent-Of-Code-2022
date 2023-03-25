def checkVisible(rowNum,colNum,grid):
    # print("-")
    # print("checking:",grid[rowNum][colNum],"at row ",rowNum," col ",colNum)

    #check l-r
    if max(grid[rowNum][:colNum]) < grid[rowNum][colNum]:
        print("l-r",grid[rowNum][colNum],"row:",rowNum,"col:",colNum)
        return 1    
    # chek r-l
    if max(grid[rowNum][colNum+1:]) < grid[rowNum][colNum]:
        print("r-l",grid[rowNum][colNum],"row:",rowNum,"col:",colNum)
        return 1
    # check t-b
    col = []
    for y in range(rowNum):
        col.append(grid[y][colNum])
    if max(col) < grid[rowNum][colNum]:
        print("t-b",grid[rowNum][colNum],"row:",rowNum,"col:",colNum)
        # print(col,"\n")
        return 1
    # check b-t
    col = []
    for y in range(rowNum+1,len(grid)):
        col.append(grid[y][colNum])
    if max(col) < grid[rowNum][colNum]:
        print("b-t",grid[rowNum][colNum],"row:",rowNum,"col:",colNum)
        # print(col,"\n")
        return 1
    return 0

def getScenicScore(rowNum,colNum,grid):
    #check l-r
    l = 0
    # print(grid[rowNum][colNum],grid[rowNum][:colNum])
    if colNum==0:
        l = 0
    else:
        # print(grid[rowNum][colNum],list(reversed(grid[rowNum][:colNum])))
        for i,num in enumerate(reversed(grid[rowNum][:colNum])):
            print(i,num)
            if num < grid[rowNum][colNum]:
                l+=1
            elif num == grid[rowNum][colNum] or i==0:
                l+=1
                break
            else:
                break
      
    # chek r-l
    r = 0
    # # if colNum==len(grid[0])-1:
    # #     r = 0
    # else:
    for num in grid[rowNum][colNum+1:]:
        # print(grid[rowNum][colNum+1:])
        if num < grid[rowNum][colNum]:
            r+=1
        else:
            r+=1
            break

    # if max(grid[rowNum][colNum+1:]) < grid[rowNum][colNum]:
    #     print("r-l",grid[rowNum][colNum],"row:",rowNum,"col:",colNum)
    #     return 1

    # check t-b
    t = 1
    if rowNum == 0:
        t = 0
    else:
        col = []
        for y in range(rowNum):
            col.append(grid[y][colNum])
        for num in col[1:]:
            if num < grid[rowNum][colNum]:
                t+=1
            # else:
            #     break
    # if max(col) < grid[rowNum][colNum]:
    #     print("t-b",grid[rowNum][colNum],"row:",rowNum,"col:",colNum)
    #     # print(col,"\n")
    #     return 1
 
    # check b-t
    b = 1
    if rowNum == len(grid)-1:
        b = 0
    else:
        col = []
        for y in range(rowNum+1,len(grid)):
            col.append(grid[y][colNum])
        # print(grid[rowNum][colNum],col[1:])
        for num in col[1:]:
            if num < grid[rowNum][colNum]:
                b+=1
            # else:
            #     break
    
    # if max(col) < grid[rowNum][colNum]:
    #     print("b-t",grid[rowNum][colNum],"row:",rowNum,"col:",colNum)
    #     # print(col,"\n")
    #     return 1
    print(grid[rowNum][colNum],"row:",rowNum,"col:",colNum," |  l:",l,"r:",r,"t:",t,"b:",b," | ",l*r*t*b)
    return l * r * t * b

def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 8\input.txt")
    grid = []
    for line in f:
        grid.append(list(map(int,line.strip().split(" ")[0])))
    count = len(grid[0])*2+len(grid)*2-4
    mostScenic = 0

    # for row in grid[1:-1]:
        # for colNum in range(1,len(row[1:])):
            # count += checkVisible(rowNum,colNum,grid) # part one

    for rowNum in range(len(grid)):
        for colNum in range(len(grid[rowNum])):
            curScenic = getScenicScore(rowNum,colNum,grid)
            if curScenic > mostScenic:
                mostScenic = curScenic
        print("---------------------------------------------")
            


    # print(count) # part one
    print(mostScenic)
if __name__=="__main__":
    main()