from typing import List


# Simulation
def distanceBetweenBusStops(distance: List[int], start: int, destination: int) -> int:
    if start > destination:
        start, destination = destination, start

    clock = sum(distance[start:destination])
    counter = sum(distance) - clock

    return min(clock, counter)


distance = [1, 2, 3, 4]
start = 0
destination = 1
print(distanceBetweenBusStops(distance, start, destination))  # 1
