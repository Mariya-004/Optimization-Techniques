def knapsack(n, c, w, v):
    mat = [[0] * (c + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if j >= w[i - 1]:
                mat[i][j] = max(mat[i - 1][j], v[i - 1] + mat[i - 1][j - w[i - 1]])
            else:
                mat[i][j] = mat[i - 1][j]

    # Trace the items that are included
    included_items = []
    cap = c
    for i in range(n, 0, -1):
        if mat[i][cap] != mat[i - 1][cap]:
            included_items.append(i - 1)
            cap -= w[i - 1]

    # Output results
    print("Included items:", included_items)
    print("Maximum value:", mat[n][c])
    return mat[n][c]

def main():
    cap = int(input("Enter the capacity of the knapsack: "))
    n = int(input("Enter the number of items: "))
    W = [int(input(f"Enter the weight of item {i + 1}: ")) for i in range(n)]
    V = [int(input(f"Enter the value of item {i + 1}: ")) for i in range(n)]
    
    knapsack(n, cap, W, V)





