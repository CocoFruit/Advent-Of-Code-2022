def main():
    f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 10\input.txt")
    x = 1
    specials = list(range(20,221,40))
    screen = []
    for y in range(6):
        screen.append(["#"]+["."]*39)

    for row in screen:
        print("".join(row))
    
    crtX = 0
    crtY = 0

    specialX = 0
    cycle = 1
    for line in f:
        line = line.strip()
        if line != "noop":
            line = line.split(" ")
            if crtX in [x-1,x,x+1]:
                screen[crtY][crtX] = "#"
                print(f"{cycle} | printed at {crtX},{crtY} | sprite X: {x}")
                
            for i in range(1):
                cycle += 1
                crtX += 1
                if crtX > 40:
                    crtX = 1
                    crtY += 1
                if crtX in [x-1,x,x+1]:
                    screen[crtY][crtX] = "#"
                    print(f"{cycle} | printed at {crtX},{crtY} | sprite X: {x}")
                    
            x += int(line[1])


        cycle+=1
        crtX+=1
        if crtX > 40:
            crtX = 1
            crtY += 1
        if crtX in [x-1,x,x+1]:
            screen[crtY][crtX] = "#"
            print(f"{cycle} | printed at {crtX},{crtY} | sprite X: {x}")

    for row in screen:
        print(" ".join(row))
    # print(specialX)

if __name__=="__main__":
    main()