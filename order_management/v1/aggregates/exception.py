class AggregateError(Exception):
    pass


class InvalidOperationError(AggregateError):
    pass
