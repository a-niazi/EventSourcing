from eventsourcing.domain import Aggregate, event


class BaseAggregate(Aggregate):
    def __init__(self):
        self._version = 0  # نسخه فعلی Aggregate

    def increment_version(self):
        """افزایش نسخه Aggregate پس از اعمال هر رویداد."""
        self._version += 1

    @property
    def version(self):
        """برگرداندن نسخه فعلی Aggregate."""
        return self._version