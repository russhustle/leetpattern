---
comments: True
---

# Combinatorial Counting

## Table of Contents

- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)
- [ ] [357. Count Numbers with Unique Digits](https://leetcode.cn/problems/count-numbers-with-unique-digits/) (Medium)
- [ ] [1175. Prime Arrangements](https://leetcode.cn/problems/prime-arrangements/) (Easy)
- [ ] [3179. Find the N-th Value After K Seconds](https://leetcode.cn/problems/find-the-n-th-value-after-k-seconds/) (Medium)
- [ ] [1359. Count All Valid Pickup and Delivery Options](https://leetcode.cn/problems/count-all-valid-pickup-and-delivery-options/) (Hard)
- [ ] [2400. Number of Ways to Reach a Position After Exactly k Steps](https://leetcode.cn/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) (Medium)
- [ ] [2514. Count Anagrams](https://leetcode.cn/problems/count-anagrams/) (Hard)
- [ ] [3154. Find Number of Ways to Reach the K-th Stair](https://leetcode.cn/problems/find-number-of-ways-to-reach-the-k-th-stair/) (Hard)
- [ ] [1643. Kth Smallest Instructions](https://leetcode.cn/problems/kth-smallest-instructions/) (Hard)
- [ ] [2842. Count K-Subsequences of a String With Maximum Beauty](https://leetcode.cn/problems/count-k-subsequences-of-a-string-with-maximum-beauty/) (Hard)
- [ ] [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/) (Hard)
- [ ] [3405. Count the Number of Arrays with K Matching Adjacent Elements](https://leetcode.cn/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/) (Hard)
- [ ] [1866. Number of Ways to Rearrange Sticks With K Sticks Visible](https://leetcode.cn/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/) (Hard)
- [ ] [1467. Probability of a Two Boxes Having The Same Number of Distinct Balls](https://leetcode.cn/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/) (Hard)
- [ ] [3272. Find the Count of Good Integers](https://leetcode.cn/problems/find-the-count-of-good-integers/) (Hard)
- [ ] [3317. Find the Number of Possible Ways for an Event](https://leetcode.cn/problems/find-the-number-of-possible-ways-for-an-event/) (Hard)
- [ ] [1916. Count Ways to Build Rooms in an Ant Colony](https://leetcode.cn/problems/count-ways-to-build-rooms-in-an-ant-colony/) (Hard)
- [ ] [3343. Count Number of Balanced Permutations](https://leetcode.cn/problems/count-number-of-balanced-permutations/) (Hard)
- [ ] [1830. Minimum Number of Operations to Make String Sorted](https://leetcode.cn/problems/minimum-number-of-operations-to-make-string-sorted/) (Hard)
- [ ] [2954. Count the Number of Infection Sequences](https://leetcode.cn/problems/count-the-number-of-infection-sequences/) (Hard)
- [ ] [3395. Subsequences with a Unique Middle Mode I](https://leetcode.cn/problems/subsequences-with-a-unique-middle-mode-i/) (Hard)
- [ ] [1575. Count All Possible Routes](https://leetcode.cn/problems/count-all-possible-routes/) (Hard)
- [ ] [3251. Find the Count of Monotonic Pairs II](https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/) (Hard)
- [ ] [2539. Count the Number of Good Subsequences](https://leetcode.cn/problems/count-the-number-of-good-subsequences/) (Medium) 👑
- [ ] [634. Find the Derangement of An Array](https://leetcode.cn/problems/find-the-derangement-of-an-array/) (Medium) 👑
- [ ] [1692. Count Ways to Distribute Candies](https://leetcode.cn/problems/count-ways-to-distribute-candies/) (Hard) 👑

## 62. Unique Paths

-   [LeetCode](https://leetcode.com/problems/unique-paths/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths/) (Medium)

-   Tags: math, dynamic programming, combinatorics
-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid.

![62](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)


```python title="62. Unique Paths - Python Solution"
# DP - 2D
def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


print(uniquePaths(m=3, n=7))  # 28
# [[1, 1, 1,  1,  1,  1,  1],
#  [1, 2, 3,  4,  5,  6,  7],
#  [1, 3, 6, 10, 15, 21, 28]]

```

```cpp title="62. Unique Paths - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

int uniquePaths(int m, int n) {
    vector dp(m, vector<int>(n, 1));

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }

    return dp[m - 1][n - 1];
}

int main() {
    int m = 3, n = 7;
    cout << uniquePaths(m, n) << endl;  // 28
    return 0;
}

```

## 357. Count Numbers with Unique Digits

-   [LeetCode](https://leetcode.com/problems/count-numbers-with-unique-digits/) | [LeetCode CH](https://leetcode.cn/problems/count-numbers-with-unique-digits/) (Medium)

-   Tags: math, dynamic programming, backtracking
## 1175. Prime Arrangements

-   [LeetCode](https://leetcode.com/problems/prime-arrangements/) | [LeetCode CH](https://leetcode.cn/problems/prime-arrangements/) (Easy)

-   Tags: math
## 3179. Find the N-th Value After K Seconds

-   [LeetCode](https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/) | [LeetCode CH](https://leetcode.cn/problems/find-the-n-th-value-after-k-seconds/) (Medium)

-   Tags: array, math, simulation, combinatorics, prefix sum
## 1359. Count All Valid Pickup and Delivery Options

-   [LeetCode](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/) | [LeetCode CH](https://leetcode.cn/problems/count-all-valid-pickup-and-delivery-options/) (Hard)

-   Tags: math, dynamic programming, combinatorics
## 2400. Number of Ways to Reach a Position After Exactly k Steps

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) (Medium)

-   Tags: math, dynamic programming, combinatorics
## 2514. Count Anagrams

-   [LeetCode](https://leetcode.com/problems/count-anagrams/) | [LeetCode CH](https://leetcode.cn/problems/count-anagrams/) (Hard)

-   Tags: hash table, math, string, combinatorics, counting
## 3154. Find Number of Ways to Reach the K-th Stair

-   [LeetCode](https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/) | [LeetCode CH](https://leetcode.cn/problems/find-number-of-ways-to-reach-the-k-th-stair/) (Hard)

-   Tags: math, dynamic programming, bit manipulation, memoization, combinatorics
## 1643. Kth Smallest Instructions

-   [LeetCode](https://leetcode.com/problems/kth-smallest-instructions/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-instructions/) (Hard)

-   Tags: array, math, dynamic programming, combinatorics
## 2842. Count K-Subsequences of a String With Maximum Beauty

-   [LeetCode](https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/) | [LeetCode CH](https://leetcode.cn/problems/count-k-subsequences-of-a-string-with-maximum-beauty/) (Hard)

-   Tags: hash table, math, string, greedy, combinatorics
## 1569. Number of Ways to Reorder Array to Get Same BST

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/) (Hard)

-   Tags: array, math, divide and conquer, dynamic programming, tree, union find, binary search tree, memoization, combinatorics, binary tree
## 3405. Count the Number of Arrays with K Matching Adjacent Elements

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/) (Hard)

-   Tags: math, combinatorics
## 1866. Number of Ways to Rearrange Sticks With K Sticks Visible

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/) (Hard)

-   Tags: math, dynamic programming, combinatorics
## 1467. Probability of a Two Boxes Having The Same Number of Distinct Balls

-   [LeetCode](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/) | [LeetCode CH](https://leetcode.cn/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/) (Hard)

-   Tags: array, math, dynamic programming, backtracking, combinatorics, probability and statistics
## 3272. Find the Count of Good Integers

-   [LeetCode](https://leetcode.com/problems/find-the-count-of-good-integers/) | [LeetCode CH](https://leetcode.cn/problems/find-the-count-of-good-integers/) (Hard)

-   Tags: hash table, math, combinatorics, enumeration
## 3317. Find the Number of Possible Ways for an Event

-   [LeetCode](https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/) | [LeetCode CH](https://leetcode.cn/problems/find-the-number-of-possible-ways-for-an-event/) (Hard)

-   Tags: math, dynamic programming, combinatorics
## 1916. Count Ways to Build Rooms in an Ant Colony

-   [LeetCode](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/) | [LeetCode CH](https://leetcode.cn/problems/count-ways-to-build-rooms-in-an-ant-colony/) (Hard)

-   Tags: math, dynamic programming, tree, graph, topological sort, combinatorics
## 3343. Count Number of Balanced Permutations

-   [LeetCode](https://leetcode.com/problems/count-number-of-balanced-permutations/) | [LeetCode CH](https://leetcode.cn/problems/count-number-of-balanced-permutations/) (Hard)

-   Tags: math, string, dynamic programming, combinatorics
## 1830. Minimum Number of Operations to Make String Sorted

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-operations-to-make-string-sorted/) (Hard)

-   Tags: math, string, combinatorics
## 2954. Count the Number of Infection Sequences

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-infection-sequences/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-infection-sequences/) (Hard)

-   Tags: array, math, combinatorics
## 3395. Subsequences with a Unique Middle Mode I

-   [LeetCode](https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/) | [LeetCode CH](https://leetcode.cn/problems/subsequences-with-a-unique-middle-mode-i/) (Hard)

-   Tags: array, hash table, math, combinatorics
## 1575. Count All Possible Routes

-   [LeetCode](https://leetcode.com/problems/count-all-possible-routes/) | [LeetCode CH](https://leetcode.cn/problems/count-all-possible-routes/) (Hard)

-   Tags: array, dynamic programming, memoization
## 3251. Find the Count of Monotonic Pairs II

-   [LeetCode](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/) (Hard)

-   Tags: array, math, dynamic programming, combinatorics, prefix sum
## 2539. Count the Number of Good Subsequences

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-good-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-good-subsequences/) (Medium)

-   Tags: hash table, math, string, combinatorics, counting
## 634. Find the Derangement of An Array

-   [LeetCode](https://leetcode.com/problems/find-the-derangement-of-an-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-derangement-of-an-array/) (Medium)

-   Tags: math, dynamic programming, combinatorics
## 1692. Count Ways to Distribute Candies

-   [LeetCode](https://leetcode.com/problems/count-ways-to-distribute-candies/) | [LeetCode CH](https://leetcode.cn/problems/count-ways-to-distribute-candies/) (Hard)

-   Tags: dynamic programming
