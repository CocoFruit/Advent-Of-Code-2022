import time

def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 4\idInput.txt")
    total = 0
    for pair in f:
        range1,range2 = pair.split(",")
        range1 = list(map(int,range1.split("-")))
        range2 = list(map(int,range2.split("-")))
        for num in range(range1[0],range1[1]+1):
            if num in range(range2[0],range2[1]+1):
                total += 1
                break
    total = [pair for pair in f]
    print(total)

if __name__=="__main__":
    st = time.time()
    main()
    et = time.time()
    print('Execution time:', et-st, 'seconds')
