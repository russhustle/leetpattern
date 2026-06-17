from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Fixed Sliding Window: O(n + m) time, O(1) space.
        Track 26 lowercase counts for the current window of length len(p).
        """
        if len(p) > len(s):
            return []

        target = [0] * 26
        window = [0] * 26
        for i, ch in enumerate(p):
            target[ord(ch) - ord("a")] += 1
            window[ord(s[i]) - ord("a")] += 1

        res = []
        if window == target:
            res.append(0)

        left = 0
        for right in range(len(p), len(s)):
            window[ord(s[right]) - ord("a")] += 1
            window[ord(s[left]) - ord("a")] -= 1
            left += 1
            if window == target:
                res.append(left)

        return res


def test_find_anagrams():
    s = Solution()
    assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert s.findAnagrams("abab", "ab") == [0, 1, 2]
    assert s.findAnagrams("af", "be") == []
    assert s.findAnagrams("baa", "aa") == [1]
    assert s.findAnagrams("", "a") == []
