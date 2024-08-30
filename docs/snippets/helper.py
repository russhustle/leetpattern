from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create(nums, pos=-1):
        if not nums:
            return None

        head = ListNode(nums[0])
        cur = head
        cycle_node = None

        for i, val in enumerate(nums[1:], start=1):
            cur.next = ListNode(val)
            cur = cur.next
            if i == pos:
                cycle_node = cur

        if pos >= 0:
            cur.next = cycle_node

        return head

    def __str__(self):
        result = []
        cur = self
        visited = set()

        while cur and cur not in visited:
            result.append(str(cur.val))
            visited.add(cur)
            cur = cur.next

        if cur:
            result.append("...")

        return " -> ".join(result)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def LPS(pattern: str) -> List[int]:
    """Returns the Longest Prefix Suffix array for the given pattern.

    Args:
        pattern (str): The pattern string.

    Returns:
        List[int]: The Longest Prefix Suffix array.
    """
    n = len(pattern)
    lps = [0 for _ in range(n)]
    j = 0

    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    return lps
