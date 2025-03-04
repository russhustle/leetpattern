from typing import Optional

from template import ListNode


# Linked List
def isPalindrome(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return True

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

    mid1 = head
    mid2 = reverse(middle(head))

    while mid2:
        if mid1.val != mid2.val:
            return False
        mid1 = mid1.next
        mid2 = mid2.next

    return True


head = ListNode().create([1, 2, 2, 1])
print(isPalindrome(head))  # True
