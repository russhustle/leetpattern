from collections import defaultdict


# Binary Search
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        self.times = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(timestamp)
        self.times[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        tmp = self.keys[key]

        left, right = 0, len(tmp) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if tmp[mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return self.times[tmp[right]] if right >= 0 else ""


obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))  # bar
print(obj.get("foo", 3))  # bar
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))  # bar2
print(obj.get("foo", 5))  # bar2
