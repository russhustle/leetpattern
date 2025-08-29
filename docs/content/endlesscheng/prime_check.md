---
comments: True
---

# Prime Check

## Table of Contents

- [ ] [3115. Maximum Prime Difference](https://leetcode.cn/problems/maximum-prime-difference/) (Medium)
- [x] [2614. Prime In Diagonal](https://leetcode.cn/problems/prime-in-diagonal/) (Easy)
- [ ] [762. Prime Number of Set Bits in Binary Representation](https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation/) (Easy)
- [ ] [3044. Most Frequent Prime](https://leetcode.cn/problems/most-frequent-prime/) (Medium)
- [ ] [866. Prime Palindrome](https://leetcode.cn/problems/prime-palindrome/) (Medium)

## 3115. Maximum Prime Difference

-   [LeetCode](https://leetcode.com/problems/maximum-prime-difference/) | [LeetCode CH](https://leetcode.cn/problems/maximum-prime-difference/) (Medium)

-   Tags: array, math, number theory
## 2614. Prime In Diagonal

-   [LeetCode](https://leetcode.com/problems/prime-in-diagonal/) | [LeetCode CH](https://leetcode.cn/problems/prime-in-diagonal/) (Easy)

-   Tags: array, math, matrix, number theory
```python title="2614. Prime In Diagonal - Python Solution"
from math import isqrt
from typing import List


# Prime
def diagonalPrime(nums: List[List[int]]) -> int:
    def is_prime(n):
        if n <= 1:
            return False

        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    res = 0
    for i, row in enumerate(nums):
        for x in row[i], row[-1 - i]:
            if x > res and is_prime(x):
                res = x

    return res


if __name__ == "__main__":
    nums = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    print(diagonalPrime(nums))  # 11

```

## 762. Prime Number of Set Bits in Binary Representation

-   [LeetCode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) | [LeetCode CH](https://leetcode.cn/problems/prime-number-of-set-bits-in-binary-representation/) (Easy)

-   Tags: math, bit manipulation
## 3044. Most Frequent Prime

-   [LeetCode](https://leetcode.com/problems/most-frequent-prime/) | [LeetCode CH](https://leetcode.cn/problems/most-frequent-prime/) (Medium)

-   Tags: array, hash table, math, matrix, counting, enumeration, number theory
## 866. Prime Palindrome

-   [LeetCode](https://leetcode.com/problems/prime-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/prime-palindrome/) (Medium)

-   Tags: math, number theory
