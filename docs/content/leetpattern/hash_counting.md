---
comments: True
---

# Hash Counting

## Table of Contents

- [x] [242. Valid Anagram](https://leetcode.cn/problems/valid-anagram/) (Easy)
- [x] [560. Subarray Sum Equals K](https://leetcode.cn/problems/subarray-sum-equals-k/) (Medium)
- [x] [49. Group Anagrams](https://leetcode.cn/problems/group-anagrams/) (Medium)
- [x] [438. Find All Anagrams in a String](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)

## 242. Valid Anagram

-   [LeetCode](https://leetcode.com/problems/valid-anagram/) | [LeetCode CH](https://leetcode.cn/problems/valid-anagram/) (Easy)

-   Tags: hash table, string, sorting
-   Return true if an input string is an anagram of another string.
-   An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once, e.g., `listen` is an anagram of `silent`.

```python title="242. Valid Anagram - Python Solution"
from collections import Counter


# Hashmap
def isAnagramHash(s: str, t: str) -> bool:
    """Return True if t is an anagram of s, False otherwise."""
    if len(s) != len(t):
        return False

    count = dict()

    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for j in t:
        if j in count:
            count[j] -= 1
        else:
            return False

    for count in count.values():
        if count != 0:
            return False

    return True


# Array
def isAnagramArray(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0 for _ in range(26)]

    for i in s:
        count[ord(i) - ord("a")] += 1

    for j in t:
        count[ord(j) - ord("a")] -= 1

    for i in count:
        if i != 0:
            return False

    return True


# Counter
def isAnagramCounter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |   Hashmap   |       O(n)      |     O(1)     |
# |    Array    |       O(n)      |     O(1)     |
# |   Counter   |       O(n)      |     O(1)     |
# |-------------|-----------------|--------------|


s = "anagram"
t = "nagaram"
print(isAnagramHash(s, t))  # True
print(isAnagramArray(s, t))  # True
print(isAnagramCounter(s, t))  # True

```

## 560. Subarray Sum Equals K

-   [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/) | [LeetCode CH](https://leetcode.cn/problems/subarray-sum-equals-k/) (Medium)

-   Tags: array, hash table, prefix sum
```python title="560. Subarray Sum Equals K - Python Solution"
from collections import defaultdict
from typing import List


# Prefix Sum
def subarraySum(nums: List[int], k: int) -> int:
    preSums = defaultdict(int)
    preSums[0] = 1
    curSum = 0
    res = 0

    for num in nums:
        curSum += num
        res += preSums[curSum - k]
        preSums[curSum] += 1

    return res


nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # 2

```

```cpp title="560. Subarray Sum Equals K - C++ Solution"
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int subarraySum(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }

    int res = 0;
    unordered_map<int, int> cnt;

    for (int ps : prefixSum) {
        if (cnt.find(ps - k) != cnt.end()) res += cnt[ps - k];
        cnt[ps]++;
    }
    return res;
}

int main() {
    vector<int> nums = {1, 1, 1};
    int k = 2;
    cout << subarraySum(nums, k) << endl;  // 2
    return 0;
}
```

## 49. Group Anagrams

-   [LeetCode](https://leetcode.com/problems/group-anagrams/) | [LeetCode CH](https://leetcode.cn/problems/group-anagrams/) (Medium)

-   Tags: array, hash table, string, sorting
```python title="49. Group Anagrams - Python Solution"
from collections import defaultdict
from typing import List


# Hash - List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for i in s:
            count[ord(i) - ord("a")] += 1

        result[tuple(count)].append(s)

    return list(result.values())


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    Hash     |     O(n * k)    |     O(n)     |
# |-------------|-----------------|--------------|


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

```

## 438. Find All Anagrams in a String

-   [LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [LeetCode CH](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)

-   Tags: hash table, string, sliding window
```python title="438. Find All Anagrams in a String - Python Solution"
from typing import List


# Sliding Window Fixed Size
def findAnagrams(s: str, p: str) -> List[int]:
    n, k = len(s), len(p)
    target = [0 for _ in range(26)]
    for ch in p:
        target[ord(ch) - ord("a")] += 1

    count = [0 for _ in range(26)]
    left = 0
    res = []

    for right in range(n):
        count[ord(s[right]) - ord("a")] += 1
        if right < k - 1:
            continue

        if count == target:
            res.append(left)

        count[ord(s[left]) - ord("a")] -= 1
        left += 1

    return res


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))  # [0, 6]

```
