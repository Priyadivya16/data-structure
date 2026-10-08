def heapify(a, n, i):
    m = i
    l, r = 2*i+1, 2*i+2

    if l < n and a[l] > a[m]: m = l
    if r < n and a[r] > a[m]: m = r

    if m != i:
        a[i], a[m] = a[m], a[i]
        heapify(a, n, m)

def heapsort(a):
    n = len(a)
    for i in range(n//2-1, -1, -1):
        heapify(a, n, i)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)

a = list(map(int, input("Enter numbers: ").split()))
heapsort(a)
print("Sorted:", a)
