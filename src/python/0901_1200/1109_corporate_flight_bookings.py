"""
-   Return the number of seats booked on each flight.
"""

from typing import List


# Difference Array
def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    """Return the number of seats booked for each flight."""
    res = [0 for _ in range(n)]

    for i, j, k in bookings:
        res[i - 1] += k
        if j < n:
            res[j] -= k

    for i in range(1, n):
        res[i] += res[i - 1]

    return res


bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
print(corpFlightBookings(bookings, n))  # [10, 55, 45, 25, 25]
