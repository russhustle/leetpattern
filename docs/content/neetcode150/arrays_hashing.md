---
comments: True
---

# Arrays Hashing

## Table of Contents

- [x] [217. Contains Duplicate](https://leetcode.cn/problems/contains-duplicate/) (Easy)
- [x] [242. Valid Anagram](https://leetcode.cn/problems/valid-anagram/) (Easy)
- [x] [1. Two Sum](https://leetcode.cn/problems/two-sum/) (Easy)
- [x] [49. Group Anagrams](https://leetcode.cn/problems/group-anagrams/) (Medium)
- [x] [347. Top K Frequent Elements](https://leetcode.cn/problems/top-k-frequent-elements/) (Medium)
- [x] [271. Encode and Decode Strings](https://leetcode.cn/problems/encode-and-decode-strings/) (Medium) 👑
- [x] [238. Product of Array Except Self](https://leetcode.cn/problems/product-of-array-except-self/) (Medium)
- [x] [36. Valid Sudoku](https://leetcode.cn/problems/valid-sudoku/) (Medium)
- [x] [128. Longest Consecutive Sequence](https://leetcode.cn/problems/longest-consecutive-sequence/) (Medium)

## 217. Contains Duplicate

-   [LeetCode](https://leetcode.com/problems/contains-duplicate/) | [LeetCode CH](https://leetcode.cn/problems/contains-duplicate/) (Easy)

-   Tags: array, hash table, sorting
-   Return True if the array contains any duplicates, otherwise return False.


```python title="217. Contains Duplicate - Python Solution"
from typing import List


# Brute Force
def containsDuplicateBF(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


# Sort
def containsDuplicateSort(nums: List[int]) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False


# Set
def containsDuplicateSet(nums: List[int]) -> bool:
    seen = set()

    for i in nums:
        if i in seen:
            return True
        seen.add(i)

    return False


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# | Brute Force |    O(n^2)       |    O(1)      |
# |     Sort    |    O(n log n)   |    O(1)      |
# |     Set     |    O(n)         |    O(n)      |
# |-------------|-----------------|--------------|

print(containsDuplicateBF([1, 2, 3, 1]))  # True
print(containsDuplicateSort([1, 2, 3, 1]))  # True
print(containsDuplicateSet([1, 2, 3, 1]))  # True

```

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

## 1. Two Sum

-   [LeetCode](https://leetcode.com/problems/two-sum/) | [LeetCode CH](https://leetcode.cn/problems/two-sum/) (Easy)

-   Tags: array, hash table
- Return the indices of the two numbers such that they add up to a specific target.
- Approach: Use a hashmap to store the indices of the numbers.
- Time Complexity: O(n)
- Space Complexity: O(n)


```python title="1. Two Sum - Python Solution"
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}  # val: idx

    for idx, val in enumerate(nums):
        if (target - val) in hashmap:
            return [hashmap[target - val], idx]

        hashmap[val] = idx


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert twoSum(nums, target) == [0, 1]

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

## 347. Top K Frequent Elements

-   [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) | [LeetCode CH](https://leetcode.cn/problems/top-k-frequent-elements/) (Medium)

-   Tags: array, hash table, divide and conquer, sorting, heap priority queue, bucket sort, counting, quickselect

```python title="347. Top K Frequent Elements - Python Solution"
import heapq
from collections import Counter
from typing import List


# Heap + Counter
def topKFrequent(nums: List[int], k: int) -> List[int]:
    minHeap = []

    for val, freq in Counter(nums).items():
        if len(minHeap) < k:
            heapq.heappush(minHeap, (freq, val))
        else:
            heapq.heappushpop(minHeap, (freq, val))

    return [i for _, i in minHeap]


# Counter (Most Common)
def topKFrequentCounter(nums: List[int], k: int) -> List[int]:
    commons = Counter(nums).most_common(k)
    return [i for i, _ in commons]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # [1, 2]
print(topKFrequentCounter(nums, k))  # [1, 2]

```

## 271. Encode and Decode Strings

-   [LeetCode](https://leetcode.com/problems/encode-and-decode-strings/) | [LeetCode CH](https://leetcode.cn/problems/encode-and-decode-strings/) (Medium)

-   Tags: array, string, design

```python title="271. Encode and Decode Strings - Python Solution"
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            strLen = int(s[i:j])
            decoded.append(s[j + 1 : j + 1 + strLen])
            i = j + 1 + strLen

        return decoded


# |-------------|-------------|--------------|
# |   Approach  |    Time     |    Space     |
# |-------------|-------------|--------------|
# | Two pointers|    O(n)     |     O(n)     |
# |-------------|-------------|--------------|


codec = Codec()
encoded = codec.encode(["hello", "world"])
print(encoded)  # "5#hello5#world"
decoded = codec.decode(encoded)
print(decoded)  # ["hello", "world"]

```

## 238. Product of Array Except Self

-   [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) | [LeetCode CH](https://leetcode.cn/problems/product-of-array-except-self/) (Medium)

-   Tags: array, prefix sum
-   Classic **Prefix Sum** problem
-   Return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

| Approach           | Time | Space |
| ------------------ | ---- | ----- |
| Prefix             | O(n) | O(n)  |
| Prefix (Optimized) | O(n) | O(1)  |


```python title="238. Product of Array Except Self - Python Solution"
from typing import List


# Prefix
def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [1 for _ in range(n)]
    suffix = [1 for _ in range(n)]

    for i in range(1, n):
        prefix[i] = nums[i - 1] * prefix[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = nums[i + 1] * suffix[i + 1]

    result = [i * j for i, j in zip(prefix, suffix)]

    return result


# Prefix (Optimized)
def productExceptSelfOptimized(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1 for _ in range(n)]

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


print(productExceptSelf([1, 2, 3, 4]))
# [24, 12, 8, 6]
print(productExceptSelfOptimized([1, 2, 3, 4]))
# [24, 12, 8, 6]

```

```cpp title="238. Product of Array Except Self - C++ Solution"
#include <vector>
#include <iostream>
using namespace std;

// Prefix Sum
class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> prefix(n, 1);
        vector<int> suffix(n, 1);
        vector<int> res(n, 1);

        for (int i = 1; i < n; i++)
        {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        for (int i = n - 2; i >= 0; i--)
        {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < n; i++)
        {
            res[i] = prefix[i] * suffix[i];
        }
        return res;
    }
};

int main()
{
    vector<int> nums = {1, 2, 3, 4};
    Solution obj;
    vector<int> result = obj.productExceptSelf(nums);

    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << "\n";
    }
    cout << endl;
    // 24, 12, 8, 6
    return 0;
}

```

## 36. Valid Sudoku

-   [LeetCode](https://leetcode.com/problems/valid-sudoku/) | [LeetCode CH](https://leetcode.cn/problems/valid-sudoku/) (Medium)

-   Tags: array, hash table, matrix

```python title="36. Valid Sudoku - Python Solution"
from typing import List


# Set
def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue

            if board[i][j] in rows[i]:
                return False
            rows[i].add(board[i][j])

            if board[i][j] in cols[j]:
                return False
            cols[j].add(board[i][j])

            box_index = (i // 3) * 3 + j // 3
            if board[i][j] in boxes[box_index]:
                return False
            boxes[box_index].add(board[i][j])

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))  # True

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
