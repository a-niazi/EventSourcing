from infrastructure.event_store import EventStore
from infrastructure.repository import AccountRepository
from service.account_service import AccountService
from service.projection_manager import ProjectionManager
from projections.transaction_projection import TransactionProjection
from projections.top_users_projection import TopUsersProjection


# Setup
store = EventStore()
repository = AccountRepository(store)

projection_manager = ProjectionManager()
transaction_projection = TransactionProjection()
top_users_projection = TopUsersProjection()
projection_manager.register_projection(transaction_projection)
projection_manager.register_projection(top_users_projection)

service = AccountService(repository, projection_manager)

service.create_account(account_id=1)

# Example Usage
service.deposit("acc1", 100)
service.deposit("acc2", 200)
service.withdraw("acc1", 50)

print("Account Summary:")
print(service.get_account_summary("acc1"))

print("Transactions:")
print(transaction_projection.get_transactions())

print("Top Users:")
print(top_users_projection.get_top_users())
