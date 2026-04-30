from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.m[key]
        for i in range(len(values)-1, -1, -1):
            if values[i][1] <= timestamp:
                return values[i][0]
        return ""

