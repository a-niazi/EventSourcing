from bank_account.v1.aggregates.account import Account
from bank_account.v1.infrastructure.event_store import EventStore

# Create EventStore
event_store = EventStore()

# Create Account
account_id = "acc123"
account = Account(account_id)


# Deposit $1,000 into the account
event1 = account.deposit(1000)
event_store.save(account.account_id, [event1])

# Withdraw $500 from account
event2 = account.withdraw(500)
event_store.save(account.account_id, [event2])

# Block account
event3 = account.block_account()
event_store.save(account.account_id, [event3])

# Reconstruct account status
restored_account = Account.reconstruct(account_id, event_store)

# View account status
print(f"Account ID: {restored_account.account_id}")
print(f"Balance: {restored_account.balance}")
print(f"Blocked: {restored_account.blocked}")