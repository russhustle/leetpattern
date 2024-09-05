from typing import List


# Set
def longestConsecutiveSet(nums: List[int]) -> int:
    num_set = set(nums)  # O(n)
    longest = 0

    for n in nums:
        if (n - 1) not in num_set:  # left boundary
            length = 1

            while (n + length) in num_set:
                length += 1

            longest = max(longest, length)

    return longest


# Union Find
def longestConsecutiveUF(nums: List[int]) -> int:
    if not nums:
        return 0

    par = {num: num for num in nums}
    rank = {num: 1 for num in nums}

    def find(num):
        p = par[num]
        while p != par[p]:
            p = par[p]
        return p

    def union(num1, num2):
        p1, p2 = find(num1), find(num2)
        if p1 == p2:
            return

        if rank[p1] < rank[p2]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]

    for num in nums:
        if num - 1 in par:
            union(num, num - 1)

    return max(rank.values())


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  Set       |  O(N)  |  O(N)   |
# | Union Find |  O(N)  |  O(N)   |
# |------------|--------|---------|


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutiveSet(nums))  # 4
print(longestConsecutiveUF(nums))  # 4
