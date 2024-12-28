from eventsourcing.system import ProcessEvent

class TotalDepositsProjection:
    def __init__(self):
        self.total_deposits = 0.0

    def process_event(self, event: ProcessEvent):
        # Process only Deposit events
        if isinstance(event, MoneyDeposited):
            self.total_deposits += event.amount

    def get_total_deposits(self):
        return self.total_deposits