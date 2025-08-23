# cc_order_queue.py

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor.")
            return
        if scoops < 1 or scoops > 3:
            print("Choose between 1-3 scoops.")
            return
        print("Order created!")
        order = {
            "customer": customer,
            "flavor": flavor,
            "scoops": scoops
        }
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for order in self.orders:
            print(f"Customer: {order['customer']}, Flavor: {order['flavor']}, Scoops: {order['scoops']}")

    def next_order(self):
        print("\nNext Order Up!")
        order = self.orders.dequeue()
        if order:
            print(f"Customer: {order['customer']}, Flavor: {order['flavor']}, Scoops: {order['scoops']}")
        else:
            print("No more orders!")


# Testing
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
