from itertools import permutations

def tsp(g, s):
    n = len(g)
    v = [i for i in range(n) if i != s]
    minimum = 999999

    for p in permutations(v):
        cost = 0
        k = s

        for j in p:
            cost += g[k][j]
            k = j

        cost += g[k][s]
        minimum = min(minimum, cost)

    return minimum

n = int(input("Enter N: "))
g = [list(map(int, input().split())) for _ in range(n)]

while True:
    s = int(input("Enter starting vertex: "))
    print("Minimum cost:", tsp(g, s))
    again = input("try again(y/n):")
    if again.lower() != 'y':
        break
