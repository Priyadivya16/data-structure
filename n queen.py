import itertools

def valid(p):
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if abs(p[i]-p[j]) == j-i:
                return False
        return True
n = int(input("Enter N:"))
sol = [p for p in itertools.permutations(range(n)) if valid(p)]

print("Number of solutions:",len(sol))
for p in sol:
    print(p)
