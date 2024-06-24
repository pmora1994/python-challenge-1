menu_items = {
    1: {"name": "Apple", 
        "price": 0.49,
        "quantity": int},
    2: {"name": "Tea - Thai iced", 
        "price": 2.95,
        "quantity": int},
    3: {"name": "Fried banana", 
        "price": 1.50,
        "quantity": int}
}

order_menu = []

def print_menu(menu_items):
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['name']} - ${value['price']:.2f}")

def take_order(menu_items):
    while True:
        print_menu(menu_items)
        menu_selection = input("Enter the number of the item you'd like to order: ")
        
        menu_selection = int(menu_selection)
        if menu_selection not in menu_items:
            print("Invalid selection. Choose a valid menu item.")
            continue
        
        item_name = menu_items[menu_selection]["name"]
        price = menu_items[menu_selection]["price"]
        
        quantity = input(f"How many {item_name}s would you like to order? (Default is 1 if invalid): ")

        try:
            quantity = int(quantity)
        except ValueError:
            quantity = 1
        
        order_menu.append({"Item name": item_name, "Price": price, "Quantity": quantity})
        
        while True:
            place_order = input("Would you like to order anything else? (y/n): ").lower()
            if place_order  == 'y':
                break
            elif place_order  == 'n':
                return
            else:
                print("Invalid input. Enter 'y' or 'n'.")

def print_receipt():
    print("Item name                  | Price   | Quantity")
    print()
    print("---------------------------|---------|----------")
    print()

    total_price = 0
    for item in order_menu:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        item_total = price * quantity
        total_price += item_total
        print(f"{item_name:<26} | ${price:<6.2f} | {quantity:<8}")
        print()

    print(f"Total Price: ${total_price:.2f}")

def main():
    take_order(menu_items)
    print_receipt()

take_order(menu_items)
print_receipt()
