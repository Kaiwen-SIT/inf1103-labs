import os

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            orders = []

            for line in file:
                line = line.strip()

                if not line:
                    continue

                line = line.strip("()")
                order_id, product_name, quantity = line.split(",")

                order_id = int(order_id.strip())
                product_name = product_name.strip().strip("'\"")
                quantity = int(quantity.strip())

                orders.append((order_id, product_name, quantity))

            return orders

    except FileNotFoundError:
        return []


def save_inventory(orders):
    with open("inventory.txt", "w") as file:
        for order in orders:
            file.write(f"({order[0]}, '{order[1]}', {order[2]})\n")


def display_orders(orders):
    print("\nCurrent Orders:\n")

    if not orders:
        print("No orders available.")
    else:
        for order in orders:
            print(f"{order[0]}, {order[1]}, {order[2]}")

    print()


def add_order(orders):
    while True:
        product_name = input("Enter Product Name: ")

        if product_name.lower() == "quit":
            return False

        if product_name.strip() == "":
            print("Product name cannot be empty.")
            continue

        break

    while True:
        quantity_input = input("Enter Quantity: ")

        if quantity_input.lower() == "quit":
            return False

        try:
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    if len(orders) == 0:
        order_id = 1001
    else:
        order_id = orders[-1][0] + 1

    new_order = (order_id, product_name, quantity)
    orders.append(new_order)

    print("\nNew Order Added:")
    print(f"{order_id}, {product_name}, {quantity}")


orders = load_inventory()

display_orders(orders)

add_order(orders)

save_inventory(orders)

print("\nInventory successfully saved to inventory.txt")

