---
comments: True
---

# Linked List Traversal

## Table of Contents

- [x] [1290. Convert Binary Number in a Linked List to Integer](https://leetcode.cn/problems/convert-binary-number-in-a-linked-list-to-integer/) (Easy)
- [x] [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](https://leetcode.cn/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/) (Medium)
- [x] [2181. Merge Nodes in Between Zeros](https://leetcode.cn/problems/merge-nodes-in-between-zeros/) (Medium)
- [ ] [725. Split Linked List in Parts](https://leetcode.cn/problems/split-linked-list-in-parts/) (Medium)
- [x] [817. Linked List Components](https://leetcode.cn/problems/linked-list-components/) (Medium)
- [ ] [3062. Winner of the Linked List Game](https://leetcode.cn/problems/winner-of-the-linked-list-game/) (Easy) 👑
- [ ] [3063. Linked List Frequency](https://leetcode.cn/problems/linked-list-frequency/) (Easy) 👑

## 1290. Convert Binary Number in a Linked List to Integer

-   [LeetCode](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) | [LeetCode CH](https://leetcode.cn/problems/convert-binary-number-in-a-linked-list-to-integer/) (Easy)

-   Tags: linked list, math
```python title="1290. Convert Binary Number in a Linked List to Integer - Python Solution"
from typing import Optional

from leetpattern.utils import ListNode


# Linked List
def getDecimalValue(head: Optional[ListNode]) -> int:
    res = 0

    while head:
        res = res * 2 + head.val
        head = head.next

    return res


node = ListNode().create([1, 0, 1])
print(node)  # 1 -> 0 -> 1
print(getDecimalValue(node))  # 5

```

## 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

-   [LeetCode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/) | [LeetCode CH](https://leetcode.cn/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/) (Medium)

-   Tags: linked list
```python title="2058. Find the Minimum and Maximum Number of Nodes Between Critical Points - Python Solution"
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

```

## 2181. Merge Nodes in Between Zeros

-   [LeetCode](https://leetcode.com/problems/merge-nodes-in-between-zeros/) | [LeetCode CH](https://leetcode.cn/problems/merge-nodes-in-between-zeros/) (Medium)

-   Tags: linked list, simulation
```python title="2181. Merge Nodes in Between Zeros - Python Solution"
from typing import Optional

from leetpattern.utils import ListNode, LinkedList


def merge_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    dummy = ListNode()
    cur = dummy

    head = head.next
    temp = 0

    while head.next:
        if head.val == 0:
            cur.next = ListNode(temp)
            cur = cur.next
            temp = 0
        else:
            temp += head.val

        head = head.next

    if temp != 0:
        cur.next = ListNode(temp)

    return dummy.next


def test_merge_nodes():
    root = LinkedList([0, 3, 1, 0, 4, 5, 2, 0])
    res = merge_nodes(root.head)
    assert LinkedList(res).to_array() == [4, 11]

```

## 725. Split Linked List in Parts

-   [LeetCode](https://leetcode.com/problems/split-linked-list-in-parts/) | [LeetCode CH](https://leetcode.cn/problems/split-linked-list-in-parts/) (Medium)

-   Tags: linked list
## 817. Linked List Components

-   [LeetCode](https://leetcode.com/problems/linked-list-components/) | [LeetCode CH](https://leetcode.cn/problems/linked-list-components/) (Medium)

-   Tags: array, hash table, linked list
```python title="817. Linked List Components - Python Solution"
from typing import List, Optional

from leetpattern.utils import ListNode


# Linked List
def numComponents(head: Optional[ListNode], nums: List[int]) -> int:
    numSet = set(nums)
    res = 0

    while head:
        if head.val in numSet:
            while head and head.val in numSet:
                head = head.next
            res += 1
        else:
            head = head.next

    return res


head = ListNode().create([0, 1, 2, 3, 4])
nums = [0, 3, 1, 4]
print(numComponents(head, nums))  # 2

```

## 3062. Winner of the Linked List Game

-   [LeetCode](https://leetcode.com/problems/winner-of-the-linked-list-game/) | [LeetCode CH](https://leetcode.cn/problems/winner-of-the-linked-list-game/) (Easy)

-   Tags: linked list
## 3063. Linked List Frequency

-   [LeetCode](https://leetcode.com/problems/linked-list-frequency/) | [LeetCode CH](https://leetcode.cn/problems/linked-list-frequency/) (Easy)

-   Tags: hash table, linked list, counting
