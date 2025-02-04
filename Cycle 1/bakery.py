from scipy.optimize import linprog

# Coefficients of the objective function (maximize revenue)
# We use negative because linprog minimizes by default
c = [-5, -3]  # Revenue: 5 per chocolate cake, 3 per vanilla cake

# Coefficients for the inequality constraints
A = [
    [2, 1],   # 2x + y <= 500 (cost constraint)
    [1, 1],   # x + y <= 400 (production capacity constraint)
]

# Right-hand side of the inequality constraints
b = [500, 400]

# Bounds for x and y (non-negativity constraints and demand constraints)
x_bounds = (100, None)  # x >= 100 (chocolate cake demand)
y_bounds = (50, None)   # y >= 50 (vanilla cake demand)

# Solve the linear program
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Check if the optimization was successful
if result.success:
    # Output the optimal values for x (chocolate cakes) and y (vanilla cakes)
    print(f"Optimal number of chocolate cakes (x): {result.x[0]}")
    print(f"Optimal number of vanilla cakes (y): {result.x[1]}")
    print(f"Maximum revenue: ${-result.fun}")  # We multiply by -1 because we minimized the negative revenue
else:
    print("Optimization failed. Please check the constraints or try again.")
