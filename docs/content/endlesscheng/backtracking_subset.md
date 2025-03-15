---
comments: True
---

# Backtracking Subset

- [x] [78. Subsets](https://leetcode.cn/problems/subsets/) (Medium)
- [ ] [784. Letter Case Permutation](https://leetcode.cn/problems/letter-case-permutation/) (Medium)
- [ ] [1286. Iterator for Combination](https://leetcode.cn/problems/iterator-for-combination/) (Medium)
- [x] [494. Target Sum](https://leetcode.cn/problems/target-sum/) (Medium)
- [ ] [2397. Maximum Rows Covered by Columns](https://leetcode.cn/problems/maximum-rows-covered-by-columns/) (Medium)
- [ ] [1239. Maximum Length of a Concatenated String with Unique Characters](https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) (Medium)
- [ ] [2212. Maximum Points in an Archery Competition](https://leetcode.cn/problems/maximum-points-in-an-archery-competition/) (Medium)
- [ ] [1255. Maximum Score Words Formed by Letters](https://leetcode.cn/problems/maximum-score-words-formed-by-letters/) (Hard)
- [ ] [2151. Maximum Good People Based on Statements](https://leetcode.cn/problems/maximum-good-people-based-on-statements/) (Hard)
- [x] [2597. The Number of Beautiful Subsets](https://leetcode.cn/problems/the-number-of-beautiful-subsets/) (Medium)
- [ ] [2959. Number of Possible Sets of Closing Branches](https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/) (Hard)
- [ ] [1601. Maximum Number of Achievable Transfer Requests](https://leetcode.cn/problems/maximum-number-of-achievable-transfer-requests/) (Hard)
- [ ] [1617. Count Subtrees With Max Distance Between Cities](https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/) (Hard)
- [ ] [320. Generalized Abbreviation](https://leetcode.cn/problems/generalized-abbreviation/) (Medium) 👑
- [ ] [254. Factor Combinations](https://leetcode.cn/problems/factor-combinations/) (Medium) 👑
- [x] [39. Combination Sum](https://leetcode.cn/problems/combination-sum/) (Medium)

## 78. Subsets

-   [LeetCode](https://leetcode.com/problems/subsets/) | [LeetCode CH](https://leetcode.cn/problems/subsets/) (Medium)

-   Tags: array, backtracking, bit manipulation

```python title="78. Subsets - Python Solution"
from typing import List


# Iterative Inclusion Backtracking
def subsets_iterative_inclusion(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res, path = [], []

    def dfs(i):
        res.append(path.copy())

        for j in range(i, n):
            path.append(nums[j])
            dfs(j + 1)
            path.pop()

    dfs(0)

    return res


# Binary Decision Backtracking
def subsets_binary_decision(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res, path = [], []

    def dfs(i):
        if i == n:
            res.append(path.copy())
            return

        # Exclude
        dfs(i + 1)

        # Include
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

    dfs(0)

    return res


print(subsets_iterative_inclusion([1, 2, 3]))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(subsets_binary_decision([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

```

## 784. Letter Case Permutation

-   [LeetCode](https://leetcode.com/problems/letter-case-permutation/) | [LeetCode CH](https://leetcode.cn/problems/letter-case-permutation/) (Medium)

-   Tags: string, backtracking, bit manipulation

## 1286. Iterator for Combination

-   [LeetCode](https://leetcode.com/problems/iterator-for-combination/) | [LeetCode CH](https://leetcode.cn/problems/iterator-for-combination/) (Medium)

-   Tags: string, backtracking, design, iterator

## 494. Target Sum

-   [LeetCode](https://leetcode.com/problems/target-sum/) | [LeetCode CH](https://leetcode.cn/problems/target-sum/) (Medium)

-   Tags: array, dynamic programming, backtracking

```python title="494. Target Sum - Python Solution"
from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:

    totalSum = sum(nums)

    if abs(target) > totalSum:
        return 0
    if (target + totalSum) % 2 == 1:
        return 0

    targetSum = (target + totalSum) // 2
    dp = [0] * (targetSum + 1)
    dp[0] = 1

    for i in range(len(nums)):
        for j in range(targetSum, nums[i] - 1, -1):
            dp[j] += dp[j - nums[i]]

    return dp[targetSum]


nums = [1, 1, 1, 1, 1]
target = 3
print(findTargetSumWays(nums, target))  # 5

```

## 2397. Maximum Rows Covered by Columns

-   [LeetCode](https://leetcode.com/problems/maximum-rows-covered-by-columns/) | [LeetCode CH](https://leetcode.cn/problems/maximum-rows-covered-by-columns/) (Medium)

-   Tags: array, backtracking, bit manipulation, matrix, enumeration

## 1239. Maximum Length of a Concatenated String with Unique Characters

-   [LeetCode](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) | [LeetCode CH](https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) (Medium)

-   Tags: array, string, backtracking, bit manipulation

## 2212. Maximum Points in an Archery Competition

-   [LeetCode](https://leetcode.com/problems/maximum-points-in-an-archery-competition/) | [LeetCode CH](https://leetcode.cn/problems/maximum-points-in-an-archery-competition/) (Medium)

-   Tags: array, backtracking, bit manipulation, enumeration

## 1255. Maximum Score Words Formed by Letters

-   [LeetCode](https://leetcode.com/problems/maximum-score-words-formed-by-letters/) | [LeetCode CH](https://leetcode.cn/problems/maximum-score-words-formed-by-letters/) (Hard)

-   Tags: array, string, dynamic programming, backtracking, bit manipulation, bitmask

## 2151. Maximum Good People Based on Statements

-   [LeetCode](https://leetcode.com/problems/maximum-good-people-based-on-statements/) | [LeetCode CH](https://leetcode.cn/problems/maximum-good-people-based-on-statements/) (Hard)

-   Tags: array, backtracking, bit manipulation, enumeration

## 2597. The Number of Beautiful Subsets

-   [LeetCode](https://leetcode.com/problems/the-number-of-beautiful-subsets/) | [LeetCode CH](https://leetcode.cn/problems/the-number-of-beautiful-subsets/) (Medium)

-   Tags: array, hash table, math, dynamic programming, backtracking, sorting, combinatorics

```cpp title="2597. The Number of Beautiful Subsets - C++ Solution"
#include <functional>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int res = 0;
        unordered_map<int, int> cnt;

        auto dfs = [&](auto&& self, int i) -> void {
            if (i == (int)nums.size()) {
                res++;
                return;
            }
            self(self, i + 1);  // Skip nums[i]
            int x = nums[i];
            if (cnt[x - k] == 0 && cnt[x + k] == 0) {
                cnt[x]++;
                self(self, i + 1);  // Include nums[i]
                cnt[x]--;           // Backtrack
            }
        };

        dfs(dfs, 0);

        return res - 1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    int k = 1;
    cout << sol.beautifulSubsets(nums, k) << endl;
    return 0;
}

```

## 2959. Number of Possible Sets of Closing Branches

-   [LeetCode](https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/) | [LeetCode CH](https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches/) (Hard)

-   Tags: bit manipulation, graph, heap priority queue, enumeration, shortest path

## 1601. Maximum Number of Achievable Transfer Requests

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-achievable-transfer-requests/) (Hard)

-   Tags: array, backtracking, bit manipulation, enumeration

## 1617. Count Subtrees With Max Distance Between Cities

-   [LeetCode](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/) | [LeetCode CH](https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/) (Hard)

-   Tags: dynamic programming, bit manipulation, tree, enumeration, bitmask

## 320. Generalized Abbreviation

-   [LeetCode](https://leetcode.com/problems/generalized-abbreviation/) | [LeetCode CH](https://leetcode.cn/problems/generalized-abbreviation/) (Medium)

-   Tags: string, backtracking, bit manipulation

## 254. Factor Combinations

-   [LeetCode](https://leetcode.com/problems/factor-combinations/) | [LeetCode CH](https://leetcode.cn/problems/factor-combinations/) (Medium)

-   Tags: backtracking

## 39. Combination Sum

-   [LeetCode](https://leetcode.com/problems/combination-sum/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum/) (Medium)

-   Tags: array, backtracking

```python title="39. Combination Sum - Python Solution"
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    path = []

    def backtracking(total, start):
        if total > target:
            return None
        if total == target:
            result.append(path[:])
            return None

        for i in range(start, len(candidates)):
            total += candidates[i]
            path.append(candidates[i])

            backtracking(total, i)

            total -= candidates[i]
            path.pop()

    backtracking(0, 0)
    return result


print(combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]

```
