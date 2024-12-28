from collections import defaultdict


class OrderProjection:
    def __init__(self):
        self.orders = {}
        self.total_revenue = 0.0
        self.orders_by_status = defaultdict(int)

    def process_event(self, order):
        self.orders[order.id] = {
            "items": order.items,
            "total_price": order.total_price,
            "status": order.status,
        }
        self._update_statistics()

    def _update_statistics(self):
        self.total_revenue = sum(order["total_price"] for order in self.orders.values())
        self.orders_by_status = defaultdict(int)
        for order in self.orders.values():
            self.orders_by_status[order["status"]] += 1

    def get_total_revenue(self):
        return self.total_revenue

    def get_orders_by_status(self, status):
        return self.orders_by_status[status]