def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day  1\calorieInput.txt")
    sums = []
    cur = []
    for line in f:
        line = line.strip()
        if line.isnumeric():
            cur.append(int(line))
        else:
            sums.append(sum(cur))
            cur = []
    f.close()

    sums.sort(reverse=True)
    print(sum(sums[:3]))
if __name__=="__main__":
    main()