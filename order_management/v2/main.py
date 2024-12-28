import os
# Use SQLite for persistence.
os.environ['PERSISTENCE_MODULE'] = 'eventsourcing.sqlite'
# Configure SQLite database URI. Either use a file-based DB;
os.environ['SQLITE_DBNAME'] = 'sqlite-db'


from application import OrderApplication

order_application = OrderApplication()
order_id = order_application.create_order()
print(f"order_id: {order_id}")

order_application.add_item(order_id, "book1", 20000, 1)
order_application.add_item(order_id, "pen", 1000, 3)
order_application.add_item(order_id, "ruler", 1000, 1)

order_detail = order_application.get_order(order_id)
print(order_detail["items"])
print(order_detail["total_price"])

# notifications = order_application.notification_log.select(
#     start=1, limit=2
# )
# print(notifications[0].topic)
# print(notifications[1].topic)
# notifications = order_application.notification_log.select(
#     start=notifications[0].id+1, limit=2
# )
# print(notifications[0].topic)
# print(notifications[1].topic)

# Projection
order_application.add_item(order_id, "book2", 20000, 1)
order_application.add_item(order_id, "pen2", 1000, 3)
order_application.add_item(order_id, "ruler2", 1000, 1)

order_latest = order_application.repository.get(order_id)
pending_events = order_latest.version == 7
p = 0
