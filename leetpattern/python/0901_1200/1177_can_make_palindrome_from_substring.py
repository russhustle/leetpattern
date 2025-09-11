from typing import List


# Prefix XOR Sum
def canMakePaliQueries(s: str, queries: List[List[int]]) -> List[bool]:
    sum = [[0] * 26]
    for c in s:
        sum.append(sum[-1].copy())
        sum[-1][ord(c) - ord("a")] ^= 1  # 奇数变偶数，偶数变奇数

    ans = []
    for left, right, k in queries:
        m = 0
        for sl, sr in zip(sum[left], sum[right + 1]):
            m += sr ^ sl
        ans.append(m // 2 <= k)
    return ans


if __name__ == "__main__":
    s = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
    assert canMakePaliQueries(s, queries) == [True, False, False, True, True]
