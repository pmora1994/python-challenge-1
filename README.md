# python-challenge-1

Here is my work for this second module.
This was a fun project to go over since it tested my knowledge on the fundamentals of python and on lists and definitions and using them in small loop settings.

# Here is a list of menu items I used from the format given to us in the instructions

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

# Here is a an empty list to store the order given to us

order_menu = []

# The following function displays the menu in the terminal

def print_menu(menu_items):
    print("Menu:")
    for key, value in menu_items.items():
        print(f"{key}. {value['name']} - ${value['price']:.2f}")

# The following is a function to take an keep track of an order

def take_order(menu_items):
    while True:
        print_menu(menu_items)
        menu_selection = input("Enter the number of the item you'd like to order: ")

# The following is for proper validation of statements given
## The try-except inputs is what I learned from w3schools (https://www.w3schools.com/python/python_try_except.asp, viewed 6/20/2024)
        
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

# Printing receipt and the format shown is what given to us on the module instructions

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
