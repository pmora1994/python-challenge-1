menu_items = {
1: {"name": "Apple", "price": 0.49},
2: {"name": "Tea - Thai iced", "price": 3.99},
3: {"name": "Fried banana", "price": 4.49}
}

order_list = []

def print_menu():
print("Menu:")
for key, value in menu_items.items():
print(f"{key}. {value['name']} - ${value['price']:.2f}")

def take_order():
while True:
print_menu()
menu_selection = input("Please enter the number of the item you'd like to order: ")

    if not menu_selection.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    
    menu_selection = int(menu_selection)
    if menu_selection not in menu_items:
        print("Invalid selection. Please choose a valid menu item.")
        continue
    
    item_name = menu_items[menu_selection]["name"]
    price = menu_items[menu_selection]["price"]
    
    quantity = input(f"How many {item_name}s would you like to order? (Default is 1 if invalid): ")
    
    if not quantity.isdigit():
        quantity = 1
    else:
        quantity = int(quantity)
    
    order_list.append({"Item name": item_name, "Price": price, "Quantity": quantity})
    
    while True:
        continue_ordering = input("Would you like to order anything else? (y/n): ").lower()
        if continue_ordering == 'y':
            break
        elif continue_ordering == 'n':
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
def print_receipt():
print("\nOrder Receipt")
print("Item name | Price | Quantity")
print("---------------------------|---------|----------")
total_price = 0
for item in order_list:
item_name = item["Item name"]
price = item["Price"]
quantity = item["Quantity"]
item_total = price * quantity
total_price += item_total
print(f"{item_name:<26} | ${price:<6.2f} | {quantity:<8}")
print(f"Total Price: ${total_price:.2f}")

def main():
take_order()
print("Thank you for your order.")
print_receipt()

if name == "main":
main()
