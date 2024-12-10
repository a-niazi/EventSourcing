class EventStore:
	def __init__(self):
		self.store = {}

	def save(self, aggregate_id, events):
		if aggregate_id not in self.store:
			self.store[aggregate_id] = []
		self.store[aggregate_id].extend(events)

	def get_events(self, aggregate_id):
		return self.store.get(aggregate_id, [])
