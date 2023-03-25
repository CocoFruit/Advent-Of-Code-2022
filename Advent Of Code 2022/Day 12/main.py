class Node:
    def __init__(self,val,x,y) -> None:
        self.val = val
        self.x = x
        self.y = y
        self.adj = []

class Graph:
    def __init__(self) -> None:
        self.graph = []
        self.tree = {}
        f = open(r"C:\Users\parke\Downloads\PythonProjects\Advent Of Code 2022\Day 12\input.txt")
        for y,line in enumerate(f):
            self.graph.append([])
            for x,char in enumerate(line.strip()):
                self.graph[y].append(Node(char,x,y))
        for row in self.graph:
            for node in row:
                self.tree[node] = []
                if node.val == "S":
                    if node.y-1>0:
                        if self.graph[node.y-1][node.x].val == "a":
                            self.tree[node].append(self.graph[node.y-1][node.x]) 
                    if node.x-1>0:
                        if self.graph[node.y][node.x-1].val == "a":
                            self.tree[node].append(self.graph[node.y][node.x-1]) 
                    if node.x+1 < len(self.graph[0]):
                        if self.graph[node.y][node.x+1].val == "a":
                            self.tree[node].append(self.graph[node.y][node.x+1]) 
                    if node.y+1 < len(self.graph):
                        if self.graph[node.y+1][node.x].val == "a":
                            self.tree[node].append(self.graph[node.y+1][node.x]) 
                            
                # up
                if node.y-1 >= 0:
                    if ord(self.graph[node.y-1][node.x].val)-1==ord(node.val) or node.val==self.graph[node.y-1][node.x].val:
                        self.tree[node].append(self.graph[node.y-1][node.x]) 
                    if node.val == "z" and self.graph[node.y-1][node.x].val == "E":
                        self.tree[node].append(self.graph[node.y-1][node.x]) 
                

                # left
                if node.x-1 >= 0:
                    if ord(self.graph[node.y][node.x-1].val)-1==ord(node.val) or node.val==self.graph[node.y][node.x-1].val:
                        self.tree[node].append(self.graph[node.y][node.x-1]) 
                    if node.val == "z" and self.graph[node.y][node.x-1].val == "E":
                        self.tree[node].append(self.graph[node.y][node.x-1]) 

                # right
                if node.x+1 < len(self.graph[0]):
                    if ord(self.graph[node.y][node.x+1].val)-1==ord(node.val) or node.val==self.graph[node.y][node.x+1].val:
                        self.tree[node].append(self.graph[node.y][node.x+1]) 
                    if node.val == "z" and self.graph[node.y][node.x+1].val == "E":
                        self.tree[node].append(self.graph[node.y][node.x+1]) 

                # bottom
                if node.y+1 < len(self.graph):
                    if ord(self.graph[node.y+1][node.x].val)-1==ord(node.val) or node.val==self.graph[node.y+1][node.x].val:
                        self.tree[node].append(self.graph[node.y+1][node.x]) 
                if node.val == "z" and self.graph[node.y+1][node.x].val == "E":
                        self.tree[node].append(self.graph[node.y+1][node.x]) 

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        print([node.val for node in current_path])
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

def main():
    graph = Graph()
    # print(graph.graph[20][138].val)
    for node in graph.tree:
        print(f"{node.val}: {[node.val for node in graph.tree[node]]}")
    # shortest = shortest_path(graph.tree,graph.graph[20][0],graph.graph[20][138])
    shortest = shortest_path(graph.tree,graph.graph[0][0],graph.graph[4][5])
    print(len(shortest)-1)

if __name__=="__main__":
    main()
