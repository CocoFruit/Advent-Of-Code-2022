from math import sqrt

def getTailPos(headPos,tailPos):
    distance = sqrt((headPos[0]-tailPos[0])**2 + (headPos[1]-tailPos[1])**2) 
    # print(distance)
    if distance < 2:
        return tailPos


    newTailPos = tailPos[::1]
    if headPos[0] > tailPos[0]: # head to the right of tail
        newTailPos[0]+=1
    if headPos[0] < tailPos[0]: # head to the left of tail
        newTailPos[0]-=1

    if headPos[1] > tailPos[1]: # head above tail
        newTailPos[1]+=1
    if headPos[1] < tailPos[1]: # head below tail
        newTailPos[1]-=1
    
    return newTailPos


def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 9\input.txt")
    headPos = [0,0]
    tailPos = [0,0]
    multiTailPos = [[0,0]]*9
    tailSeen = [[0,0]]

    for move,line in enumerate(f): 
        line = line.split(" x`")
        direction = line[0]
        steps = int(line[1])

        if direction == "R":
            for i in range(steps):
                headPos[0]+=1
                # tailPos = getTailPos(headPos,tailPos)
                multiTailPos[0] = getTailPos(headPos,multiTailPos[0])
                for i in range(1,len(multiTailPos[1:])+1):
                    multiTailPos[i] = getTailPos(multiTailPos[i-1],multiTailPos[i])
                # print(multiTailPos)
                if multiTailPos[-1] not in tailSeen:
                    tailSeen.append(multiTailPos[-1])
        elif direction == "L":
            for i in range(steps):
                headPos[0]-=1
                # tailPos = getTailPos(headPos,tailPos)
                multiTailPos[0] = getTailPos(headPos,multiTailPos[0])
                for i in range(1,len(multiTailPos[1:])+1):
                    multiTailPos[i] = getTailPos(multiTailPos[i-1],multiTailPos[i])
                # print(multiTailPos)
                if multiTailPos[-1] not in tailSeen:
                    tailSeen.append(multiTailPos[-1]) 
        elif direction == "U":
            for i in range(steps):
                headPos[1]+=1
                # tailPos = getTailPos(headPos,tailPos)
                multiTailPos[0] = getTailPos(headPos,multiTailPos[0])
                for i in range(1,len(multiTailPos[1:])+1):
                    multiTailPos[i] = getTailPos(multiTailPos[i-1],multiTailPos[i])
                # print(multiTailPos)
                if multiTailPos[-1] not in tailSeen:
                    tailSeen.append(multiTailPos[-1])
        elif direction == "D":
            for i in range(steps):
                headPos[1]-=1
                # tailPos = getTailPos(headPos,tailPos)
                multiTailPos[0] = getTailPos(headPos,multiTailPos[0])
                for i in range(1,len(multiTailPos[1:])+1):
                    multiTailPos[i] = getTailPos(multiTailPos[i-1],multiTailPos[i])
                # print(multiTailPos)
                if multiTailPos[-1] not in tailSeen:
                    tailSeen.append(multiTailPos[-1]) 
        
        # print("----------------------------------")
    # print(tailSeen)
    print(len(tailSeen))
if __name__=="__main__":
    main()