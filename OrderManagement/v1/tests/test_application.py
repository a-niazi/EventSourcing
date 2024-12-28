import unittest
from OrderManagement.v1.application.order_app import OrderApplication

class TestOrderApplication(unittest.TestCase):
    def setUp(self):
        self.app = OrderApplication()

    def test_create_order(self):
        order = self.app.create_order()
        self.assertIsNotNone(order.id)

    def test_add_item_to_order(self):
        order = self.app.create_order()
        self.app.add_item_to_order(order.id, "Laptop", 1000.0, 1)
        updated_order = self.app.repository.get(order.id)
        self.assertEqual(updated_order.total_price, 1000.0)

    def test_change_order_status(self):
        order = self.app.create_order()
        self.app.change_order_status(order.id, "Shipped")
        updated_order = self.app.repository.get(order.id)
        self.assertEqual(updated_order.status, "Shipped")

if __name__ == "__main__":
    unittest.main()