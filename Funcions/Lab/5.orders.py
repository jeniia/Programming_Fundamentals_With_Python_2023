def calculate_total_price(product, quantity):
    product_prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }
    if product in product_prices:
        # Calculate total price
        total_price = product_prices[product] * quantity
        return "{:.2f}".format(total_price)
    else:
        return "Invalid product"


# Example usage
product = input()
quantity = int(input())

# Calculate and print total price
total_price = calculate_total_price(product, quantity)
print(total_price)
