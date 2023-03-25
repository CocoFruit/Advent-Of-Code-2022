import numpy as np
import re
from time import sleep
import os

def main():
    # zeros is air
    # ones is rock
    # neg ones is sand
    grid = np.zeros([1,1],dtype=int)
    f = open(r"CS Club\Advent Of Code 2022\Day 14\input.txt")
    highestY = 0
    for line in f:
        coords = list(map(int,re.split(r' -> |,',line.strip())))
        for i in range(0,len(coords)-3,2):
            x1,y1 = coords[i],coords[i+1]
            x2,y2 = coords[i+2],coords[i+3]
            
            mx = max(x1,x2)
            if mx > grid.shape[1]:
                unpadded = np.copy(grid)
                grid = np.zeros([grid.shape[0],mx+2],dtype=int)
                grid[:unpadded.shape[0],:unpadded.shape[1]] = unpadded
            
            my = max(y1,y2)
            if my > highestY:
                highestY=my

            if my > grid.shape[0]:
                unpadded = np.copy(grid)
                grid = np.zeros([my+2,grid.shape[1]],dtype=int)
                grid[:unpadded.shape[0],:unpadded.shape[1]] = unpadded

            if y2>y1:
                grid[y1:y2,x1]=1
            elif y1>y2:
                grid[y2:y1,x1]=1
            elif x2>x1:
                grid[y1,x1:x2+1]=1
            elif x1>x2:
                grid[y1,x2:x1+1]=1
    
    unpadded = np.copy(grid)
    grid = np.zeros([10000,10000],dtype=int)
    grid[:unpadded.shape[0],:unpadded.shape[1]] = unpadded

    grid[highestY+2,:]=1
    print(grid.shape)
    input("press enter to start")
    c = 0
    going = True
    while not grid[0,500]:
        grid[0,500]=-1
        y,x=0,500
        c+=1
        # print(grid[:,494:503])
        while 1:
            try:
                if grid[y+1,x]==0:
                    grid[y,x]=0
                    y+=1
                    grid[y,x]=-1
                elif grid[y+1,x-1]==0:
                    grid[y,x]=0
                    y,x=y+1,x-1
                    grid[y,x]=-1
                elif grid[y+1,x+1]==0:
                    grid[y,x]=0
                    y,x=y+1,x+1
                    grid[y,x]=-1
                else:
                    break
            except:
                print("Done")
                going = False
                break
            # sleep(.01)
            # os.system('cls')

            # print(grid[:12,490:510])
            # for i in range(grid.shape[0]):
            #     for j in range(494-1,503+1):
            #         n = grid[i,j]
            #         if n == 0:
            #             print(" ",end="")
            #         elif n == 1:
            #             print("#",end="")
            #         elif n == -1:
            #             print("O",end="")
            #     print()
            # input()
    print(f"{highestY} was highestY")
    print(f"{c} pieces of sand fell")
if __name__=="__main__":
    main()