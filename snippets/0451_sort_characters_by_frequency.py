import heapq
from collections import Counter


def frequencySort(s: str) -> str:
    result = ""

    # Max Heap
    heap = [(-freq, val) for val, freq in Counter(s).items()]
    heapq.heapify(heap)

    while heap:
        freq, val = heapq.heappop(heap)
        result += val * -freq

    return result


print(frequencySort("tree"))  # eert
