class AggregateError(Exception):
    """خطای عمومی برای Aggregate‌ها."""
    pass


class InvalidOperationError(AggregateError):
    """وقتی عملیات نامعتبر روی Aggregate انجام شود."""
    pass