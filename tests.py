import unittest
from helper import OrderManager

class TestOrderManager(unittest.TestCase):
    def setUp(self):
        self.manager = OrderManager()
        self.order1 = {'id': 1, 'item': 'Laptop'}
        self.order2 = {'id': 2, 'item': 'Phone'}

    # add_order
    def test_add_order(self):
        self.manager.add_order(self.order1)
        self.assertIn(self.order1, self.manager.orders)

    def test_add_order_invalid(self):
        with self.assertRaises(ValueError):
            self.manager.add_order({'item': 'Laptop'})

    # add_order_to_front
    def test_add_order_to_front(self):
        self.manager.add_order_to_front(self.order2)
        self.assertEqual(self.manager.orders[0], self.order2)

    def test_add_order_to_front_invalid(self):
        with self.assertRaises(ValueError):
            self.manager.add_order_to_front({'id': 3})

    # remove_order
    def test_remove_order(self):
        self.manager.add_order(self.order1)
        removed = self.manager.remove_order()
        self.assertEqual(removed, self.order1)

    def test_remove_order_empty(self):
        with self.assertRaises(IndexError):
            self.manager.remove_order()

    # remove_order_from_front
    def test_remove_order_from_front(self):
        self.manager.add_order(self.order2)
        removed = self.manager.remove_order_from_front()
        self.assertEqual(removed, self.order2)

    def test_remove_order_from_front_empty(self):
        with self.assertRaises(IndexError):
            self.manager.remove_order_from_front()

    # find_order_by_id
    def test_find_order_by_id(self):
        self.manager.add_order(self.order1)
        found = self.manager.find_order_by_id(1)
        self.assertEqual(found, self.order1)

    @unittest.expectedFailure
    def test_find_order_by_id_not_found(self):
        self.manager.add_order(self.order1)
        self.manager.find_order_by_id(99)

unittest.main()