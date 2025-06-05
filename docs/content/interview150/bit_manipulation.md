---
comments: True
---

# Bit Manipulation

## Table of Contents

- [ ] [67. Add Binary](https://leetcode.cn/problems/add-binary/) (Easy)
- [x] [190. Reverse Bits](https://leetcode.cn/problems/reverse-bits/) (Easy)
- [x] [191. Number of 1 Bits](https://leetcode.cn/problems/number-of-1-bits/) (Easy)
- [x] [136. Single Number](https://leetcode.cn/problems/single-number/) (Easy)
- [ ] [137. Single Number II](https://leetcode.cn/problems/single-number-ii/) (Medium)
- [ ] [201. Bitwise AND of Numbers Range](https://leetcode.cn/problems/bitwise-and-of-numbers-range/) (Medium)

## 67. Add Binary

-   [LeetCode](https://leetcode.com/problems/add-binary/) | [LeetCode CH](https://leetcode.cn/problems/add-binary/) (Easy)

-   Tags: math, string, bit manipulation, simulation
## 190. Reverse Bits

-   [LeetCode](https://leetcode.com/problems/reverse-bits/) | [LeetCode CH](https://leetcode.cn/problems/reverse-bits/) (Easy)

-   Tags: divide and conquer, bit manipulation

```python title="190. Reverse Bits - Python Solution"
# Bit Manipulation
def reverseBits(n: int) -> int:
    res = 0

    for i in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1

    return res


n = 0b00000010100101000001111010011100
print(reverseBits(n))  # 964176192

```

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

## 136. Single Number

-   [LeetCode](https://leetcode.com/problems/single-number/) | [LeetCode CH](https://leetcode.cn/problems/single-number/) (Easy)

-   Tags: array, bit manipulation

```python title="136. Single Number - Python Solution"
from functools import reduce
from operator import xor
from typing import List


# XOR
def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res


# XOR
def singleNumberXOR(nums: List[int]) -> int:
    return reduce(xor, nums)


# XOR
def singleNumberXORLambda(nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # 4
print(singleNumberXOR(nums))  # 4
print(singleNumberXORLambda(nums))  # 4

```

## 137. Single Number II

-   [LeetCode](https://leetcode.com/problems/single-number-ii/) | [LeetCode CH](https://leetcode.cn/problems/single-number-ii/) (Medium)

-   Tags: array, bit manipulation
## 201. Bitwise AND of Numbers Range

-   [LeetCode](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | [LeetCode CH](https://leetcode.cn/problems/bitwise-and-of-numbers-range/) (Medium)

-   Tags: bit manipulation
