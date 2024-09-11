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

    def intersect(self, other: "ListNode", val: int) -> None:
        cur = self
        while cur and cur.val != val:
            cur = cur.next

        if not cur:
            raise ValueError(f"Value {val} not found in the list.")

        cur_other = other
        while cur_other.next:
            cur_other = cur_other.next

        cur_other.next = cur


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


def complexity(table: List[List[str]]) -> None:
    header = ["Approach", "Time", "Space"]
    table.insert(0, header)

    col_widths = [
        max(len(row[i]) for row in table) for i in range(len(table[0]))
    ]

    def format_row(row):
        return " | ".join(
            f"{cell:<{col_widths[i]}}" for i, cell in enumerate(row)
        )

    separator = "|".join("-" * (width + 2) for width in col_widths)

    print(f"# |{separator}|")
    print(f"# | {format_row(table[0])} |")
    print(f"# |{separator}|")
    for row in table[1:]:
        print(f"# | {format_row(row)} |")
    print(f"# |{separator}|")