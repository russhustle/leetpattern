---
comments: True
---

# Bit Basics

## Table of Contents

- [ ] [3370. Smallest Number With All Set Bits](https://leetcode.cn/problems/smallest-number-with-all-set-bits/) (Easy)
- [ ] [3226. Number of Bit Changes to Make Two Integers Equal](https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/) (Easy)
- [ ] [1356. Sort Integers by The Number of 1 Bits](https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/) (Easy)
- [ ] [461. Hamming Distance](https://leetcode.cn/problems/hamming-distance/) (Easy)
- [ ] [2220. Minimum Bit Flips to Convert Number](https://leetcode.cn/problems/minimum-bit-flips-to-convert-number/) (Easy)
- [ ] [476. Number Complement](https://leetcode.cn/problems/number-complement/) (Easy)
- [ ] [1009. Complement of Base 10 Integer](https://leetcode.cn/problems/complement-of-base-10-integer/) (Easy)
- [ ] [868. Binary Gap](https://leetcode.cn/problems/binary-gap/) (Easy)
- [ ] [3211. Generate Binary Strings Without Adjacent Zeros](https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/) (Medium)
- [ ] [2917. Find the K-or of an Array](https://leetcode.cn/problems/find-the-k-or-of-an-array/) (Easy)
- [ ] [693. Binary Number with Alternating Bits](https://leetcode.cn/problems/binary-number-with-alternating-bits/) (Easy)
- [ ] [2657. Find the Prefix Common Array of Two Arrays](https://leetcode.cn/problems/find-the-prefix-common-array-of-two-arrays/) (Medium)
- [ ] [231. Power of Two](https://leetcode.cn/problems/power-of-two/) (Easy)
- [ ] [342. Power of Four](https://leetcode.cn/problems/power-of-four/) (Easy)
- [x] [191. Number of 1 Bits](https://leetcode.cn/problems/number-of-1-bits/) (Easy)
- [x] [2595. Number of Even and Odd Bits](https://leetcode.cn/problems/number-of-even-and-odd-bits/) (Easy)
- [x] [338. Counting Bits](https://leetcode.cn/problems/counting-bits/) (Easy)

## 3370. Smallest Number With All Set Bits

-   [LeetCode](https://leetcode.com/problems/smallest-number-with-all-set-bits/) | [LeetCode CH](https://leetcode.cn/problems/smallest-number-with-all-set-bits/) (Easy)

-   Tags: math, bit manipulation
## 3226. Number of Bit Changes to Make Two Integers Equal

-   [LeetCode](https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/) | [LeetCode CH](https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/) (Easy)

-   Tags: bit manipulation
## 1356. Sort Integers by The Number of 1 Bits

-   [LeetCode](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) | [LeetCode CH](https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/) (Easy)

-   Tags: array, bit manipulation, sorting, counting
## 461. Hamming Distance

-   [LeetCode](https://leetcode.com/problems/hamming-distance/) | [LeetCode CH](https://leetcode.cn/problems/hamming-distance/) (Easy)

-   Tags: bit manipulation
## 2220. Minimum Bit Flips to Convert Number

-   [LeetCode](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) | [LeetCode CH](https://leetcode.cn/problems/minimum-bit-flips-to-convert-number/) (Easy)

-   Tags: bit manipulation
## 476. Number Complement

-   [LeetCode](https://leetcode.com/problems/number-complement/) | [LeetCode CH](https://leetcode.cn/problems/number-complement/) (Easy)

-   Tags: bit manipulation
## 1009. Complement of Base 10 Integer

-   [LeetCode](https://leetcode.com/problems/complement-of-base-10-integer/) | [LeetCode CH](https://leetcode.cn/problems/complement-of-base-10-integer/) (Easy)

-   Tags: bit manipulation
## 868. Binary Gap

-   [LeetCode](https://leetcode.com/problems/binary-gap/) | [LeetCode CH](https://leetcode.cn/problems/binary-gap/) (Easy)

-   Tags: bit manipulation
## 3211. Generate Binary Strings Without Adjacent Zeros

-   [LeetCode](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/) | [LeetCode CH](https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/) (Medium)

-   Tags: string, backtracking, bit manipulation
## 2917. Find the K-or of an Array

-   [LeetCode](https://leetcode.com/problems/find-the-k-or-of-an-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-k-or-of-an-array/) (Easy)

-   Tags: array, bit manipulation
## 693. Binary Number with Alternating Bits

-   [LeetCode](https://leetcode.com/problems/binary-number-with-alternating-bits/) | [LeetCode CH](https://leetcode.cn/problems/binary-number-with-alternating-bits/) (Easy)

-   Tags: bit manipulation
## 2657. Find the Prefix Common Array of Two Arrays

-   [LeetCode](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/) | [LeetCode CH](https://leetcode.cn/problems/find-the-prefix-common-array-of-two-arrays/) (Medium)

-   Tags: array, hash table, bit manipulation
## 231. Power of Two

-   [LeetCode](https://leetcode.com/problems/power-of-two/) | [LeetCode CH](https://leetcode.cn/problems/power-of-two/) (Easy)

-   Tags: math, bit manipulation, recursion
## 342. Power of Four

-   [LeetCode](https://leetcode.com/problems/power-of-four/) | [LeetCode CH](https://leetcode.cn/problems/power-of-four/) (Easy)

-   Tags: math, bit manipulation, recursion
## 191. Number of 1 Bits

-   [LeetCode](https://leetcode.com/problems/number-of-1-bits/) | [LeetCode CH](https://leetcode.cn/problems/number-of-1-bits/) (Easy)

-   Tags: divide and conquer, bit manipulation

```python title="191. Number of 1 Bits - Python Solution"
# Bit Manipulation
def hammingWeight1(n: int) -> int:
    res = 0

    while n != 0:
        n = n & (n - 1)  # Unset the rightmost 1-bit
        res += 1

    return res


def hammingWeight2(n: int) -> int:
    return bin(n).count("1")


def hammingWeight3(n: int) -> int:
    def decimalToBinary(n: int) -> str:
        if n == 0:
            return "0"

        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2

        return binary

    binary = decimalToBinary(n)

    return binary.count("1")


n = 11
print(hammingWeight1(n))  # 3
print(hammingWeight2(n))  # 3

n = 47
print(bin(n))

```

## 2595. Number of Even and Odd Bits

-   [LeetCode](https://leetcode.com/problems/number-of-even-and-odd-bits/) | [LeetCode CH](https://leetcode.cn/problems/number-of-even-and-odd-bits/) (Easy)

-   Tags: bit manipulation
-   Topic: Bit Manipulation
-   Difficulty: Easy

> You are given a positive integer n.
> Let even denote the number of even indices in the binary representation of n with value 1.
> Let odd denote the number of odd indices in the binary representation of n with value 1.
> Note that bits are indexed from right to left in the binary representation of a number.
> Return the array [even, odd].


```python title="2595. Number of Even and Odd Bits - Python Solution"


```

## 338. Counting Bits

-   [LeetCode](https://leetcode.com/problems/counting-bits/) | [LeetCode CH](https://leetcode.cn/problems/counting-bits/) (Easy)

-   Tags: dynamic programming, bit manipulation

```python title="338. Counting Bits - Python Solution"
from typing import List


# Bit Manipulation
def countBits(n: int) -> List[int]:
    bits = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)

    return bits


n = 5
print(countBits(n))  # [0, 1, 1, 2, 1, 2]

```
