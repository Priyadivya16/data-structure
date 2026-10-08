INF = 999999

def prim(G):
    n = len(G)
    selected = [False] * n
    selected[0] = True

    print("Edge : Weight")

    for _ in range(n - 1):
        minimum = INF
        a = b = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and G[i][j] != 0:
                        if G[i][j] < minimum:
                            minimum = G[i][j]
                            a, b = i, j

        print(a, "-", b, ":", G[a][b])
        selected[b] = True


n = int(input("Enter number of vertices: "))
G = [list(map(int, input().split())) for _ in range(n)]

prim(G)
