from typing import List


# Greedy
def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()
    moves = 0

    for i, j in zip(seats, students):
        moves += abs(i - j)

    return moves


print(minMovesToSeat([3, 1, 5], [2, 7, 4]))  # 4
