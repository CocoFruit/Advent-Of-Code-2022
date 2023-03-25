import string
ALPHABET = string.ascii_letters
def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 3\sackInput")
    total = 0
    lines = []
    for i,line in enumerate(f):
        if (i+1) % 3 == 0:
            for char in line:
                if char in lines[0] and char in lines[1]:
                    total+=ALPHABET.index(char)+1
                    lines = []
                    break
        else:
            lines.append(line.strip())
    print(total)
if __name__=="__main__":
    main()
