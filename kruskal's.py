n = int(input("Vertices:"))
e = int(input("Edges:"))

edges = []
for _ in range(e):
    u ,v,w = map(int,input().split())
    edges.append((w,u,v))
edges.sort()
parent = list(range(n))
cost = 0

def find(x):
    while parent[x] !=x:
        x = parent[x]
    return x
for w,u,v in edges:
    a,b = find(u),find(v)
    if  a!=b:
        parent[a] = b
        print(u,"-",v,"=",w)
        cost +=w
print("Minimum Cost:",cost)
