---
comments: True
---

# One Sequence Two Pointers In-Place Modification

## Table of Contents

- [x] [27. Remove Element](https://leetcode.cn/problems/remove-element/) (Easy)
- [x] [26. Remove Duplicates from Sorted Array](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) (Easy)
- [x] [80. Remove Duplicates from Sorted Array II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/) (Medium)
- [x] [283. Move Zeroes](https://leetcode.cn/problems/move-zeroes/) (Easy)
- [x] [905. Sort Array By Parity](https://leetcode.cn/problems/sort-array-by-parity/) (Easy)
- [ ] [922. Sort Array By Parity II](https://leetcode.cn/problems/sort-array-by-parity-ii/) (Easy)
- [ ] [2460. Apply Operations to an Array](https://leetcode.cn/problems/apply-operations-to-an-array/) (Easy)
- [x] [1089. Duplicate Zeros](https://leetcode.cn/problems/duplicate-zeros/) (Easy)

## 27. Remove Element

-   [LeetCode](https://leetcode.com/problems/remove-element/) | [LeetCode CH](https://leetcode.cn/problems/remove-element/) (Easy)

-   Tags: array, two pointers
-   Remove all instances of a given value in-place.


```python title="27. Remove Element - Python Solution"
from typing import List


# Fast Slow Pointers
def removeElement(nums: List[int], val: int) -> int:
    fast, slow = 0, 0

    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))  # 5

```

```cpp title="27. Remove Element - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

// Fast Slow Pointers
int removeElement(vector<int>& nums, int val) {
    size_t n = nums.size();
    size_t slow = 0, fast = 0;

    while (fast < n) {
        if (nums[fast] != val) {
            nums[slow] = nums[fast];
            slow++;
        }
        fast++;
    }
    return (int)slow;
}

int main() {
    vector<int> nums = {3, 2, 2, 3};
    int val = 3;
    cout << removeElement(nums, val) << endl;  // 2
    return 0;
}

```

## 26. Remove Duplicates from Sorted Array

-   [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) (Easy)

-   Tags: array, two pointers
-   Remove duplicates in-place.


```python title="26. Remove Duplicates from Sorted Array - Python Solution"
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    fast, slow = 1, 1

    while fast < len(nums):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


nums = [1, 1, 2]
print(removeDuplicates(nums))  # 2

```

## 80. Remove Duplicates from Sorted Array II

-   [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | [LeetCode CH](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/) (Medium)

-   Tags: array, two pointers
-   Allow at most two duplicates.
-   fast pointer: explore the array
-   slow pointer: point to the position to be replaced


```python title="80. Remove Duplicates from Sorted Array II - Python Solution"
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    fast, slow = 2, 2

    while fast < len(nums):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums))

```

## 283. Move Zeroes

-   [LeetCode](https://leetcode.com/problems/move-zeroes/) | [LeetCode CH](https://leetcode.cn/problems/move-zeroes/) (Easy)

-   Tags: array, two pointers
-   Move all zeroes to the end of the array while maintaining the relative order of the non-zero elements.


```python title="283. Move Zeroes - Python Solution"
from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    fast, slow = 0, 0

    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # [1, 3, 12, 0, 0]

```

```cpp title="283. Move Zeroes - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

void moveZeroes(vector<int>& nums) {
    size_t n = nums.size();
    size_t fast = 0, slow = 0;

    while (fast < n) {
        if (nums[fast] != 0) {
            swap(nums[slow], nums[fast]);
            slow++;
        }
        fast++;
    }
}

int main() {
    vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);
    // [1, 3, 12, 0, 0]
    for (size_t i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}

```

## 905. Sort Array By Parity

-   [LeetCode](https://leetcode.com/problems/sort-array-by-parity/) | [LeetCode CH](https://leetcode.cn/problems/sort-array-by-parity/) (Easy)

-   Tags: array, two pointers, sorting

```python title="905. Sort Array By Parity - Python Solution"
from typing import List


# Left Right Pointers
def sortArrayByParityLR(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if not nums[left] % 2:
            left += 1
        else:
            while left < right and nums[right] % 2:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]

    return nums


# Fast Slow Pointers
def sortArrayByParityFS(nums: List[int]) -> List[int]:
    n = len(nums)
    fast, slow = 0, 0

    while fast < n:
        if not nums[fast] % 2:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1

    return nums


nums = [3, 1, 2, 4]
print(sortArrayByParityLR(nums))  # [4, 2, 1, 3]
print(sortArrayByParityFS(nums))  # [4, 2, 1, 3]

```

## 922. Sort Array By Parity II

-   [LeetCode](https://leetcode.com/problems/sort-array-by-parity-ii/) | [LeetCode CH](https://leetcode.cn/problems/sort-array-by-parity-ii/) (Easy)

-   Tags: array, two pointers, sorting
## 2460. Apply Operations to an Array

-   [LeetCode](https://leetcode.com/problems/apply-operations-to-an-array/) | [LeetCode CH](https://leetcode.cn/problems/apply-operations-to-an-array/) (Easy)

-   Tags: array, two pointers, simulation
## 1089. Duplicate Zeros

-   [LeetCode](https://leetcode.com/problems/duplicate-zeros/) | [LeetCode CH](https://leetcode.cn/problems/duplicate-zeros/) (Easy)

-   Tags: array, two pointers
-   Duplicate each occurrence of zero, shifting the remaining elements to the right.


```python title="1089. Duplicate Zeros - Python Solution"
from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    fast, slow = 0, 0

    # First pass: find the position
    # where the last element would be in the expanded array
    while fast < n:
        if arr[slow] == 0:
            fast += 1
        slow += 1
        fast += 1

    slow -= 1
    fast -= 1

    # Second pass: move elements backwards
    while slow >= 0:
        if fast < n:
            arr[fast] = arr[slow]

        if arr[slow] == 0:
            fast -= 1
            if fast < n:
                arr[fast] = 0

        slow -= 1
        fast -= 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr)
print(arr)  # [1, 0, 0, 2, 3, 0, 0, 4]

```
