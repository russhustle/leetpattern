from collections import defaultdict, deque
from typing import List


# BFS
def numBusesToDestination(
    routes: List[List[int]], source: int, target: int
) -> int:
    if source == target:
        return 0

    graph = defaultdict(set)  # {stop: buses}
    for buses, route in enumerate(routes):
        for stop in route:
            graph[stop].add(buses)

    q = deque([(source, 0)])  # (stop, bus)
    visited_stops = set([source])
    visited_buses = set()

    while q:
        stop, bus = q.popleft()

        if stop == target:
            return bus

        for buses in graph[stop]:
            if buses not in visited_buses:
                visited_buses.add(buses)
                for next_stop in routes[buses]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, bus + 1))

    return -1


routes = [[1, 2, 7], [3, 6, 7]]
source = 1
target = 6
print(numBusesToDestination(routes, source, target))  # 2
