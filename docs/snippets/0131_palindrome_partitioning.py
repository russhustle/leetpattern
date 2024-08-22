from typing import List


def partition(s: str) -> List[List[str]]:
    path, result = [], []

    def backtracking(startIndex):
        if startIndex == len(s):
            result.append(path[:])
            return None

        for i in range(startIndex, len(s)):
            if is_palindrome(s, startIndex, i):
                path.append(s[startIndex : i + 1])
                backtracking(i + 1)
                path.pop()

    def is_palindrome(s: str, start, end) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

    backtracking(0)

    return result


print(partition("aab"))  # [['a', 'a', 'b'], ['aa', 'b']]
