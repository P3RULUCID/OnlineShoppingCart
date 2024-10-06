from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                print(f"{item_name} has been removed from cart")
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item: ItemToPurchase):
        item_found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                item_found = True              
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description          
                print(f"{modified_item.item_name} has been updated.")
                break           
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            total_items = self.get_num_items_in_cart()
            print(f"Number of Items: {total_items}")
            for item in self.cart_items:
                item.print_item_cost()
            total_cost = self.get_cost_of_cart()
            print(f"\nTotal: ${total_cost:.2f}")

    def print_descriptions(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")
