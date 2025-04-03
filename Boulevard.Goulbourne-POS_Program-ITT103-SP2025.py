import datetime

# Supermarket details
STORE_NAME = "B&K New Era Supermarket"
STORE_ADDRESS = "114 Brunswick Avenue, Spanish Town, St. Catherine"

# Product catalog (dictionary with item name, price, and stock)
products = {
    "Milk": [150, 10],
    "Bread": [120, 15],
    "Rice": [800, 8],
    "Sugar": [200, 12],
    "Eggs": [500, 5],
    "Chicken": [1000, 4],
    "Soap": [90, 20],
    "Shampoo": [300, 7],
    "Toothpaste": [250, 10],
    "Water": [100, 25]
}

cart = {}
SALES_TAX = 0.10
DISCOUNT_THRESHOLD = 5000
DISCOUNT_RATE = 0.05

def display_products():
    print("\nAvailable Products:")
    for item, details in products.items():
        print(f"{item}: ${details[0]} - Stock: {details[1]}")

def add_to_cart():
    item = input("Enter product name: ").strip()
    if item in products:
        qty = int(input("Enter quantity: "))
        if qty > products[item][1]:
            print("Insufficient stock!")
        else:
            cart[item] = cart.get(item, 0) + qty
            products[item][1] -= qty
            print(f"{qty} {item}(s) added to cart.")
    else:
        print("Product not found!")

def remove_from_cart():
    item = input("Enter product name to remove: ").strip()
    if item in cart:
        qty_to_remove = int(input(f"Enter quantity to remove (max {cart[item]}): "))
        if qty_to_remove >= cart[item]:
            products[item][1] += cart[item]
            del cart[item]
            print(f"Removed {item} from cart.")
        else:
            cart[item] -= qty_to_remove
            products[item][1] += qty_to_remove
            print(f"Removed {qty_to_remove} of {item} from cart.")
    else:
        print("Item not in cart!")

def view_cart():
    print("\nYour Cart:")
    total = 0
    for item, qty in cart.items():
        price = products[item][0] * qty
        print(f"{item}: {qty} x ${products[item][0]} = ${price}")
        total += price
    print(f"Subtotal: ${total}")

def checkout():
    while True:
        subtotal = sum(products[item][0] * qty for item, qty in cart.items())
        tax = subtotal * SALES_TAX
        total_due = subtotal + tax
        discount = 0
        if subtotal > DISCOUNT_THRESHOLD:
            discount = subtotal * DISCOUNT_RATE
            total_due -= discount

        print(f"Subtotal: ${subtotal}")
        print(f"Tax (10%): ${tax}")
        print(f"Discount: ${discount}")
        print(f"Total Due: ${total_due}")

        payment = float(input("Enter payment amount: "))
        if payment >= total_due:
            change = payment - total_due
            print(f"Payment accepted. Change: ${change}")
            generate_receipt(subtotal, tax, discount, total_due, payment, change)
            cart.clear()
            break
        else:
            print("Insufficient payment. You can remove items to lower the cost.")
            view_cart()
            remove_from_cart()
            # Recalculate total after removal
            subtotal = sum(products[item][0] * qty for item, qty in cart.items())
            tax = subtotal * SALES_TAX
            total_due = subtotal + tax - discount
            if payment >= total_due:
                change = payment - total_due
                print(f"Payment accepted. Change: ${change}")
                generate_receipt(subtotal, tax, discount, total_due, payment, change)
                cart.clear()
                break

def generate_receipt(subtotal, tax, discount, total_due, payment, change):
    print("\n=== B&K New Era Supermarket ===")
    print(f"{STORE_NAME}\n{STORE_ADDRESS}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("---------------------------------")
    for item, qty in cart.items():
        print(f"{item} x{qty} @ ${products[item][0]} = ${products[item][0] * qty}")
    print("---------------------------------")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Discount: ${discount}")
    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${payment}")
    print(f"Change: ${change}")
    print("Thank you for shopping at B&K New Era Supermarket!\n")

def main():
    while True:
        print("\n1. View Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Exiting...\n")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
