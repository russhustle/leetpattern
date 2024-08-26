import heapq


def nthUglyNumber(n: int) -> int:
    heap = [1]
    seen = set(heap)

    factors = [2, 3, 5]
    current = 1

    # Pop the smallest ugly number n times
    for _ in range(n):
        current = heapq.heappop(heap)  # Pop the smallest ugly number

        for factor in factors:
            new = current * factor
            if new not in seen:
                seen.add(new)
                heapq.heappush(heap, new)

    return current


print(nthUglyNumber(10))  # 12
