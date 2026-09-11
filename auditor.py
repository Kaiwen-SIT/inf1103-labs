inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock.lower() == "quit":
        break


    if not stock.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    stock = int(stock)

    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue

    inventory += stock
    print(f"Stock added. Current inventory: {inventory}")

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break

print("\n--- Inventory Report ---")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")