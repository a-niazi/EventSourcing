from eventsourcing.persistence import SQLiteDatastore
from eventsourcing.application import EventSourcedApplication


class EventStore:
    def __init__(self, db_path=":memory:"):
        self.datastore = SQLiteDatastore(db_path)

    def get_application(self):
        return EventSourcedApplication(datastore=self.datastore)
