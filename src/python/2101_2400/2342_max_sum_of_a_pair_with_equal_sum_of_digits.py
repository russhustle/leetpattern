from typing import List


# Enumerate Right Maintain Left
def maximumSum(nums: List[int]) -> int:
    def digits_sum(num):
        res = 0
        while num:
            num, carry = divmod(num, 10)
            res += carry
        return res

    hashmap = {}  # digit sum: largest num
    res = -1

    for num in nums:
        ds = digits_sum(num)

        if ds not in hashmap:
            hashmap[ds] = num
        else:
            res = max(res, num + hashmap[ds])
            hashmap[ds] = max(hashmap[ds], num)

    return res


nums = [18, 43, 36, 13, 7]
print(maximumSum(nums))  # 54
