from collections import defaultdict
from typing import List


def beautifulSubarrays(nums: List[int]) -> int:
    res, s = 0, 0
    cnt = defaultdict(int)
    cnt[0] = 1

    for x in nums:
        s ^= x
        res += cnt[s]
        cnt[s] += 1

    return res


nums = [4, 3, 1, 2, 4]
print(beautifulSubarrays(nums))  # 2
