from ItemToPurchase import ItemToPurchase
from InputCheck import int_input

def main():
    num_items = int_input("How many items do you want to enter?\n")
    items = []

    for i in range(num_items):
        print(f"Item {i+1}")
        item = ItemToPurchase()
        item.input_item_details()
        items.append(item)
        print()

    print("TOTAL COST")
    total_cost = 0
    for item in items:
        item.print_item_cost()
        total_cost += item.item_price * item.item_quantity

    print(f"\nTotal: ${total_cost:.2f}")

if __name__ == "__main__":
    main()

