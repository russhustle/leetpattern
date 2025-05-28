---
comments: True
---

# Sliding Window Variable Subarrays Exact

## Table of Contents

- [ ] [930. Binary Subarrays With Sum](https://leetcode.cn/problems/binary-subarrays-with-sum/) (Medium)
- [x] [1248. Count Number of Nice Subarrays](https://leetcode.cn/problems/count-number-of-nice-subarrays/) (Medium)
- [x] [3305. Count of Substrings Containing Every Vowel and K Consonants I](https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/) (Medium)
- [x] [3306. Count of Substrings Containing Every Vowel and K Consonants II](https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/) (Medium)
- [x] [992. Subarrays with K Different Integers](https://leetcode.cn/problems/subarrays-with-k-different-integers/) (Hard)

## 930. Binary Subarrays With Sum

-   [LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/) | [LeetCode CH](https://leetcode.cn/problems/binary-subarrays-with-sum/) (Medium)

-   Tags: array, hash table, sliding window, prefix sum
## 1248. Count Number of Nice Subarrays

-   [LeetCode](https://leetcode.com/problems/count-number-of-nice-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/count-number-of-nice-subarrays/) (Medium)

-   Tags: array, hash table, math, sliding window, prefix sum

```python title="1248. Count Number of Nice Subarrays - Python Solution"
from typing import List


# Prefix Sum
def numberOfSubarrays(nums: List[int], k: int) -> int:
    count = 0
    odd_counts = {0: 1}  # odd_count -> count
    odd_count = 0

    for num in nums:
        if num % 2 == 1:
            odd_count += 1
        if odd_count - k in odd_counts:
            count += odd_counts[odd_count - k]
        if odd_count in odd_counts:
            odd_counts[odd_count] += 1
        else:
            odd_counts[odd_count] = 1

    return count


nums = [1, 1, 2, 1, 1]
k = 3
print(numberOfSubarrays(nums, k))  # 2

```

## 3305. Count of Substrings Containing Every Vowel and K Consonants I

-   [LeetCode](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/) | [LeetCode CH](https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/) (Medium)

-   Tags: hash table, string, sliding window

```python title="3305. Count of Substrings Containing Every Vowel and K Consonants I - Python Solution"
from collections import defaultdict


# Sliding Window Variable Subarrays Exact
def countOfSubstrings(word: str, k: int) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    n = len(word)

    def count(m: int) -> int:
        occur = defaultdict(int)
        valid_vow_cnt, con_cnt = 0, 0
        left = 0
        res = 0

        for right in range(n):
            while left < n and (con_cnt < m or valid_vow_cnt < 5):
                if word[left] in vowels:
                    if occur[word[left]] == 0:
                        valid_vow_cnt += 1
                    occur[word[left]] += 1
                else:
                    con_cnt += 1
                left += 1

            if con_cnt >= m and valid_vow_cnt == 5:
                res += n - left + 1

            if word[right] in vowels:
                occur[word[right]] -= 1
                if occur[word[right]] == 0:
                    valid_vow_cnt -= 1
            else:
                con_cnt -= 1

        return res

    return count(k) - count(k + 1)


word = "ieaouqqieaouqq"
k = 1
print(countOfSubstrings(word, k))  # 3

```

## 3306. Count of Substrings Containing Every Vowel and K Consonants II

-   [LeetCode](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/) (Medium)

-   Tags: hash table, string, sliding window

```python title="3306. Count of Substrings Containing Every Vowel and K Consonants II - Python Solution"
from collections import defaultdict


# Sliding Window Variable Subarrays Exact
def countOfSubstrings(word: str, k: int) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    n = len(word)

    def count(m: int) -> int:
        occur = defaultdict(int)
        valid_vow_cnt, con_cnt = 0, 0
        left = 0
        res = 0

        for right in range(n):
            while left < n and (con_cnt < m or valid_vow_cnt < 5):
                if word[left] in vowels:
                    if occur[word[left]] == 0:
                        valid_vow_cnt += 1
                    occur[word[left]] += 1
                else:
                    con_cnt += 1
                left += 1

            if con_cnt >= m and valid_vow_cnt == 5:
                res += n - left + 1

            if word[right] in vowels:
                occur[word[right]] -= 1
                if occur[word[right]] == 0:
                    valid_vow_cnt -= 1
            else:
                con_cnt -= 1

        return res

    return count(k) - count(k + 1)


word = "ieaouqqieaouqq"
k = 1
print(countOfSubstrings(word, k))  # 3

```

## 992. Subarrays with K Different Integers

-   [LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/) | [LeetCode CH](https://leetcode.cn/problems/subarrays-with-k-different-integers/) (Hard)

-   Tags: array, hash table, sliding window, counting

```python title="992. Subarrays with K Different Integers - Python Solution"
from typing import List


# Sliding Window - Variable
def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    def atMost(k: int) -> int:
        count = 0
        left = 0
        freq = {}

        for right in range(len(nums)):
            if nums[right] not in freq:
                freq[nums[right]] = 0
            freq[nums[right]] += 1

            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            count += right - left + 1

        return count

    return atMost(k) - atMost(k - 1)


nums = [1, 2, 1, 2, 3]
k = 2
print(subarraysWithKDistinct(nums, k))  # 7

```
