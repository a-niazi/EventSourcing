from eventsourcing.application import Application
from order_management.v1.aggregates.order import Order
from order_management.v1.projections.order_projection import OrderProjection


class OrderApplication(Application):
    def __init__(self):
        super().__init__()
        self.projection = OrderProjection()

    def create_order(self) -> Order:
        order = Order()
        self.save(order)
        return order

    def add_item_to_order(self, order_id: str, item_name: str, price: float, quantity: int):
        order = self.repository.get(order_id)
        order.add_item(item_name, price, quantity)
        self.save(order)
        self.projection.process_event(order)

    def change_order_status(self, order_id: str, status: str):
        order = self.repository.get(order_id)
        order.change_status(status)
        self.save(order)
        self.projection.process_event(order)

    def get_projection(self) -> OrderProjection:
        return self.projection