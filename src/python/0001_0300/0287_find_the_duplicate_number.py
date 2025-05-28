"""
-   Find the duplicate number in an array containing `n + 1` integers where each integer is between `1` and `n` inclusive.
-   Floyd's Tortoise and Hare (Cycle Detection)
    -   141. Linked List Cycle
    -   142. Linked List Cycle II
-   Time Complexity: O(n)
-   Space Complexity: O(1)

Example: `nums = [1, 3, 4, 2, 2]`

|  0   |  1   |  2   |  3   |  4   |
| :--: | :--: | :--: | :--: | :--: |
|  1   |  3   |  4   |  2   |  2   |



```mermaid
graph LR
0((0)) --> 1((1))
1 --> 3((3))
2((2))--> 4((4))
3 --> 2
4 --> 2
```
"""

from typing import List


# Floyd Cycle Detection Algorithm
def findDuplicate(nums: List[int]) -> int:
    fast, slow = nums[0], nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # 2
