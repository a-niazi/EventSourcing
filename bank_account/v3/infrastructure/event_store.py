# infrastructure/event_store.py
class EventStore:
    def __init__(self):
        self.events = []

    def append(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events

    def get_events_by_account_id(self, account_id):
        return [event for event in self.events if getattr(event, 'entity_id', None) == account_id]