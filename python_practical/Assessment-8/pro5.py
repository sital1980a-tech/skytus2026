products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Headphones", "price": 2000},
    3: {"name": "Mouse", "price": 500},
    4: {"name": "Keyboard", "price": 1500}
}

cart = {}

def show_products():
    print("\n--- Available Products ---")
    for pid, item in products.items():
        print(f"{pid}. {item['name']} - ₹{item['price']}")

def add_to_cart():
    show_products()
    pid = int(input("Enter product ID to add: "))
    qty = int(input("Enter quantity: "))

    if pid in products:
        if pid in cart:
            cart[pid]["qty"] += qty
        else:
            cart[pid] = {
                "name": products[pid]["name"],
                "price": products[pid]["price"],
                "qty": qty
            }
        print("Item added to cart ✅")
    else:
        print("Invalid product ID ❌")

def view_cart():
    if not cart:
        print("\nCart is empty.")
        return

    print("\n--- Your Cart ---")
    total = 0
    for item in cart.values():
        cost = item["price"] * item["qty"]
        total += cost
        print(f"{item['name']} x {item['qty']} = ₹{cost}")

    print("Total Amount: ₹", total)

def remove_item():
    pid = int(input("Enter product ID to remove: "))
    if pid in cart:
        del cart[pid]
        print("Item removed ❌")
    else:
        print("Item not found in cart.")

def checkout():
    view_cart()
    if cart:
        print("\nOrder placed successfully 🎉")
        cart.clear()

def main():
    while True:
        print("\n=== E-Commerce Cart ===")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove Item")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Thank you for shopping! 👋")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
