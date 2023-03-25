import ast
from itertools import zip_longest
from functools import cmp_to_key

def compare(l,r):
    if l is None:
        return -1
    if r is None:
        return 1

    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0
    elif isinstance(l, list) and isinstance(r, list):
        for l2, r2 in zip_longest(l, r):
            if (result := compare(l2, r2)) != 0:
                return result
        return 0
    else:
        l2 = [l] if isinstance(l, int) else l
        r2 = [r] if isinstance(r, int) else r
        return compare(l2, r2)
    
def main():
    global pair,s
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 13\input.txt")
    curLines = []
    s = 0
    pair = 0
    lstOfThngs = []
    for line in f:
        curLines.append(line)
        if len(line)==1:
            pair += 1
            lstOfThngs.append(ast.literal_eval(curLines[0]))
            lstOfThngs.append(ast.literal_eval(curLines[1]))
            if compare(ast.literal_eval(curLines[0]),ast.literal_eval(curLines[1])) <= -1:
                s += pair
            curLines = []

    f.close()
    print(lstOfThngs)

    # part 1
    print(s)
    # part 2
    part2 = 1

    sortedThing = sorted([*lstOfThngs,[[2]],[[6]]],key=cmp_to_key(compare))
    for thing in sortedThing:
        print(thing)
    print(sortedThing.index([[2]])+1)
    print(sortedThing.index([[6]])+1)
    print((sortedThing.index([[6]])+1)*(sortedThing.index([[2]])+1))
if __name__=="__main__":
    main()