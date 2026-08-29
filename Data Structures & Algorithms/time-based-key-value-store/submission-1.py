import bisect

class TimeMap:
    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyStore.get(key, [])
        if not values:
            return ""
        
        # Search for the timestamp integer directly.
        # bisect_right returns the index where the target would be inserted to the right.
        idx = bisect.bisect_right(values, timestamp, key=lambda x: x[1])
        
        # If idx is 0, all timestamps in the list are strictly greater than the target.
        if idx == 0:
            return ""
            
        # The largest valid timestamp is at idx - 1
        return values[idx - 1][0]