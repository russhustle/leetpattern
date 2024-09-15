from collections import deque
from typing import List


# Monotonic Queue
def maximumRobots(
    chargeTimes: List[int], runningCosts: List[int], budget: int
) -> int:
    ans = sum_cost = left = 0
    q = deque()

    for right, (time, cost) in enumerate(zip(chargeTimes, runningCosts)):
        # 1. Add
        while q and time >= chargeTimes[q[-1]]:
            q.pop()
        q.append(right)
        sum_cost += cost

        # 2. Remove
        while q and chargeTimes[q[0]] + (right - left + 1) * sum_cost > budget:
            if q[0] == left:
                q.popleft()
            sum_cost -= runningCosts[left]
            left += 1

        # 3. Update
        ans = max(ans, right - left + 1)
    return ans


chargeTimes = [3, 6, 1, 3, 4]
runningCosts = [2, 1, 3, 4, 5]
budget = 25
print(maximumRobots(chargeTimes, runningCosts, budget))  # 3
