from typing import List


# DP - Knapsack Unbounded
def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    wordSet = set(wordDict)
    dp = [False for _ in range(n + 1)]
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[n]


s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))  # True
