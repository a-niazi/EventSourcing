import json


class EventSerializer:
    @staticmethod
    def serialize(event):
        return json.dumps(event.__dict__)

    @staticmethod
    def deserialize(event_data, event_type):
        return event_type(**json.loads(event_data))