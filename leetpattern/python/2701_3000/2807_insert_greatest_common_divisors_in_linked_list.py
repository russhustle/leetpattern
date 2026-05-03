from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        dummy = head
        cur = dummy

        while cur.next:
            v1, v2 = cur.val, cur.next.val
            new = ListNode(val=gcd(max(v1, v2), min(v1, v2)))
            new.next = cur.next
            cur.next = new
            cur = cur.next.next

        return dummy
