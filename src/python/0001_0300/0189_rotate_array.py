"""
- Rotate array with reversing subarrays

```mermaid
graph TD
    A[1 2 3 4 5 6 7] --Reverse entire array--> B[7 6 5 4 3 2 1]
    B --Reverse first k elements--> C[5 6 7 4 3 2 1]
    C --Reverse remaining n-k elements--> D[5 6 7 1 2 3 4];
```
"""

from typing import List


# Array
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def reverse(i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    n = len(nums)
    k %= n
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # [5, 6, 7, 1, 2, 3, 4]
