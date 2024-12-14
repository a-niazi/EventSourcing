class EventStore:
    def __init__(self):
        self.store = []

    def append(self, event):
        self.store.append(event)

    def get_events(self, account_id=None):
        if account_id:
            return [event for event in self.store if event.account_id == account_id]
        return self.store
