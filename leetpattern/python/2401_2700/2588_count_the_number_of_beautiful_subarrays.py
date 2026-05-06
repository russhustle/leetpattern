from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        """Prefix XOR + HashMap: O(n) time, O(n) space.
        A subarray XORs to 0 iff its prefix XOR equals
        a previously seen prefix XOR.
        """
        res, prefix = 0, 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            prefix ^= x
            res += cnt[prefix]
            cnt[prefix] += 1
        return res


def test_beautiful_subarrays():
    s = Solution()
    assert s.beautifulSubarrays([4, 3, 1, 2, 4]) == 2
    assert s.beautifulSubarrays([1, 10, 4]) == 0
    assert s.beautifulSubarrays([0]) == 1
