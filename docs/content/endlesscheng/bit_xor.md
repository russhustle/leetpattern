---
comments: True
---

# Bit XOR

## Table of Contents

- [ ] [1486. XOR Operation in an Array](https://leetcode.cn/problems/xor-operation-in-an-array/) (Easy)
- [ ] [1720. Decode XORed Array](https://leetcode.cn/problems/decode-xored-array/) (Easy)
- [ ] [2433. Find The Original Array of Prefix Xor](https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/) (Medium)
- [ ] [1310. XOR Queries of a Subarray](https://leetcode.cn/problems/xor-queries-of-a-subarray/) (Medium)
- [ ] [2683. Neighboring Bitwise XOR](https://leetcode.cn/problems/neighboring-bitwise-xor/) (Medium)
- [ ] [1829. Maximum XOR for Each Query](https://leetcode.cn/problems/maximum-xor-for-each-query/) (Medium)
- [ ] [2997. Minimum Number of Operations to Make Array XOR Equal to K](https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/) (Medium)
- [ ] [1442. Count Triplets That Can Form Two Arrays of Equal XOR](https://leetcode.cn/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) (Medium)
- [ ] [2429. Minimize XOR](https://leetcode.cn/problems/minimize-xor/) (Medium)
- [ ] [2527. Find Xor-Beauty of Array](https://leetcode.cn/problems/find-xor-beauty-of-array/) (Medium)
- [ ] [2317. Maximum XOR After Operations ](https://leetcode.cn/problems/maximum-xor-after-operations/) (Medium)
- [x] [2588. Count the Number of Beautiful Subarrays](https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays/) (Medium)
- [ ] [2564. Substring XOR Queries](https://leetcode.cn/problems/substring-xor-queries/) (Medium)
- [ ] [1734. Decode XORed Permutation](https://leetcode.cn/problems/decode-xored-permutation/) (Medium)
- [ ] [2857. Count Pairs of Points With Distance k](https://leetcode.cn/problems/count-pairs-of-points-with-distance-k/) (Medium)
- [ ] [1803. Count Pairs With XOR in a Range](https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/) (Hard)
- [ ] [3215. Count Triplets with Even XOR Set Bits II](https://leetcode.cn/problems/count-triplets-with-even-xor-set-bits-ii/) (Medium) 👑

## 1486. XOR Operation in an Array

-   [LeetCode](https://leetcode.com/problems/xor-operation-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/xor-operation-in-an-array/) (Easy)

-   Tags: math, bit manipulation
## 1720. Decode XORed Array

-   [LeetCode](https://leetcode.com/problems/decode-xored-array/) | [LeetCode CH](https://leetcode.cn/problems/decode-xored-array/) (Easy)

-   Tags: array, bit manipulation
## 2433. Find The Original Array of Prefix Xor

-   [LeetCode](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/) | [LeetCode CH](https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/) (Medium)

-   Tags: array, bit manipulation
## 1310. XOR Queries of a Subarray

-   [LeetCode](https://leetcode.com/problems/xor-queries-of-a-subarray/) | [LeetCode CH](https://leetcode.cn/problems/xor-queries-of-a-subarray/) (Medium)

-   Tags: array, bit manipulation, prefix sum
## 2683. Neighboring Bitwise XOR

-   [LeetCode](https://leetcode.com/problems/neighboring-bitwise-xor/) | [LeetCode CH](https://leetcode.cn/problems/neighboring-bitwise-xor/) (Medium)

-   Tags: array, bit manipulation
## 1829. Maximum XOR for Each Query

-   [LeetCode](https://leetcode.com/problems/maximum-xor-for-each-query/) | [LeetCode CH](https://leetcode.cn/problems/maximum-xor-for-each-query/) (Medium)

-   Tags: array, bit manipulation, prefix sum
## 2997. Minimum Number of Operations to Make Array XOR Equal to K

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/) (Medium)

-   Tags: array, bit manipulation
## 1442. Count Triplets That Can Form Two Arrays of Equal XOR

-   [LeetCode](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) | [LeetCode CH](https://leetcode.cn/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) (Medium)

-   Tags: array, hash table, math, bit manipulation, prefix sum
## 2429. Minimize XOR

-   [LeetCode](https://leetcode.com/problems/minimize-xor/) | [LeetCode CH](https://leetcode.cn/problems/minimize-xor/) (Medium)

-   Tags: greedy, bit manipulation
## 2527. Find Xor-Beauty of Array

-   [LeetCode](https://leetcode.com/problems/find-xor-beauty-of-array/) | [LeetCode CH](https://leetcode.cn/problems/find-xor-beauty-of-array/) (Medium)

-   Tags: array, math, bit manipulation
## 2317. Maximum XOR After Operations 

-   [LeetCode](https://leetcode.com/problems/maximum-xor-after-operations/) | [LeetCode CH](https://leetcode.cn/problems/maximum-xor-after-operations/) (Medium)

-   Tags: array, math, bit manipulation
## 2588. Count the Number of Beautiful Subarrays

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays/) (Medium)

-   Tags: array, hash table, bit manipulation, prefix sum
- `nums = [4, 3, 1, 2, 4]`
- In bianry

```
4 -> 100
3 -> 011
1 -> 001
2 -> 010
4 -> 100
```

```python title="2588. Count the Number of Beautiful Subarrays - Python Solution"
from collections import defaultdict
from typing import List


def beautifulSubarrays(nums: List[int]) -> int:
    res, s = 0, 0
    cnt = defaultdict(int)
    cnt[0] = 1

    for x in nums:
        s ^= x
        res += cnt[s]
        cnt[s] += 1

    return res


nums = [4, 3, 1, 2, 4]
print(beautifulSubarrays(nums))  # 2

```

## 2564. Substring XOR Queries

-   [LeetCode](https://leetcode.com/problems/substring-xor-queries/) | [LeetCode CH](https://leetcode.cn/problems/substring-xor-queries/) (Medium)

-   Tags: array, hash table, string, bit manipulation
## 1734. Decode XORed Permutation

-   [LeetCode](https://leetcode.com/problems/decode-xored-permutation/) | [LeetCode CH](https://leetcode.cn/problems/decode-xored-permutation/) (Medium)

-   Tags: array, bit manipulation
## 2857. Count Pairs of Points With Distance k

-   [LeetCode](https://leetcode.com/problems/count-pairs-of-points-with-distance-k/) | [LeetCode CH](https://leetcode.cn/problems/count-pairs-of-points-with-distance-k/) (Medium)

-   Tags: array, hash table, bit manipulation
## 1803. Count Pairs With XOR in a Range

-   [LeetCode](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/) | [LeetCode CH](https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/) (Hard)

-   Tags: array, bit manipulation, trie
## 3215. Count Triplets with Even XOR Set Bits II

-   [LeetCode](https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-triplets-with-even-xor-set-bits-ii/) (Medium)

-   Tags: array, bit manipulation
