---
comments: True
---

# Math

## Table of Contents

- [x] [1945. Sum of Digits of String After Convert](https://leetcode.cn/problems/sum-of-digits-of-string-after-convert/) (Easy)
- [x] [1894. Find the Student that Will Replace the Chalk](https://leetcode.cn/problems/find-the-student-that-will-replace-the-chalk/) (Medium)
- [x] [7. Reverse Integer](https://leetcode.cn/problems/reverse-integer/) (Medium)

## 1945. Sum of Digits of String After Convert

-   [LeetCode](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-digits-of-string-after-convert/) (Easy)

-   Tags: string, simulation
```python title="1945. Sum of Digits of String After Convert - Python Solution"
# Math
def getLucky(s: str, k: int) -> int:
    def getSum(n: int) -> int:
        total = 0
        while n != 0:
            n, m = divmod(n, 10)
            total += m
        return total

    result = ""
    for i in s:
        result += str(ord(i) - ord("a") + 1)
    result = int(result)

    for _ in range(k):
        result = getSum(result)

    return result


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |    Math    |  O(n)  |  O(1)   |
# |------------|--------|---------|


s = "iiii"
k = 1

print(getLucky(s, k))  # 36

```

## 1894. Find the Student that Will Replace the Chalk

-   [LeetCode](https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/) | [LeetCode CH](https://leetcode.cn/problems/find-the-student-that-will-replace-the-chalk/) (Medium)

-   Tags: array, binary search, simulation, prefix sum
```python title="1894. Find the Student that Will Replace the Chalk - Python Solution"
from typing import List


# Math
def chalkReplacer(chalk: List[int], k: int) -> int:
    total = sum(chalk)

    k %= total

    for i, c in enumerate(chalk):
        k -= c

        if k < 0:
            return i

    return -1


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |    Math    |  O(n)  |  O(1)   |
# |------------|--------|---------|


chalk = [5, 1, 5]
k = 22

print(chalkReplacer(chalk, k))  # 0

```

## 7. Reverse Integer

-   [LeetCode](https://leetcode.com/problems/reverse-integer/) | [LeetCode CH](https://leetcode.cn/problems/reverse-integer/) (Medium)

-   Tags: math
```python title="7. Reverse Integer - Python Solution"
# Math
def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1

    sign = -1 if x < 0 else 1
    x = abs(x)
    res = 0

    while x != 0:
        x, pop = divmod(x, 10)

        if res > (INT_MAX - pop) // 10:
            return 0

        res = res * 10 + pop

    return res * sign


print(reverse(123))  # 321
print(reverse(-123))  # -321

```

