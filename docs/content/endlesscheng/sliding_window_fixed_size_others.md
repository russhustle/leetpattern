---
comments: True
---

# Sliding Window Fixed Size Others

## Table of Contents

- [x] [2269. Find the K-Beauty of a Number](https://leetcode.cn/problems/find-the-k-beauty-of-a-number/) (Easy)
- [ ] [1984. Minimum Difference Between Highest and Lowest of K Scores](https://leetcode.cn/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) (Easy)
- [ ] [220. Contains Duplicate III](https://leetcode.cn/problems/contains-duplicate-iii/) (Hard)

## 2269. Find the K-Beauty of a Number

-   [LeetCode](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) | [LeetCode CH](https://leetcode.cn/problems/find-the-k-beauty-of-a-number/) (Easy)

-   Tags: math, string, sliding window

```python title="2269. Find the K-Beauty of a Number - Python Solution"
def divisorSubstrings(num: int, k: int) -> int:
    numStr = str(num)
    n = len(numStr)
    res = 0

    for i in range(n - k + 1):
        x = int(numStr[i : i + k])
        if x > 0 and num % x == 0:
            res += 1

    return res


num = 240
k = 2
print(divisorSubstrings(num, k))  # 2

```

## 1984. Minimum Difference Between Highest and Lowest of K Scores

-   [LeetCode](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) | [LeetCode CH](https://leetcode.cn/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) (Easy)

-   Tags: array, sliding window, sorting

## 220. Contains Duplicate III

-   [LeetCode](https://leetcode.com/problems/contains-duplicate-iii/) | [LeetCode CH](https://leetcode.cn/problems/contains-duplicate-iii/) (Hard)

-   Tags: array, sliding window, sorting, bucket sort, ordered set
