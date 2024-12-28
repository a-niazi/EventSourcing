from application.order_app import OrderApplication

if __name__ == "__main__":
    app = OrderApplication()

    # ایجاد سفارش‌ها
    order1 = app.create_order()
    order2 = app.create_order()

    # افزودن محصولات به سفارش اول
    app.add_item_to_order(order1.id, "Laptop", 1000.0, 1)
    app.add_item_to_order(order1.id, "Mouse", 50.0, 2)
    app.change_order_status(order1.id, "Shipped")

    # افزودن محصولات به سفارش دوم
    app.add_item_to_order(order2.id, "Keyboard", 100.0, 1)
    app.change_order_status(order2.id, "Cancelled")

    # گزارش‌گیری از پروجکشن
    projection = app.get_projection()
    print(f"Total Revenue: {projection.get_total_revenue()}")  # خروجی: 1150.0
    print(f"Shipped Orders: {projection.get_orders_by_status('Shipped')}")  # خروجی: 1
    print(f"Cancelled Orders: {projection.get_orders_by_status('Cancelled')}")  # خروجی: 1