import numpy as np

#zeros = unknown
#ones = sensor
#negative ones = beacon
#two = known not there

def diamond2(r):
    b = np.r_[:r,r:-1:-1]
    return (b[:,None]+b)>=r

def main():
    sensorDict = {}
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 15\input.txt")
    maxX = 0
    maxY = 0
    minX = 0
    minY = 0
    for line in f:
        line = line.split("=")
        x ,y  = int(line[1].split(",")[0]),int(line[2].split(":")[0])
        x2,y2 = int(line[3].split(",")[0]),int(line[4].split("\n")[0])

        maxX = max(x,x2,maxX)
        maxY = max(y,y2,maxY)
        minX = min(x,x2,minX)
        minY = min(y,y2,minY)
        sensorDict[(x,y)]=(x2,y2)
    print(minY,minX)

    # grid = {(i,j):0 for i in range()}


    # xS = abs(minX)
    # yS = abs(minY)


    # grid = np.zeros([maxY+1+yS,maxX+1+xS],dtype=int)
    # for sensor in sensorDict:
    #     grid[sensor[1]+yS,sensor[0]+xS] = 1
    #     grid[sensorDict[sensor][1]+yS,sensorDict[sensor][0]+xS] = -1
    

    # for row in grid:
    #     print(list(row))
    
if __name__=="__main__":
    main()