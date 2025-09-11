from typing import Optional

from leetpattern.utils import ListNode


# Linked List
def deleteNodes(
    head: Optional[ListNode], m: int, n: int
) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    cur = dummy

    while cur.next:
        for _ in range(m):
            if not cur.next:
                break
            cur = cur.next

        for _ in range(n):
            if not cur.next:
                break
            cur.next = cur.next.next

    return dummy.next


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    m = 2
    n = 3
    head = list_from_array(head)
    print(head)
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13
    head = deleteNodes(head, m, n)
    print(head)
    # 1 -> 2 -> 6 -> 7 -> 11 -> 12
