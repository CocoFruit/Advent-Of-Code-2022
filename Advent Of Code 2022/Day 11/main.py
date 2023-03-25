from math import prod

class Monkey:
    def __init__(self,num,items,op,test,t,f):
        self.num = num
        self.items = items
        self.op = op
        self.test = test
        self.t = t
        self.f = f
        self.itemsInspected = 0

def main():
    monkeys = []
    file = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code\Day 11\input.txt")
    num = 0
    items = []
    op,test = "",""
    t,f = 0,0

    for line in file:
        if line[:6] == "Monkey":
            num = line[7]
        elif line[:7] == "  Start":
            items = list(map(int,line.strip()[16:].split(", ")))
        elif line[:4] == "  Op":
            op = line.strip()[17:]
        elif line[:6] == "  Test":
            test = int(line.strip()[19:])
        elif line[7:11] == "true":
            t = int(line[29])
        elif line[7:12] == "false":
            f = int(line[30])
            monkeys.append(Monkey(num,items,op,test,t,f))

    file.close()




    for round in range(1,10001):
        # print(f"----------------------\nRound: {round}\n----------------------")
        modThing = prod(monkey.test for monkey in monkeys)
        for monkey in monkeys:
            for item in monkey.items:
                # print(item)
                new = 0
                old = item
                new = eval(monkey.op)
                # new = new//3
                new = new%modThing
                monkey.itemsInspected += 1
                if new % monkey.test==0:
                    # print(f"item with worry level of {new} is thrown to monkey {monkey.t}")
                    monkeys[monkey.t].items.append(new)
                else:
                    # print(f"item with worry level of {new} is thrown to monkey {monkey.f}")
                    monkeys[monkey.f].items.append(new)
                monkey.items = []

    # for monkey in monkeys:
    #     print(monkey.itemsInspected)
    print(sorted([monkey.itemsInspected for monkey in monkeys],reverse=True))

if __name__=="__main__":
    main()