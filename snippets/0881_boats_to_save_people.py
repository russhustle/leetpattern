from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats


people = [3, 2, 2, 1]
limit = 3
print(numRescueBoats(people, limit))
