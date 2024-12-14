from application.service import AccountService
from infrastructure.event_store import EventStore

# Create Event Store
event_store = EventStore()

# Create Account Service
account_service = AccountService(event_store)
account_id1 = "acc123"
account_id2 = "acc456"

# Deposit
account_service.deposit(account_id1, 1000)
account_service.deposit(account_id2, 500)
account_service.withdraw(account_id1, 200)
account_service.deposit(account_id1, 2000)

# get monthly reports
print("Monthly Summary:")
print(account_service.get_monthly_summary())

# get top users
print("Top Users:")
print(account_service.get_top_users())

# get total inventory
print("Total Inventory:")
print(account_service.get_total_inventory())
