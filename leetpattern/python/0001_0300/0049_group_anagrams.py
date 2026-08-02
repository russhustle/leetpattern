from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Counting Hash Map: O(n * k) time, O(n) space.
        Words with the same 26-letter frequency tuple are anagrams.
        """
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord("a")] += 1
            groups[tuple(counts)].append(word)

        return list(groups.values())


def test_group_anagrams():
    def normalized(groups):
        return sorted(sorted(group) for group in groups)

    s = Solution()
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert normalized(result) == [
        ["ate", "eat", "tea"],
        ["bat"],
        ["nat", "tan"],
    ]
    assert normalized(s.groupAnagrams([""])) == [[""]]
    assert normalized(s.groupAnagrams(["a"])) == [["a"]]
