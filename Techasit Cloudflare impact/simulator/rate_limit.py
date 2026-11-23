import time

class RateLimiter:
    def __init__(self, limit=100, window=10):
        self.limit = limit
        self.window = window
        self.events = {}

    def allow(self, client_id):
        now = time.time()
        events = [t for t in self.events.get(client_id, []) if now - t < self.window]
        if len(events) >= self.limit:
            self.events[client_id] = events
            return False
        events.append(now)
        self.events[client_id] = events
        return True
