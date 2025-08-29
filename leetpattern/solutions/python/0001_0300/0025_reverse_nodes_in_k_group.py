from typing import Optional

from template import ListNode


# Linked List
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    p0 = dummy = ListNode(next=head)
    pre = None
    cur = head

    while n >= k:
        n -= k
        for _ in range(k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        nxt = p0.next
        nxt.next = cur
        p0.next = pre
        p0 = nxt

    return dummy.next


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    k = 2
    head = ListNode.create(head)
    print(head)  # 1 -> 2 -> 3 -> 4 -> 5
    print(reverseKGroup(head, k))  # 2 -> 1 -> 4 -> 3 -> 5
