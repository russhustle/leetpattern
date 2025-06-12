from collections import defaultdict
from typing import List


# Enumerate Right Maintain Left
def countNicePairs(nums: List[int]) -> int:
    rev = lambda n: int(str(n)[::-1])
    cnt = defaultdict(int)
    MOD = 10**9 + 7
    res = 0

    for num in nums:
        cnt[num - rev(num)] += 1

    for i in cnt.values():
        res += i * (i - 1) // 2  # math.comb(i, 2)

    return res % MOD


if __name__ == "__main__":
    assert countNicePairs([42, 11, 1, 97]) == 2
    assert countNicePairs([13, 10, 35, 24, 76]) == 4
    assert countNicePairs([100, 200, 300]) == 0
    assert countNicePairs([123, 321, 456, 654]) == 2
    assert countNicePairs([12, 21, 34, 43]) == 2
