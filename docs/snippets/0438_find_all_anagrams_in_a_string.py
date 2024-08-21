from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    result = []
    if len(s) < len(p):
        return result

    countP = [0] * 26
    for i in p:
        countP[ord(i) - ord("a")] += 1

    countS = [0] * 26
    for i in range(len(p)):
        countS[ord(s[i]) - ord("a")] += 1

    if countS == countP:
        result.append(0)

    # sliding window
    for i in range(len(p), len(s)):
        countS[ord(s[i]) - ord("a")] += 1  # add new character
        countS[ord(s[i - len(p)]) - ord("a")] -= 1  # remove old character
        if countS == countP:
            result.append(i - len(p) + 1)  # append the starting index

    return result


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))  # [0, 6]
