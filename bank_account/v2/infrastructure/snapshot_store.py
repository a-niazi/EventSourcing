class SnapshotStore:
    def __init__(self):
        self.snapshots = {}

    def save_snapshot(self, aggregate_id, snapshot):
        self.snapshots[aggregate_id] = snapshot

    def get_snapshot(self, aggregate_id):
        return self.snapshots.get(aggregate_id, None)
