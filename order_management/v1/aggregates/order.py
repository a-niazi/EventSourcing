from .base import BaseAggregate
from .exception import InvalidOperationError


class Order(BaseAggregate):
    """
    مدیریت وضعیت سفارش و عملیات آن.
    """

    def __init__(self):
        super().__init__()
        self.items = []
        self.status = "Pending"
        self.total_price = 0.0

    def add_item(self, item_name: str, price: float, quantity: int):
        if quantity <= 0 or price <= 0:
            raise InvalidOperationError("قیمت و تعداد باید مثبت باشند.")
        self.items.append({"item_name": item_name, "price": price, "quantity": quantity})
        self.total_price += price * quantity
        self.increment_version()

    def change_status(self, status: str):
        if status not in ["Pending", "Shipped", "Cancelled"]:
            raise InvalidOperationError(f"وضعیت '{status}' نامعتبر است.")
        self.status = status
        self.increment_version()

