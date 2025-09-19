from typing import List


#  Simulation
def sumEvenAfterQueries(nums: List[int], queries: List[List[int]]) -> List[int]:
    res = []
    cur = sum(i for i in nums if i % 2 == 0)

    for val, idx in queries:
        if nums[idx] % 2 == 0:
            cur -= nums[idx]

        nums[idx] += val
        if nums[idx] % 2 == 0:
            cur += nums[idx]

        res.append(cur)

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sumEvenAfterQueries(nums, queries))  # [8, 6, 2, 4]
