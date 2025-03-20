---
comments: True
---

# Hash

## Table of Contents

- [x] [1. Two Sum](https://leetcode.cn/problems/two-sum/) (Easy)
- [x] [49. Group Anagrams](https://leetcode.cn/problems/group-anagrams/) (Medium)
- [x] [128. Longest Consecutive Sequence](https://leetcode.cn/problems/longest-consecutive-sequence/) (Medium)

## 1. Two Sum

-   [LeetCode](https://leetcode.com/problems/two-sum/) | [LeetCode CH](https://leetcode.cn/problems/two-sum/) (Easy)

-   Tags: array, hash table
-   Return the indices of the two numbers such that they add up to a specific target.

| Approach | Time Complexity | Space Complexity |
| :------: | :-------------: | :--------------: |
| Hashmap  |      O(n)       |       O(n)       |

```python title="1. Two Sum - Python Solution"
from typing import List


# Hashmap
def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}  # val: idx

    for idx, val in enumerate(nums):
        if (target - val) in hashmap:
            return [hashmap[target - val], idx]

        hashmap[val] = idx


nums = [2, 7, 11, 15]
target = 18
assert twoSum(nums, target) == [1, 2]

```

```cpp title="1. Two Sum - C++ Solution"
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hashmap;

    for (size_t i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];

        if (hashmap.find(complement) != hashmap.end()) {
            return {hashmap[complement], (int)i};
        }
        hashmap[nums[i]] = (int)i;
    }

    return {-1, -1};
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(nums, target);
    cout << result[0] << ", " << result[1] << endl;
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

## 128. Longest Consecutive Sequence

-   [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-consecutive-sequence/) (Medium)

-   Tags: array, hash table, union find

```python title="128. Longest Consecutive Sequence - Python Solution"
from typing import List


# Set
def longestConsecutiveSet(nums: List[int]) -> int:
    num_set = set(nums)  # O(n)
    longest = 0

    for n in nums:
        if (n - 1) not in num_set:  # left boundary
            length = 1

            while (n + length) in num_set:
                length += 1

            longest = max(longest, length)

    return longest


# Union Find
def longestConsecutiveUF(nums: List[int]) -> int:
    if not nums:
        return 0

    par = {num: num for num in nums}
    rank = {num: 1 for num in nums}

    def find(num):
        p = par[num]
        while p != par[p]:
            p = par[p]
        return p

    def union(num1, num2):
        p1, p2 = find(num1), find(num2)
        if p1 == p2:
            return

        if rank[p1] < rank[p2]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]

    for num in nums:
        if num - 1 in par:
            union(num, num - 1)

    return max(rank.values())


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  Set       |  O(N)  |  O(N)   |
# | Union Find |  O(N)  |  O(N)   |
# |------------|--------|---------|


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutiveSet(nums))  # 4
print(longestConsecutiveUF(nums))  # 4

```
