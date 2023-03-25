import numpy as np

def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 20\input.txt")
    inputArray = np.array(list(map(int,f.read().split("\n"))))
    zerosArray = np.zeros(len(inputArray),dtype=int)
    arr = np.array(list(zip(inputArray,zerosArray)))
    for i,num in enumerate(arr):
        if not num[1]:
            arr[(i+num[0])%len(arr)] = num[0]
            num[1] = 1
            np.delete(arr,i-1)
    print(arr)        
if __name__=="__main__":
    main()