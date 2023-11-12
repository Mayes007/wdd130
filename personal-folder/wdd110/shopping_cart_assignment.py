#Python

# Initialize empty list to store the names of items in the shopping cart
shopping_cart = []

# Function to display the menu
def display_menu():
    print("\nWelcome to the Shopping Cart Program!")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

# Function to add an item to the shopping cart
def add_item():
    item_name = input("What item would you like to add? ")
    shopping_cart.append(item_name)
    print(f"'{item_name}' has been added to the cart.")

# Function to display the contents of the shopping cart
def view_cart():
    print("\nThe contents of the shopping cart are:")
    for i, item in enumerate(shopping_cart, start=1):
        print(f"{i}. {item}")

# Main program loop
while True:
    display_menu()
    choice = input("Please enter an action: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        view_cart()
    elif choice == '5':
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")