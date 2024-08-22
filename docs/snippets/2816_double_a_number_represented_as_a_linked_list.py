from typing import Optional

from helper import ListNode


def doubleIt(head: Optional[ListNode]) -> Optional[ListNode]:

    def twice(node):
        if not node:
            return 0
        doubled_value = node.val * 2 + twice(node.next)
        node.val = doubled_value % 10
        return doubled_value // 10

    carry = twice(head)

    if carry:
        head = ListNode(val=carry, next=head)

    return head


head = ListNode.create([1, 2, 3, 4])
print(head)
# 1 -> 2 -> 3 -> 4
print(doubleIt(head))
# 2 -> 4 -> 6 -> 8
