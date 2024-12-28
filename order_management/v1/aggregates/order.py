from .base import BaseAggregate
from .exception import InvalidOperationError


class Order(BaseAggregate):
    def __init__(self):
        super().__init__()
        self.items = []
        self.status = "Pending"
        self.total_price = 0.0

    def add_item(self, item_name: str, price: float, quantity: int):
        if quantity <= 0 or price <= 0:
            raise InvalidOperationError("Price and quantity must be positive.")
        self.items.append({"item_name": item_name, "price": price, "quantity": quantity})
        self.total_price += price * quantity
        self.increment_version()

    def change_status(self, status: str):
        if status not in ["Pending", "Shipped", "Cancelled"]:
            raise InvalidOperationError(f"status '{status}' is not valid.")
        self.status = status
        self.increment_version()

