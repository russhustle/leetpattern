class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Sliding Window: O(n) time, O(min(n, charset)) space.
        Jump the left edge past each repeated character's previous index.
        """
        left = 0
        res = 0
        seen = {}

        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            seen[ch] = right
            res = max(res, right - left + 1)

        return res

    def lengthOfLongestSubstringSet(self, s: str) -> int:
        """Sliding Window Set: O(n) time, O(min(n, charset)) space.
        Shrink until the current character is unique in the window.
        """
        left = 0
        res = 0
        window = set()

        for right, ch in enumerate(s):
            while ch in window:
                window.remove(s[left])
                left += 1
            window.add(ch)
            res = max(res, right - left + 1)

        return res


def test_length_of_longest_substring():
    s = Solution()
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("abba", 2),
        ("dvdf", 3),
    ]

    for text, expected in cases:
        assert s.lengthOfLongestSubstring(text) == expected
        assert s.lengthOfLongestSubstringSet(text) == expected
