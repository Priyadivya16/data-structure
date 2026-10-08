def knapsack(wt, val, W, n, t):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1, t),
            knapsack(wt, val, W, n - 1, t)
            )
    else:
        t[n][W] = knapsack(wt, val, W, n - 1, t)

    return t[n][W]


def main():
    weights = list(map(int, input("Enter weights: ").split()))
    values = list(map(int, input("Enter values: ").split()))
    capacity = int(input("Enter capacity: "))

    n = len(weights)
    t = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
    result = knapsack(weights, values, capacity, n, t)
    print("Maximum value:", result)


if __name__ == "__main__":
    main()
                                                                 
