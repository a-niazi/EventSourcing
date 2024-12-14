from domain.aggregates import AccountAggregate

class AccountRepository:
    def __init__(self, event_store):
        self.event_store = event_store

    def load(self, account_id):
        aggregate = AccountAggregate(account_id)
        events = self.event_store.get_events(account_id)
        for event in events:
            aggregate.apply(event)
        return aggregate

    def save(self, event):
        self.event_store.append(event)
