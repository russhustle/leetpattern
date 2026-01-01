from typing import List


class longestCommonPrefix:
    def horizontal_scan(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

    def vertical_scan(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]

        return strs[0]

    def divide_conquer(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def merge(left, right):
            n = min(len(left), len(right))
            for i in range(n):
                if left[i] != right[i]:
                    return left[:i]
            return left[:n]

        def find(strs, start, end):
            if start == end:
                return strs[start]
            mid = start + (end - start) // 2
            left = find(strs, start, mid)
            right = find(strs, mid + 1, end)
            return merge(left, right)

        return find(strs, 0, len(strs) - 1)

    def binary_search(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def isCommonPrefix(strs, length):
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)

        minLen = min(len(s) for s in strs)
        low, high = 0, minLen
        while low < high:
            mid = low + (high - low) // 2
            if isCommonPrefix(strs, mid + 1):
                low = mid + 1
            else:
                high = mid

        return strs[0][:low]


if __name__ == "__main__":
    solution = longestCommonPrefix()
    strs = ["flower", "flow", "flight"]
    assert solution.horizontal_scan(strs) == "fl"
    assert solution.vertical_scan(strs) == "fl"
    assert solution.divide_conquer(strs) == "fl"
    assert solution.binary_search(strs) == "fl"
