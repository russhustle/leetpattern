---
comments: True
---

# Bit Contribution Method

## Table of Contents

- [ ] [477. Total Hamming Distance](https://leetcode.cn/problems/total-hamming-distance/) (Medium)
- [x] [1863. Sum of All Subset XOR Totals](https://leetcode.cn/problems/sum-of-all-subset-xor-totals/) (Easy)
- [ ] [2425. Bitwise XOR of All Pairings](https://leetcode.cn/problems/bitwise-xor-of-all-pairings/) (Medium)
- [ ] [2275. Largest Combination With Bitwise AND Greater Than Zero](https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/) (Medium)
- [ ] [1835. Find XOR Sum of All Pairs Bitwise AND](https://leetcode.cn/problems/find-xor-sum-of-all-pairs-bitwise-and/) (Hard)
- [ ] [2505. Bitwise OR of All Subsequence Sums](https://leetcode.cn/problems/bitwise-or-of-all-subsequence-sums/) (Medium) 👑
- [ ] [3153. Sum of Digit Differences of All Pairs](https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs/) (Medium)

## 477. Total Hamming Distance

-   [LeetCode](https://leetcode.com/problems/total-hamming-distance/) | [LeetCode CH](https://leetcode.cn/problems/total-hamming-distance/) (Medium)

-   Tags: array, math, bit manipulation

## 1863. Sum of All Subset XOR Totals

-   [LeetCode](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-all-subset-xor-totals/) (Easy)

-   Tags: array, math, backtracking, bit manipulation, combinatorics, enumeration

```python title="1863. Sum of All Subset XOR Totals - Python Solution"
from functools import reduce
from operator import or_
from typing import List


def subsetXORSum(nums: List[int]) -> int:
    return reduce(or_, nums) << (len(nums) - 1)


if __name__ == "__main__":
    nums = [5, 1, 6]
    print(subsetXORSum(nums))  # 28

```

## 2425. Bitwise XOR of All Pairings

-   [LeetCode](https://leetcode.com/problems/bitwise-xor-of-all-pairings/) | [LeetCode CH](https://leetcode.cn/problems/bitwise-xor-of-all-pairings/) (Medium)

-   Tags: array, bit manipulation, brainteaser

## 2275. Largest Combination With Bitwise AND Greater Than Zero

-   [LeetCode](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/) | [LeetCode CH](https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/) (Medium)

-   Tags: array, hash table, bit manipulation, counting

## 1835. Find XOR Sum of All Pairs Bitwise AND

-   [LeetCode](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/) | [LeetCode CH](https://leetcode.cn/problems/find-xor-sum-of-all-pairs-bitwise-and/) (Hard)

-   Tags: array, math, bit manipulation

## 2505. Bitwise OR of All Subsequence Sums

-   [LeetCode](https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/) | [LeetCode CH](https://leetcode.cn/problems/bitwise-or-of-all-subsequence-sums/) (Medium)

-   Tags: array, math, bit manipulation, brainteaser

## 3153. Sum of Digit Differences of All Pairs

-   [LeetCode](https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs/) (Medium)

-   Tags: array, hash table, math, counting
