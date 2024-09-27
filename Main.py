from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase

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
            print("TO-DO: Future Feature")

        elif choice == 'r':
            print("TO-DO: Future Feature")

        elif choice == 'c':
            print("TO-DO: Future Feature")

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
    cart = ShoppingCart("John Doe", "February 1, 2020")
    item1 = ItemToPurchase("Nike Romaleos", 189.0, 2, "Volt color, Weightlifting shoes")
    item2 = ItemToPurchase("Chocolate Chips", 3.0, 5, "Semi-sweet")
    item3 = ItemToPurchase("Powerbeats 2 Headphones", 128.0, 1, "Bluetooth headphones")

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    
    print_menu(cart)

if __name__ == "__main__":
    main()
