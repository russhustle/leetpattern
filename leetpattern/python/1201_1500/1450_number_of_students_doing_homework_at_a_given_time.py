from typing import List


# Brute Force
def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    num = 0
    for i, j in zip(startTime, endTime):
        if i <= queryTime <= j:
            num += 1

    return num


# |----------|---------|----------|
# | Approach |  Time   |  Space   |
# |----------|---------|----------|
# |   BF     |  O(n)   |  O(1)    |
# |----------|---------|----------|


startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4

print(busyStudent(startTime, endTime, queryTime))  # 1
