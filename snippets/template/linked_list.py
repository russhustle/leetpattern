from typing import List, Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

    @staticmethod
    def create(nums: List[int], pos=-1) -> Optional["ListNode"]:
        """Create a linked list from a list of integers.

        Args:
            nums (List[int]): List of integers.
            pos (int, optional): Position of the cycle node. Defaults to -1.
        Returns:
            Optional[ListNode]: Head of the linked list.
        """
        if not nums:
            return None

        head = ListNode(value=nums[0])
        cur = head
        cycle_node = None

        for i, val in enumerate(nums[1:], start=1):
            cur.next = ListNode(value=val)
            cur = cur.next
            if i == pos:
                cycle_node = cur

        if pos >= 0:
            cur.next = cycle_node

        return head

    def __str__(self):
        """String representation of the linked list."""
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
