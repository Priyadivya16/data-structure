def binary_search(a,x):
    low,high =0, len(a)-1
    while low <= high:
        mid = (low + high)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid -1
    return -1
a = list(map(int,input("Enter elements:").split()))
a.sort()
x = int(input("Enter element to search:"))
r = binary_search(a,x)
print("found at index", r if r!=-1 else "Not Found")
