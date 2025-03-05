import math

# Function to calculate Economic Order Quantity (EOQ)
def calculate_eoq(annual_demand, ordering_cost, holding_cost):
    """
    Calculates the Economic Order Quantity (EOQ).
    
    Parameters:
    annual_demand (int or float): Annual demand for the product (units)
    ordering_cost (int or float): Ordering cost per order
    holding_cost (int or float): Holding cost per unit per year
    
    Returns:
    float: The Economic Order Quantity (EOQ)
    """
    eoq = math.sqrt((2 * annual_demand * ordering_cost) / holding_cost)
    return eoq

# Given data
annual_demand = 10000  # units
ordering_cost = 200    # dollars per order
holding_cost = 5      # dollars per unit per year

# Calculate EOQ
eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost)

# Print the calculated EOQ
print(f"The Economic Order Quantity (EOQ) is: {eoq:.2f} units")
