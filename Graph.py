class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self,u,v):
        self.graph.setdefault(u,[]).append(v)
        self.graph.setdefault(v,[]).append(u)
    def dfs(self,node,visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(node,end=" ")
        for n in self.graph[node]:
            if n not in visited:
                self.dfs(n,visited)
    def bfs(self,start):
        visited = {start}
        queue = [start]
        while queue:
            node = queue.pop(0)
            print(node,end=" ")
            for n in self.graph[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
g = Graph()
n = int(input("Enter number of nodes:"))
for i in range(n):
    g.graph[i+1] = []
e= int(input("Enter number of edges:"))
for i in range(e):
    u,v = map(int,input("Enter edge:").split())
    g.add_edge(u,v)
start = int(input("Enter Source node:"))
print("DFS:", end=" ")
g.dfs(start)
print("\nBFS:", end=" ")
g.bfs(start)
