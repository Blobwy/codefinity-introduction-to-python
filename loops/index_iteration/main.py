prices = [29.99, 45.50, 12.75, 38.20]

for index in range(len(prices)):
    if index == 0:
        prices[index] = prices[index] * 0.9
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    elif index == 1:
        prices[index] = prices[index] * 0.8
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    elif index == 2:
        prices[index] = prices[index] * 0.85
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    else:
        prices[index] = prices[index] * 0.95
        print(f"Updated price for item {index}: ${prices[index]:.2f}")

