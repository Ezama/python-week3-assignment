# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Check if discount is applicable
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        discounted_price = price - discount 
        # return the discounted price
        return discounted_price
    else:
        # No discount applicable
        return price

# Get user input
price = float(input("Enter price: "))
discount_percent = float(input("Enter discount: "))

# Calculate and print the discounted price
print(calculate_discount(price, discount_percent))