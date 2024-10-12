# Function to display the menu
def display_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $3.75")
    print("3. Nachos - $4.00")
    print("4. Soft Drink - $1.25")
    print("5. Quit\n")


def taco_tuesday_order_system():
    print("Welcome to Taco Palace! Please view the menu below and enter the number that represents your selection.")

    menu_items = ["Taco", "Burrito", "Nachos", "Soft Drink"]
    prices = [2.50, 3.75, 4.00, 1.25]

    order_list = []
    total_amount = 0

    while True:
        display_menu()

        user_input = input("Enter your selection: ")

        if user_input.isdigit():
            selection = int(user_input)  # Convert to integer

            if selection == 5:  # Quit option
                break

            if 1 <= selection <= 4:
                item_name = menu_items[selection - 1]
                price = prices[selection - 1]
                print("You selected a {item_name}.")
                order_list.append(item_name)
                total_amount += price
            else:
                print("Invalid selection. Please enter a number between 1 and 5.")
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

    if order_list:
        print(f"\nYou ordered: {', '.join(order_list)}.")
        print(f"Your total is: ${total_amount:.2f}.")
    else:
        print("\nYou did not order anything.")



taco_tuesday_order_system()