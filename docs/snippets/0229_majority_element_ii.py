from collections import Counter
from typing import List


# Hash Map
def majorityElementHash(nums: List[int]) -> List[int]:
    counts = Counter(nums)
    target = len(nums) // 3
    res = []

    for num in nums:
        if counts[num] > target and num not in res:
            res.append(num)

    return res


# Boyer-Moore
def majorityElementMoore(nums: List[int]) -> List[int]:
    if not nums:
        return []

    cdt1, cnt1 = None, 0
    cdt2, cnt2 = None, 0

    for num in nums:
        if num == cdt1:
            cnt1 += 1
        elif num == cdt2:
            cnt2 += 1
        elif cnt1 == 0:
            cdt1, cnt1 = num, 1
        elif cnt2 == 0:
            cdt2, cnt2 = num, 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    return [n for n in (cdt1, cdt2) if nums.count(n) > len(nums) // 3]


nums = [3, 2, 3]
print(majorityElementHash(nums))  # [3]
print(majorityElementMoore(nums))  # [3]
