from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for i in s:
            count[ord(i) - ord("a")] += 1

        result[tuple(count)].append(s)

    return result.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
