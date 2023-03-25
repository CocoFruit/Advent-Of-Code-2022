import numpy as np



def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code 2022\Day 17\input.txt")
    rocks = [np.array([[1,1,1,1]]),np.array([[0,1,0],[1,1,1],[0,1,0]]),np.array([[0,0,1],[0,0,1],[1,1,1]]),np.array([[1],[1],[1],[1]]),np.array([[1,1],[1,1]])]
    grid = np.zeros([3,7],dtype=int)
    rockNum = 0
    print(grid)

if __name__=="__main__":
    main()