import numpy as np

def main():
    
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 8\input.txt")
    arr = np.array([list(map(int,list(thing))) for thing in f.read().split("\n")])
    total = arr.shape[0]*2 + arr.shape[1]*2 - 4
    bestScore = 1

    for y,row in enumerate(arr):
        for x,tree in enumerate(row):
            left = row[:x][::-1]
            right = row[x+1:]
            up = arr[:y,x][::-1]
            down = arr[y+1:,x]
            if y>0 and y<arr.shape[0]-1 and x>0 and x<arr.shape[1]-1:
                if max(left)<tree or max(right)<tree or max(up)<tree or max(down)<tree:
                    total += 1

            score = 1
            for direction in [left,right,up,down]:
                tracker = 0
                for i in range(len(direction)):

                    if direction[i] < tree:
                        tracker += 1

                    elif direction[i] >= tree:
                        tracker += 1
                        break

                score *= tracker
            bestScore = max(bestScore,score)
            
    print(total)
    print(bestScore)

if __name__=="__main__":
    main()