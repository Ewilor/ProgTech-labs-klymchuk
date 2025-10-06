from helper import OrderManager

def main():
    manager = OrderManager()
    manager.add_order({'id': 1, 'item': 'Laptop'})
    manager.add_order({'id': 2, 'item': 'Phone'})
    manager.add_order_to_front({'id': 3, 'item': 'Tablet'})

    print("All orders:", list(manager.orders))
    print("Removed from end:", manager.remove_order())
    print("Removed from front:", manager.remove_order_from_front())
    try:
        print("Find order by id 2:", manager.find_order_by_id(2))
        print("Find order by id 99:", manager.find_order_by_id(99))
    except LookupError as e:
        print("Error:", e)

main()