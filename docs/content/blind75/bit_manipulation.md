---
comments: True
---

# Bit Manipulation

- [x] [191. Number of 1 Bits](https://leetcode.cn/problems/number-of-1-bits/) (Easy)
- [x] [338. Counting Bits](https://leetcode.cn/problems/counting-bits/) (Easy)
- [x] [190. Reverse Bits](https://leetcode.cn/problems/reverse-bits/) (Easy)
- [x] [268. Missing Number](https://leetcode.cn/problems/missing-number/) (Easy)
- [x] [371. Sum of Two Integers](https://leetcode.cn/problems/sum-of-two-integers/) (Medium)

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

## 268. Missing Number

-   [LeetCode](https://leetcode.com/problems/missing-number/) | [LeetCode CH](https://leetcode.cn/problems/missing-number/) (Easy)

-   Tags: array, hash table, math, binary search, bit manipulation, sorting

```python title="268. Missing Number - Python Solution"
from typing import List


# Math
def missingNumberMath(nums: List[int]) -> int:
    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)


# Bit Manipulation (XOR)
def missingNumberXOR(nums: List[int]) -> int:
    n = len(nums)

    for i, num in enumerate(nums):
        n ^= i ^ num

    return n


nums = [3, 0, 1]
print(missingNumberMath(nums))  # 2
print(missingNumberXOR(nums))  # 2

```

## 371. Sum of Two Integers

-   [LeetCode](https://leetcode.com/problems/sum-of-two-integers/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-two-integers/) (Medium)

-   Tags: math, bit manipulation

```python title="371. Sum of Two Integers - Python Solution"
# Bit Manipulation
def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        temp = (a ^ b) & MASK
        b = ((a & b) << 1) & MASK
        a = temp

    return a if a <= MAX_INT else ~(a ^ MASK)


print(getSum(1, 2))  # 3

```
