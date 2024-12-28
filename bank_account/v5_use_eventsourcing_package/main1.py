# import os
# # Use SQLite for persistence.
# os.environ['PERSISTENCE_MODULE'] = 'eventsourcing.sqlite'
# # Configure SQLite database URI. Either use a file-based DB;
# os.environ['SQLITE_DBNAME'] = 'EventStore'

from bank_account.v5_use_eventsourcing_package.application.account import AccountApplication
from bank_account.v5_use_eventsourcing_package.projections.total_balance_projection import BalanceProjection

app = AccountApplication() #env={"IS_SNAPSHOTTING_ENABLED": "y"})

account1 = app.create_account("amir1")
account2 = app.create_account("ali1")
p = account1.collect_events()
events = account1.collect_events()

app.deposit(account1.id, 1000)
app.deposit(account2.id, 1500)
app.withdraw(account1.id, 300)


# dd = app.take_snapshot(account1.id)
# snapshots = app.snapshots.get(account1.id, desc=True, limit=10)
# snapshots = list(snapshots)
# assert snapshots[0].originator_id == account1.id
# assert snapshots[0].originator_version == 4



# tbp = BalanceProjection()
#
# for event in app.repository.event_store.get(account1.id):
#     tbp.process_event(event)
#
#
# print(f"Total Balance: {tbp.total_balance}")
# print(f"Total Balance: {tbp.account_balances}")

print(f"Total Balance: {app.balance_projection.total_balance}")
print(f"Total Balance: {app.balance_projection.account_balances}")
