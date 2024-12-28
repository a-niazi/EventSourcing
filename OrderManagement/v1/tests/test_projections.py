import unittest
from OrderManagement.v1.projections.order_projection import OrderProjection
from OrderManagement.v1.aggregates.order import Order


class TestOrderProjection(unittest.TestCase):
    def test_projection_updates(self):
        projection = OrderProjection()
        order = Order()
        order.add_item("Laptop", 1000.0, 1)
        projection.process_event(order)
        self.assertEqual(projection.get_total_revenue(), 1000.0)

    def test_orders_by_status(self):
        projection = OrderProjection()
        order = Order()
        order.change_status("Shipped")
        projection.process_event(order)
        self.assertEqual(projection.get_orders_by_status("Shipped"), 1)


if __name__ == "__main__":
    unittest.main()
