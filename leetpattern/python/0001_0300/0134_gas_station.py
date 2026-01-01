from typing import List


class canCompleteCircuit:
    def greedy(self, gas: List[int], cost: List[int]) -> int:
        """
        Approach: Greedy
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # edge case
        if sum(gas) < sum(cost):
            return -1

        cur_sum = 0
        start = 0

        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]

            if cur_sum < 0:
                start = i + 1
                cur_sum = 0

        return start


if __name__ == "__main__":
    solution = canCompleteCircuit()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert solution.greedy(gas, cost) == 3
