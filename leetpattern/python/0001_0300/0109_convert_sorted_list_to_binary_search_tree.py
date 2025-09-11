"""
![109](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head:
        return None

    def find_mid(head: ListNode) -> ListNode:
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        return slow

    mid = find_mid(head)

    node = TreeNode(mid.val)

    if head == mid:
        return node

    node.left = sortedListToBST(head)
    node.right = sortedListToBST(mid.next)

    return node


head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

root = sortedListToBST(head)
assert root.val == 0
assert root.left.val == -3
assert root.left.left.val == -10
assert root.right.val == 9
assert root.right.left.val == 5
print("All passed")

#      0
#     / \
#   -3   9
#   /   /
# -10  5
