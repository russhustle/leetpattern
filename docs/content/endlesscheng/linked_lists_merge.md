---
comments: True
---

# Linked Lists Merge

## Table of Contents

- [x] [2. Add Two Numbers](https://leetcode.cn/problems/add-two-numbers/) (Medium)
- [ ] [445. Add Two Numbers II](https://leetcode.cn/problems/add-two-numbers-ii/) (Medium)
- [x] [2816. Double a Number Represented as a Linked List](https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/) (Medium)
- [x] [21. Merge Two Sorted Lists](https://leetcode.cn/problems/merge-two-sorted-lists/) (Easy)
- [ ] [369. Plus One Linked List](https://leetcode.cn/problems/plus-one-linked-list/) (Medium) 👑
- [ ] [1634. Add Two Polynomials Represented as Linked Lists](https://leetcode.cn/problems/add-two-polynomials-represented-as-linked-lists/) (Medium) 👑

## 2. Add Two Numbers

-   [LeetCode](https://leetcode.com/problems/add-two-numbers/) | [LeetCode CH](https://leetcode.cn/problems/add-two-numbers/) (Medium)

-   Tags: linked list, math, recursion
-   Represent the sum of two numbers as a linked list.

```python title="2. Add Two Numbers - Python Solution"
from typing import Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


# Linked List
def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    carry = 0

    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        carry, val = divmod(v1 + v2 + carry, 10)
        cur.next = ListNode(val)
        cur = cur.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        cur.next = ListNode(val=carry)

    return dummy.next


def test_add_two_numbers():
    l1 = list_from_array([2, 4, 3])
    l2 = list_from_array([5, 6, 4])
    result = add_two_numbers(l1, l2)
    assert list_to_array(result) == [7, 0, 8]

```

```cpp title="2. Add Two Numbers - C++ Solution"
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
   public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* cur = &dummy;
        int carry = 0;

        while (l1 || l2 || carry) {
            if (l1) {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                carry += l2->val;
                l2 = l2->next;
            }
            cur->next = new ListNode(carry % 10);
            cur = cur->next;
            carry /= 10;
        }
        return dummy.next;
    }
};
```

## 445. Add Two Numbers II

-   [LeetCode](https://leetcode.com/problems/add-two-numbers-ii/) | [LeetCode CH](https://leetcode.cn/problems/add-two-numbers-ii/) (Medium)

-   Tags: linked list, math, stack
## 2816. Double a Number Represented as a Linked List

-   [LeetCode](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/) (Medium)

-   Tags: linked list, math, stack
-   Given a number represented as a linked list, double it and return the resulting linked list.

```python title="2816. Double a Number Represented as a Linked List - Python Solution"
from typing import Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


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


def test_doubleIt() -> None:
    head = list_from_array([9, 9, 9])
    assert (list_to_array(doubleIt(head))) == [1, 9, 9, 8]

```

## 21. Merge Two Sorted Lists

-   [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) | [LeetCode CH](https://leetcode.cn/problems/merge-two-sorted-lists/) (Easy)

-   Tags: linked list, recursion
-   Task: Merge the two linked lists into one sorted list.

```python title="21. Merge Two Sorted Lists - Python Solution"
from typing import Optional

from leetpattern.utils import ListNode


# Linked List
def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    if list1:
        cur.next = list1
    elif list2:
        cur.next = list2

    return dummy.next

```

```cpp title="21. Merge Two Sorted Lists - C++ Solution"
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
   public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy;
        ListNode* cur = &dummy;

        while (list1 && list2) {
            if (list1->val < list2->val) {
                cur->next = list1;
                list1 = list1->next;
            } else {
                cur->next = list2;
                list2 = list2->next;
            }
            cur = cur->next;
        }

        cur->next = list1 ? list1 : list2;

        return dummy.next;
    }
};
```

## 369. Plus One Linked List

-   [LeetCode](https://leetcode.com/problems/plus-one-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/plus-one-linked-list/) (Medium)

-   Tags: linked list, math
## 1634. Add Two Polynomials Represented as Linked Lists

-   [LeetCode](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/) | [LeetCode CH](https://leetcode.cn/problems/add-two-polynomials-represented-as-linked-lists/) (Medium)

-   Tags: linked list, math, two pointers
