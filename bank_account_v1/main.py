from aggregates.account import Account
from infrastructure.event_store import EventStore
from events.account_events import DepositMade, WithdrawalMade, AccountBlocked

# ایجاد EventStore
event_store = EventStore()

# ایجاد حساب
account_id = "acc123"
account = Account(account_id)


# واریز 1000 دلار به حساب
event1 = account.deposit(1000)
event_store.save(account.account_id, [event1])

# برداشت 500 دلار از حساب
event2 = account.withdraw(500)
event_store.save(account.account_id, [event2])

# مسدود کردن حساب
event3 = account.block_account()
event_store.save(account.account_id, [event3])

# بازسازی وضعیت حساب
restored_account = Account.reconstruct(account_id, event_store)

# مشاهده وضعیت حساب
print(f"Account ID: {restored_account.account_id}")
print(f"Balance: {restored_account.balance}")
print(f"Blocked: {restored_account.blocked}")