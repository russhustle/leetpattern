from typing import Optional

from helper import ListNode


# 1. Recursive
def removeNodesRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    head.next = removeNodesRecursive(head.next)

    if head.next and head.val < head.next.val:
        return head.next

    return head


# 2. Iterative
def removeNodesIterative(head: Optional[ListNode]) -> Optional[ListNode]:
    stack = []
    cur = head

    while cur:
        # pop all nodes in stack that are smaller than cur
        while stack and cur.val > stack[-1].val:
            stack.pop()

        stack.append(cur)
        cur = cur.next

    # link all nodes in stack
    dummy = ListNode()
    cur = dummy

    for node in stack:
        cur.next = node
        cur = cur.next

    return dummy.next


head = [5, 2, 13, 3, 8]
head1 = ListNode.create(head)
print(head1)
# 5 -> 2 -> 13 -> 3 -> 8
print(removeNodesRecursive(head1))
# 13 -> 8

head2 = ListNode.create(head)
print(removeNodesIterative(head2))
# 13 -> 8
