---
comments: True
---

# Exchange Argument

## Table of Contents

- [ ] [2895. Minimum Processing Time](https://leetcode.cn/problems/minimum-processing-time/) (Medium)
- [ ] [3457. Eat Pizzas!](https://leetcode.cn/problems/eat-pizzas/) (Medium)
- [ ] [1665. Minimum Initial Energy to Finish Tasks](https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/) (Hard)
- [ ] [3273. Minimum Amount of Damage Dealt to Bob](https://leetcode.cn/problems/minimum-amount-of-damage-dealt-to-bob/) (Hard)
- [ ] [2136. Earliest Possible Day of Full Bloom](https://leetcode.cn/problems/earliest-possible-day-of-full-bloom/) (Hard)
- [x] [179. Largest Number](https://leetcode.cn/problems/largest-number/) (Medium)
- [ ] [3309. Maximum Possible Number by Binary Concatenation](https://leetcode.cn/problems/maximum-possible-number-by-binary-concatenation/) (Medium)

## 2895. Minimum Processing Time

-   [LeetCode](https://leetcode.com/problems/minimum-processing-time/) | [LeetCode CH](https://leetcode.cn/problems/minimum-processing-time/) (Medium)

-   Tags: array, greedy, sorting
## 3457. Eat Pizzas!

-   [LeetCode](https://leetcode.com/problems/eat-pizzas/) | [LeetCode CH](https://leetcode.cn/problems/eat-pizzas/) (Medium)

-   Tags: array, greedy, sorting
## 1665. Minimum Initial Energy to Finish Tasks

-   [LeetCode](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/) | [LeetCode CH](https://leetcode.cn/problems/minimum-initial-energy-to-finish-tasks/) (Hard)

-   Tags: array, greedy, sorting
## 3273. Minimum Amount of Damage Dealt to Bob

-   [LeetCode](https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/) | [LeetCode CH](https://leetcode.cn/problems/minimum-amount-of-damage-dealt-to-bob/) (Hard)

-   Tags: array, greedy, sorting
## 2136. Earliest Possible Day of Full Bloom

-   [LeetCode](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/) | [LeetCode CH](https://leetcode.cn/problems/earliest-possible-day-of-full-bloom/) (Hard)

-   Tags: array, greedy, sorting
## 179. Largest Number

-   [LeetCode](https://leetcode.com/problems/largest-number/) | [LeetCode CH](https://leetcode.cn/problems/largest-number/) (Medium)

-   Tags: array, string, greedy, sorting

```python title="179. Largest Number - Python Solution"
from functools import cmp_to_key
from typing import List


# Greedy
def largestNumber(nums: List[int]) -> str:
    strs = map(str, nums)

    def cmp(a, b):
        if a + b == b + a:
            return 0
        elif a + b > b + a:
            return 1
        else:
            return -1

    strs = sorted(strs, key=cmp_to_key(cmp), reverse=True)

    return "".join(strs) if strs[0] != "0" else "0"


nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))  # 9534330

```

## 3309. Maximum Possible Number by Binary Concatenation

-   [LeetCode](https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/) | [LeetCode CH](https://leetcode.cn/problems/maximum-possible-number-by-binary-concatenation/) (Medium)

-   Tags: array, bit manipulation, enumeration
