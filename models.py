class Vehicle:
    def __init__(self, vid, capacity):
        self.id = vid
        self.capacity = capacity

class Delivery:
    def __init__(self, source, destination, priority=1):
        self.source = source
        self.destination = destination
        self.priority = priority
