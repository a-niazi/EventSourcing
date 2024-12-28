# -*- coding: utf-8 -*-
from typing import Any, Dict, cast
from uuid import UUID

from eventsourcing.application import Application

from domainmodel import Order


class OrderApplication(Application):
    def create_order(self) -> UUID:
        order = Order()
        self.save(order)
        return order.id

    def add_item(self, order_id: UUID, item_name: str, price: float, quantity: int) -> None:
        order = cast(Order, self.repository.get(order_id))
        order.add_item(item_name, price, quantity)
        self.save(order)

    def get_order(self, order_id: UUID) -> Dict[str, Any]:
        order = cast(Order, self.repository.get(order_id))
        return {"name": order.status, "items": order.items, "total_price": order.total_price}
