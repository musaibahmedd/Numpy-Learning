import numpy as np

# Simulated daily stock prices
prices = np.array([
    102, 105, 101, 110, 115,
    108, 120, 118, 125, 130
])

# Calculate daily average
average_price = np.mean(prices)

# Find highest and lowest prices
highest_price = np.max(prices)
lowest_price = np.min(prices)

# Find prices above average
above_average = prices[prices > average_price]

# Calculate 10% increase
future_prices = prices * 1.10

# Calculate price difference
price_change = prices[-1] - prices[0]

print("Average:", average_price)
print("Highest:", highest_price)
print("Lowest:", lowest_price)
print("Above average:", above_average)
print("Price change:", price_change)