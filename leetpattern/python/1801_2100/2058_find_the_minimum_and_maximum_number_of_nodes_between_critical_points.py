from typing import List, Optional

from leetpattern.utils import ListNode


# Linked List
def nodesBetweenCriticalPoints(head: Optional[ListNode]) -> List[int]:
    pre = head.val
    cur = head.next
    idx = 0
    count = 0
    res = []
    mn = float("inf")

    while cur.next:
        idx += 1
        val = cur.val
        if pre > val and val < cur.next.val:
            res.append(idx)
            count += 1
        elif pre < val and val > cur.next.val:
            res.append(idx)
            count += 1

        if count >= 2:
            mn = min(mn, res[-1] - res[-2])
        pre = val
        cur = cur.next

    if count >= 2:
        return [mn, res[-1] - res[0]]
    else:
        return [-1, -1]


node = ListNode().create([5, 3, 1, 2, 5, 1, 2])
print(nodesBetweenCriticalPoints(node))  # [1, 3]
