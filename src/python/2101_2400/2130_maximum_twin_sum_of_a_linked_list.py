from typing import Optional

from template import ListNode


# Linked List
def pairSum(head: Optional[ListNode]) -> int:
    def middle(node):
        fast, slow = node, node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(node):
        cur, pre = node, None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    list1 = head
    list2 = reverse(middle(head))
    res = float("-inf")

    while list2:
        res = max(res, list1.val + list2.val)
        list1 = list1.next
        list2 = list2.next

    return res


node = ListNode().create([4, 2, 2, 3])
print(pairSum(node))  # 7
