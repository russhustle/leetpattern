---
comments: True
---

# DP Other DP

## Table of Contents

- [ ] [1387. Sort Integers by The Power Value](https://leetcode.cn/problems/sort-integers-by-the-power-value/) (Medium)
- [ ] [823. Binary Trees With Factors](https://leetcode.cn/problems/binary-trees-with-factors/) (Medium)
- [ ] [940. Distinct Subsequences II](https://leetcode.cn/problems/distinct-subsequences-ii/) (Hard)
- [x] [135. Candy](https://leetcode.cn/problems/candy/) (Hard)
- [ ] [650. 2 Keys Keyboard](https://leetcode.cn/problems/2-keys-keyboard/) (Medium)
- [ ] [638. Shopping Offers](https://leetcode.cn/problems/shopping-offers/) (Medium)
- [ ] [467. Unique Substrings in Wraparound String](https://leetcode.cn/problems/unique-substrings-in-wraparound-string/) (Medium)
- [ ] [2262. Total Appeal of A String](https://leetcode.cn/problems/total-appeal-of-a-string/) (Hard)
- [ ] [828. Count Unique Characters of All Substrings of a Given String](https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/) (Hard)
- [ ] [2746. Decremental String Concatenation](https://leetcode.cn/problems/decremental-string-concatenation/) (Medium)
- [ ] [2930. Number of Strings Which Can Be Rearranged to Contain Substring](https://leetcode.cn/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/) (Medium)
- [ ] [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/) (Hard)
- [ ] [818. Race Car](https://leetcode.cn/problems/race-car/) (Hard)
- [ ] [920. Number of Music Playlists](https://leetcode.cn/problems/number-of-music-playlists/) (Hard)
- [ ] [1388. Pizza With 3n Slices](https://leetcode.cn/problems/pizza-with-3n-slices/) (Hard)
- [ ] [1987. Number of Unique Good Subsequences](https://leetcode.cn/problems/number-of-unique-good-subsequences/) (Hard)
- [ ] [903. Valid Permutations for DI Sequence](https://leetcode.cn/problems/valid-permutations-for-di-sequence/) (Hard)
- [ ] [1896. Minimum Cost to Change the Final Value of Expression](https://leetcode.cn/problems/minimum-cost-to-change-the-final-value-of-expression/) (Hard)
- [ ] [1531. String Compression II](https://leetcode.cn/problems/string-compression-ii/) (Hard)
- [ ] [964. Least Operators to Express Number](https://leetcode.cn/problems/least-operators-to-express-number/) (Hard)
- [ ] [1787. Make the XOR of All Segments Equal to Zero](https://leetcode.cn/problems/make-the-xor-of-all-segments-equal-to-zero/) (Hard)
- [ ] [2060. Check if an Original String Exists Given Two Encoded Strings](https://leetcode.cn/problems/check-if-an-original-string-exists-given-two-encoded-strings/) (Hard)
- [ ] [2809. Minimum Time to Make Array Sum At Most x](https://leetcode.cn/problems/minimum-time-to-make-array-sum-at-most-x/) (Hard)
- [ ] [3299. Sum of Consecutive Subsequences](https://leetcode.cn/problems/sum-of-consecutive-subsequences/) (Hard) 👑
- [ ] [2189. Number of Ways to Build House of Cards](https://leetcode.cn/problems/number-of-ways-to-build-house-of-cards/) (Medium) 👑
- [x] [2597. The Number of Beautiful Subsets](https://leetcode.cn/problems/the-number-of-beautiful-subsets/) (Medium)
- [ ] [2638. Count the Number of K-Free Subsets](https://leetcode.cn/problems/count-the-number-of-k-free-subsets/) (Medium) 👑

## 1387. Sort Integers by The Power Value

-   [LeetCode](https://leetcode.com/problems/sort-integers-by-the-power-value/) | [LeetCode CH](https://leetcode.cn/problems/sort-integers-by-the-power-value/) (Medium)

-   Tags: dynamic programming, memoization, sorting
## 823. Binary Trees With Factors

-   [LeetCode](https://leetcode.com/problems/binary-trees-with-factors/) | [LeetCode CH](https://leetcode.cn/problems/binary-trees-with-factors/) (Medium)

-   Tags: array, hash table, dynamic programming, sorting
## 940. Distinct Subsequences II

-   [LeetCode](https://leetcode.com/problems/distinct-subsequences-ii/) | [LeetCode CH](https://leetcode.cn/problems/distinct-subsequences-ii/) (Hard)

-   Tags: string, dynamic programming
## 135. Candy

-   [LeetCode](https://leetcode.com/problems/candy/) | [LeetCode CH](https://leetcode.cn/problems/candy/) (Hard)

-   Tags: array, greedy
-   Return the minimum number of candies you must give.

```python title="135. Candy - Python Solution"
from typing import List


# Greedy
def candy(ratings: List[int]) -> int:
    # TC: O(n)
    # SC: O(n)
    n = len(ratings)

    if n <= 1:
        return n

    candy = [1 for _ in range(n)]

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candy[i] = candy[i - 1] + 1

    for j in range(n - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            candy[j] = max(candy[j], candy[j + 1] + 1)

    return sum(candy)


ratings = [1, 0, 2]
print(candy(ratings))  # 5

```

## 650. 2 Keys Keyboard

-   [LeetCode](https://leetcode.com/problems/2-keys-keyboard/) | [LeetCode CH](https://leetcode.cn/problems/2-keys-keyboard/) (Medium)

-   Tags: math, dynamic programming
## 638. Shopping Offers

-   [LeetCode](https://leetcode.com/problems/shopping-offers/) | [LeetCode CH](https://leetcode.cn/problems/shopping-offers/) (Medium)

-   Tags: array, dynamic programming, backtracking, bit manipulation, memoization, bitmask
## 467. Unique Substrings in Wraparound String

-   [LeetCode](https://leetcode.com/problems/unique-substrings-in-wraparound-string/) | [LeetCode CH](https://leetcode.cn/problems/unique-substrings-in-wraparound-string/) (Medium)

-   Tags: string, dynamic programming
## 2262. Total Appeal of A String

-   [LeetCode](https://leetcode.com/problems/total-appeal-of-a-string/) | [LeetCode CH](https://leetcode.cn/problems/total-appeal-of-a-string/) (Hard)

-   Tags: hash table, string, dynamic programming
## 828. Count Unique Characters of All Substrings of a Given String

-   [LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/) | [LeetCode CH](https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/) (Hard)

-   Tags: hash table, string, dynamic programming
## 2746. Decremental String Concatenation

-   [LeetCode](https://leetcode.com/problems/decremental-string-concatenation/) | [LeetCode CH](https://leetcode.cn/problems/decremental-string-concatenation/) (Medium)

-   Tags: array, string, dynamic programming
## 2930. Number of Strings Which Can Be Rearranged to Contain Substring

-   [LeetCode](https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/) | [LeetCode CH](https://leetcode.cn/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/) (Medium)

-   Tags: math, dynamic programming, combinatorics
## 1569. Number of Ways to Reorder Array to Get Same BST

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/) (Hard)

-   Tags: array, math, divide and conquer, dynamic programming, tree, union find, binary search tree, memoization, combinatorics, binary tree
## 818. Race Car

-   [LeetCode](https://leetcode.com/problems/race-car/) | [LeetCode CH](https://leetcode.cn/problems/race-car/) (Hard)

-   Tags: dynamic programming
## 920. Number of Music Playlists

-   [LeetCode](https://leetcode.com/problems/number-of-music-playlists/) | [LeetCode CH](https://leetcode.cn/problems/number-of-music-playlists/) (Hard)

-   Tags: math, dynamic programming, combinatorics
## 1388. Pizza With 3n Slices

-   [LeetCode](https://leetcode.com/problems/pizza-with-3n-slices/) | [LeetCode CH](https://leetcode.cn/problems/pizza-with-3n-slices/) (Hard)

-   Tags: array, dynamic programming, greedy, heap priority queue
## 1987. Number of Unique Good Subsequences

-   [LeetCode](https://leetcode.com/problems/number-of-unique-good-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/number-of-unique-good-subsequences/) (Hard)

-   Tags: string, dynamic programming
## 903. Valid Permutations for DI Sequence

-   [LeetCode](https://leetcode.com/problems/valid-permutations-for-di-sequence/) | [LeetCode CH](https://leetcode.cn/problems/valid-permutations-for-di-sequence/) (Hard)

-   Tags: string, dynamic programming, prefix sum
## 1896. Minimum Cost to Change the Final Value of Expression

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-change-the-final-value-of-expression/) (Hard)

-   Tags: math, string, dynamic programming, stack
## 1531. String Compression II

-   [LeetCode](https://leetcode.com/problems/string-compression-ii/) | [LeetCode CH](https://leetcode.cn/problems/string-compression-ii/) (Hard)

-   Tags: string, dynamic programming
## 964. Least Operators to Express Number

-   [LeetCode](https://leetcode.com/problems/least-operators-to-express-number/) | [LeetCode CH](https://leetcode.cn/problems/least-operators-to-express-number/) (Hard)

-   Tags: math, dynamic programming, memoization
## 1787. Make the XOR of All Segments Equal to Zero

-   [LeetCode](https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/) | [LeetCode CH](https://leetcode.cn/problems/make-the-xor-of-all-segments-equal-to-zero/) (Hard)

-   Tags: array, dynamic programming, bit manipulation
## 2060. Check if an Original String Exists Given Two Encoded Strings

-   [LeetCode](https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/) | [LeetCode CH](https://leetcode.cn/problems/check-if-an-original-string-exists-given-two-encoded-strings/) (Hard)

-   Tags: string, dynamic programming
## 2809. Minimum Time to Make Array Sum At Most x

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-make-array-sum-at-most-x/) (Hard)

-   Tags: array, dynamic programming, sorting
## 3299. Sum of Consecutive Subsequences

-   [LeetCode](https://leetcode.com/problems/sum-of-consecutive-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-consecutive-subsequences/) (Hard)

-   Tags: array, hash table, dynamic programming
## 2189. Number of Ways to Build House of Cards

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-build-house-of-cards/) (Medium)

-   Tags: math, dynamic programming
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

## 2638. Count the Number of K-Free Subsets

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-k-free-subsets/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-k-free-subsets/) (Medium)

-   Tags: array, math, dynamic programming, sorting, combinatorics
