from eventsourcing.domain import Aggregate, event


class BaseAggregate(Aggregate):
    def __init__(self):
        self._version = 0

    def increment_version(self):
        self._version += 1

    @property
    def version(self):
        return self._version
