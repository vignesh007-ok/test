def calculate_bill(price, quantity):
    if price < 0 or quantity <= 0:
        raise ValueError("Invalid price or quantity input.")
    return price * quantity

def shopping_bill_calculator():
    print("--- Shopping Bill Application ---")
    try:
        price = float(input("Enter the item's unit price: "))
        quantity = int(input("Enter the quantity: "))
        
        total = calculate_bill(price, quantity)
        print(f"\nTotal Bill: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    shopping_bill_calculator()
