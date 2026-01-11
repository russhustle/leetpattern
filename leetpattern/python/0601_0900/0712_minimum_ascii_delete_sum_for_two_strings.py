class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        题目要求: 计算将两个字符串变为相同所需删除字符的最小 ASCII 值和。
        思路: 保留最大公共子序列的字符，其余字符删除。使用动态规划计算最大公共子序列的 ASCII 值和。
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        total = sum(map(ord, s1)) + sum(map(ord, s2))

        for i, x in enumerate(s1):
            for j, y in enumerate(s2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + ord(x)
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return total - dp[-1][-1] * 2
