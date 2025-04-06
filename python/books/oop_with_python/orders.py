from __future__ import annotations


class Customer:
    def __init__(self, name: str, email: str):
        self.name: str = name
        self.email: str = email
        self.orders: list['Order'] = []

    def add_order(self, order: Order) -> None:
        self.orders.append(order)


class Order:
    def __init__(self, order_id: int, products: list[str]):
        self.order_id: int = order_id
        self.products: list[str] = products


# Usage:
customer1 = Customer('John Doe', 'john@example.com')
order1 = Order(1, ['Product1', 'Product2'])
customer1.add_order(order1)
