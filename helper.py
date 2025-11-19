from collections import deque

class OrderManager:
    def __init__(self):
        self.orders = deque()

    def add_order(self, order):
        if not isinstance(order, dict) or 'id' not in order or 'item' not in order:
            raise ValueError("Order must be a dict with 'id' and 'item'")
        self.orders.append(order)

    def add_order_to_front(self, order):
        if not isinstance(order, dict) or 'id' not in order or 'item' not in order:
            raise ValueError("Order must be a dict with 'id' and 'item'")
        self.orders.appendleft(order)

    def remove_order(self):
        if not self.orders:
            raise IndexError("No orders to remove")
        return self.orders.pop()

    def remove_order_from_front(self):
        if not self.orders:
            raise IndexError("No orders to remove")
        return self.orders.popleft()

    def find_order_by_id(self, order_id):
        for order in self.orders:
            if order['id'] == order_id:
                return order
        raise LookupError("Order not found")
