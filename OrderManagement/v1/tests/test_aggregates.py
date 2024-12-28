import unittest
from OrderManagement.v1.aggregates.order import Order

class TestOrderAggregate(unittest.TestCase):
    def test_add_item(self):
        order = Order()
        order.add_item("Laptop", 1000.0, 1)
        self.assertEqual(order.total_price, 1000.0)
        self.assertEqual(len(order.items), 1)

    def test_change_status(self):
        order = Order()
        order.change_status("Shipped")
        self.assertEqual(order.status, "Shipped")

if __name__ == "__main__":
    unittest.main()