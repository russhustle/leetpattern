from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.moving = {}
        self.table = defaultdict(lambda: defaultdict(lambda: [0, 0]))
        # table[start][end] = [count, total_time]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.moving[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.moving[id]
        del self.moving[id]

        duration = t - start_time
        count, total = self.table[start_station][stationName]

        self.table[start_station][stationName] = [count + 1, total + duration]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, total = self.table[startStation][endStation]
        return total / count
