def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


def main():
    my_list = list(map(int, input("Enter elements: ").split()))

    print("List:", my_list)

    sorted_list = quicksort(my_list)

    print("Sorted list:", sorted_list)


if __name__ == "__main__":
    main()
