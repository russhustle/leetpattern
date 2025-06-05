---
comments: True
---

# Interval Coverage

## Table of Contents

- [x] [45. Jump Game II](https://leetcode.cn/problems/jump-game-ii/) (Medium)
- [ ] [1024. Video Stitching](https://leetcode.cn/problems/video-stitching/) (Medium)
- [ ] [1326. Minimum Number of Taps to Open to Water a Garden](https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/) (Hard)

## 45. Jump Game II

-   [LeetCode](https://leetcode.com/problems/jump-game-ii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-ii/) (Medium)

-   Tags: array, dynamic programming, greedy
- Return the minimum number of jumps to reach the last index.


```python title="45. Jump Game II - Python Solution"
from typing import List


# Greedy - Interval
def jump(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0

    reach = 0
    left, right = 0, 0
    res = 0

    while right < n - 1:
        for i in range(left, right + 1):
            reach = max(reach, i + nums[i])

        left = right + 1
        right = reach
        res += 1

    return res


if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2

```

## 1024. Video Stitching

-   [LeetCode](https://leetcode.com/problems/video-stitching/) | [LeetCode CH](https://leetcode.cn/problems/video-stitching/) (Medium)

-   Tags: array, dynamic programming, greedy
## 1326. Minimum Number of Taps to Open to Water a Garden

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/) (Hard)

-   Tags: array, dynamic programming, greedy
