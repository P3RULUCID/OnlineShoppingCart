from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
from InputCheck import non_empty_input, validate_date_input, int_input

def print_menu(cart: ShoppingCart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("Choose an option: ", end="")
        choice = input().strip().lower()
        
        if choice == 'a':
            item = ItemToPurchase()
            item.input_item_details()
            cart.add_item(item)
            print(f"{item.item_name} has been added to the cart.")

        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            cart.remove_item(item_name)

        elif choice == 'c':
            item_name = non_empty_input("Enter the item name to change: ")
            modified_item = ItemToPurchase(item_name=item_name)
            new_quantity = int_input("Enter the new quantity: ")
            modified_item.item_quantity = new_quantity
            cart.modify_item(modified_item)

        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'q':
            print("Thank you for using the shopping cart program!")
            break

        else:
            print("Invalid choice. Please try again.")
            
def main():
    customer_name = non_empty_input("Provide Customer Name:\n")
    current_date = validate_date_input("Enter a date (e.g., February 1, 2020): ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()
