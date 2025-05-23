from typing import List


# Greedy
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    curSum = 0
    totalSum = 0
    start = 0

    for i in range(len(gas)):
        curSum += gas[i] - cost[i]
        totalSum += gas[i] - cost[i]

        if curSum < 0:
            start = i + 1
            curSum = 0

    if totalSum < 0:
        return -1

    return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))  # 3
