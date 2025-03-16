---
comments: True
---

# Indeed

- [x] [985. Sum of Even Numbers After Queries](https://leetcode.cn/problems/sum-of-even-numbers-after-queries/) (Medium)
- [x] [453. Minimum Moves to Equal Array Elements](https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/) (Medium)
- [ ] [2547. Minimum Cost to Split an Array](https://leetcode.cn/problems/minimum-cost-to-split-an-array/) (Hard)
- [ ] [2225. Find Players With Zero or One Losses](https://leetcode.cn/problems/find-players-with-zero-or-one-losses/) (Medium)
- [ ] [563. Binary Tree Tilt](https://leetcode.cn/problems/binary-tree-tilt/) (Easy)
- [x] [23. Merge k Sorted Lists](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)
- [ ] [2133. Check if Every Row and Column Contains All Numbers](https://leetcode.cn/problems/check-if-every-row-and-column-contains-all-numbers/) (Easy)

## 985. Sum of Even Numbers After Queries

-   [LeetCode](https://leetcode.com/problems/sum-of-even-numbers-after-queries/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-even-numbers-after-queries/) (Medium)

-   Tags: array, simulation

```python title="985. Sum of Even Numbers After Queries - Python Solution"
from typing import List


#  Simulation
def sumEvenAfterQueries(
    nums: List[int], queries: List[List[int]]
) -> List[int]:
    res = []
    cur = sum(i for i in nums if i % 2 == 0)

    for val, idx in queries:
        if nums[idx] % 2 == 0:
            cur -= nums[idx]

        nums[idx] += val
        if nums[idx] % 2 == 0:
            cur += nums[idx]

        res.append(cur)

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sumEvenAfterQueries(nums, queries))  # [8, 6, 2, 4]

```

## 453. Minimum Moves to Equal Array Elements

-   [LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) | [LeetCode CH](https://leetcode.cn/problems/minimum-moves-to-equal-array-elements/) (Medium)

-   Tags: array, math

```python title="453. Minimum Moves to Equal Array Elements - Python Solution"
from typing import List


def minMoves1(nums: List[int]) -> int:
    res, min_val = 0, min(nums)

    for num in nums:
        res += num - min_val

    return res


def minMoves2(nums: List[int]) -> int:
    return sum(nums) - len(nums) * min(nums)


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(minMoves1(nums))  # 3
    print(minMoves2(nums))  # 3

```

```cpp title="453. Minimum Moves to Equal Array Elements - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int minMoves(vector<int>& nums) {
    int res = 0;
    int min_num = *min_element(nums.begin(), nums.end());

    for (int num : nums) {
        res += num - min_num;
    }

    return res;
}

int main() {
    vector<int> nums = {1, 2, 3};
    cout << minMoves(nums) << endl;  // 3
    return 0;
}

```

## 2547. Minimum Cost to Split an Array

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-split-an-array/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-split-an-array/) (Hard)

-   Tags: array, hash table, dynamic programming, counting

## 2225. Find Players With Zero or One Losses

-   [LeetCode](https://leetcode.com/problems/find-players-with-zero-or-one-losses/) | [LeetCode CH](https://leetcode.cn/problems/find-players-with-zero-or-one-losses/) (Medium)

-   Tags: array, hash table, sorting, counting

## 563. Binary Tree Tilt

-   [LeetCode](https://leetcode.com/problems/binary-tree-tilt/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-tilt/) (Easy)

-   Tags: tree, depth first search, binary tree

## 23. Merge k Sorted Lists

-   [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) | [LeetCode CH](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)

-   Tags: linked list, divide and conquer, heap priority queue, merge sort
-   Prerequisite: 21. Merge Two Sorted Lists
-   Video explanation: [23. Merge K Sorted Lists - NeetCode](https://youtu.be/q5a5OiGbT6Q?si=SQ2dCvsYQ3LQctPh)

```python title="23. Merge k Sorted Lists - Python Solution"
import copy
import heapq
from typing import List, Optional

from template import ListNode


# Divide and Conquer
def mergeKListsDC(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    def mergeTwo(l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 if l1 else l2

        return dummy.next

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(mergeTwo(l1, l2))

        lists = merged

    return lists[0]


# Heap - Merge k Sorted
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    minHeap = []  # (val, idx, node)

    for idx, head in enumerate(lists):
        if head:
            heapq.heappush(minHeap, (head.val, idx, head))

    while minHeap:
        _, idx, node = heapq.heappop(minHeap)
        cur.next = node
        cur = cur.next

        node = node.next
        if node:
            heapq.heappush(minHeap, (node.val, idx, node))

    return dummy.next


n1 = ListNode.create([1, 4, 5])
n2 = ListNode.create([1, 3, 4])
n3 = ListNode.create([2, 6])
lists = [n1, n2, n3]
lists1 = copy.deepcopy(lists)
lists2 = copy.deepcopy(lists)
print(mergeKListsDC(lists1))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
print(mergeKLists(lists2))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

```

## 2133. Check if Every Row and Column Contains All Numbers

-   [LeetCode](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/) | [LeetCode CH](https://leetcode.cn/problems/check-if-every-row-and-column-contains-all-numbers/) (Easy)

-   Tags: array, hash table, matrix
