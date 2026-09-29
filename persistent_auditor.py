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



orders = load_inventory()

print(orders)



