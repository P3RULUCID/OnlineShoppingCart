from InputCheck import int_input, float_input, non_empty_input

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def input_item_details(self):
        self.item_name = non_empty_input("Enter the item name:\n")
        self.item_price = float_input("Enter the item price:\n")
        self.item_quantity = int_input("Enter the item quantity:\n")
        self.item_description = non_empty_input("Enter the item description:\n")

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name:<20} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
