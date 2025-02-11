import numpy as np

def vogel_approximation_method(supply, demand, costs):
    transportation_plan = np.zeros_like(costs)
    total_cost = 0

    while np.sum(supply) > 0 and np.sum(demand) > 0:
        row_penalties = [sorted(row)[:2] for row in costs]
        col_penalties = [sorted(costs[:, c])[:2] for c in range(costs.shape[1])]

        max_row_penalty = max(map(lambda x: x[1] - x[0], row_penalties))
        max_col_penalty = max(map(lambda x: x[1] - x[0], col_penalties))

        if max_row_penalty >= max_col_penalty:
            row_idx = row_penalties.index(max(row_penalties, key=lambda x: x[1] - x[0]))
            col_idx = np.argmin(costs[row_idx])
        else:
            col_idx = col_penalties.index(max(col_penalties, key=lambda x: x[1] - x[0]))
            row_idx = np.argmin(costs[:, col_idx])

        allocated = min(supply[row_idx], demand[col_idx])
        supply[row_idx] -= allocated
        demand[col_idx] -= allocated
        transportation_plan[row_idx, col_idx] = allocated
        total_cost += allocated * costs[row_idx, col_idx]

        costs[row_idx, :] = float('inf') if supply[row_idx] == 0 else costs[row_idx, :]
        costs[:, col_idx] = float('inf') if demand[col_idx] == 0 else costs[:, col_idx]

    return transportation_plan, total_cost

# Example usage
supply = np.array([20, 30, 25])
demand = np.array([10, 30, 35])
costs = np.array([
    [8, 6, 10],
    [9, 7, 4],
    [3, 4, 2]
])

plan, cost = vogel_approximation_method(supply, demand, costs)
print("Optimal Transportation Plan:")
print(plan)
print("Total Transportation Cost:", cost)
