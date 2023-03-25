def main():

    i = 100
    going = True
    while going:
        d_structure = {}
        f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 21\input.txt")
        for line in f:
            line=line.split(": ")
            d_structure[line[0]] = line[1].strip().split(" ")
        f.close()
        d_structure["humn"] = [str(i)]
        while not (d_structure["root"][0].lstrip("-").isnumeric() and d_structure["root"][0].lstrip("-").isnumeric()):
            for monkey in d_structure:
                # print(d_structure)
                if len(d_structure[monkey])>1:
                    if not d_structure[monkey][0].lstrip("-").isnumeric():
                        if len(d_structure[d_structure[monkey][0]])==1:
                            d_structure[monkey][0]=d_structure[d_structure[monkey][0]][0]
                    if not d_structure[monkey][2].lstrip("-").isnumeric():
                        # print(d_structure[monkey])
                        if len(d_structure[d_structure[monkey][2]])==1:
                            d_structure[monkey][2]=d_structure[d_structure[monkey][2]][0]

                    if d_structure[monkey][0].lstrip("-").isnumeric() and d_structure[monkey][2].lstrip("-").isnumeric() and monkey!="root":
                        d_structure[monkey] = [str(int(eval("".join(d_structure[monkey]))))]
        i+=1
        # print(d_structure["root"])
        print(i)
        if d_structure["root"][0] == d_structure["root"][2]:
            print(d_structure["root"][0])
            print(i)
            break
if __name__=="__main__":
    main()