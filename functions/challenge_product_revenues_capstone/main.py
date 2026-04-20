# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

def formatted_output(revenues):
    sorted_revenues = sorted(revenues)
    for item in sorted_revenues:
        print(f"{item[0]} has total revenue of ${item[1]}")
        
revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenues))
formatted_output(revenue_per_product)

# Example of expected output line (do not remove):
print(f"{revenues[0]} has total revenue of ${revenues[1]}")
    