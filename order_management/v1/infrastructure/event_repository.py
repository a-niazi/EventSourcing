from .repository import RepositoryInterface


class EventRepository(RepositoryInterface):
    def __init__(self, application):
        self.application = application

    def save(self, aggregate):
        self.application.save(aggregate)

    def get(self, aggregate_id: str):
        return self.application.repository.get(aggregate_id)

    def delete(self, aggregate_id: str):
        aggregate = self.get(aggregate_id)
        aggregate._trigger_event("Deleted")
        self.save(aggregate)
