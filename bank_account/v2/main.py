from aggregates.account import Account
from infrastructure.event_store import EventStore
from infrastructure.snapshot_store import SnapshotStore
from projections import TopUsersProjection, \
	TransactionSummaryProjection, \
	MonthlyTransactionSummaryProjection, \
	TransactionTypePercentageProjection, \
	TotalInventoryProjection


# Create EventStore
event_store = EventStore()
snapshot_store = SnapshotStore()

# Create Account
account_id = "acc123"
account = Account(account_id)

projection = TransactionSummaryProjection()

# Deposit $1,000 into the account
event1 = account.deposit(1000)
event_store.save(account.account_id, [event1])
projection.apply(event1)

# Deposit $500 into the account
event2 = account.deposit(500)
event_store.save(account.account_id, [event2])
projection.apply(event2)

# Withdraw $500 from account
event3 = account.withdraw(1000)
event_store.save(account.account_id, [event3])
projection.apply(event3)

# Deposit $100 into the account
event4 = account.deposit(100)
event_store.save(account.account_id, [event4])
projection.apply(event4)

# Block account
event5 = account.block_account()
event_store.save(account.account_id, [event5])
projection.apply(event5)

#create snapshot
snapshot = account.create_snapshot()
snapshot_store.save_snapshot(account.account_id, snapshot)

# * * * * * * * * * * * * * *
# Reconstruct account status
# * * * * * * * * * * * * * *
restored_account = Account.reconstruct_from_snapshot(snapshot, event_store)

# View account status
print("account status:")
print(f"Account ID: {restored_account.account_id}")
print(f"Balance: {restored_account.balance}")
print(f"Blocked: {restored_account.blocked}")

# projection view
summary = projection.get_summary()
print("\nTransaction Summary:")
print(f"Total Deposits: {summary['total_deposits']}")
print(f"Total Withdrawals: {summary['total_withdrawals']}")
print(f"Transaction Count: {summary['transaction_count']}")


# * * * * * * * * * *
# Monthly Projection
# * * * * * * * * * *
monthly_projection = MonthlyTransactionSummaryProjection()

monthly_projection.apply(event1)
monthly_projection.apply(event2)
monthly_projection.apply(event3)
monthly_projection.apply(event4)
monthly_projection.apply(event5)

print("\nonthly Transaction Summary:")
print(monthly_projection.get_monthly_summary())


# * * * * * * * * * *
# Top User Projection
# * * * * * * * * * *
top_users_projection = TopUsersProjection()

top_users_projection.apply(event1, account_id)
top_users_projection.apply(event2, account_id)
top_users_projection.apply(event3, account_id)
top_users_projection.apply(event4, account_id)
top_users_projection.apply(event5, account_id)

print("\nTop Users:")
print(top_users_projection.get_top_users())


# * * * * * * * * * * * * * * * * * * * *
# Transaction Type Percentage Projection
# * * * * * * * * * * * * * * * * * * * *
type_percentage_projection = TransactionTypePercentageProjection()

type_percentage_projection.apply(event1)
type_percentage_projection.apply(event2)
type_percentage_projection.apply(event3)
type_percentage_projection.apply(event4)


print("\nTransaction Type Percentages:")
print(type_percentage_projection.get_type_percentage())


# * * * * * * * * * * * * * * * * * * * *
# Total Inventory Projection
# * * * * * * * * * * * * * * * * * * * *
total_inventory = TotalInventoryProjection()

total_inventory.apply(event1)
total_inventory.apply(event2)
total_inventory.apply(event3)
total_inventory.apply(event4)

print(f'Total Inventory: {total_inventory.get_total_inventory()}')
