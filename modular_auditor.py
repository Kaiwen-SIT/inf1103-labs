def get_valid_input():
    while True:
        stock = input("Enter stock quantity (or 'quit' to exit): ")

        if stock.lower() == "quit":
            return "quit"

        if not stock.isdigit():
            print("Error: Please enter a valid integer.")
            return None

        stock = int(stock)

        if stock < 0:
            print("Error: Stock quantity cannot be negative.")
            return None

        return stock


def process_delivery(current_total, new_value):
    return current_total + new_value


def generate_report(total_units, failed_attempts):
    print("\n--- Inventory Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

inventory = 0
failed_entries = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        break

    if stock is None:
        failed_entries += 1
        continue

    tax = calculate_tax(stock)
    inventory = process_delivery(inventory, stock)

    print(f"Stock added. Current inventory: {inventory}")

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break

generate_report(inventory, failed_entries)