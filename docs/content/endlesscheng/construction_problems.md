---
comments: True
---

# Construction Problems

- [ ] [942. DI String Match](https://leetcode.cn/problems/di-string-match/) (Easy)
- [ ] [1968. Array With Elements Not Equal to Average of Neighbors](https://leetcode.cn/problems/array-with-elements-not-equal-to-average-of-neighbors/) (Medium)
- [ ] [1253. Reconstruct a 2-Row Binary Matrix](https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/) (Medium)
- [ ] [2182. Construct String With Repeat Limit](https://leetcode.cn/problems/construct-string-with-repeat-limit/) (Medium)
- [ ] [969. Pancake Sorting](https://leetcode.cn/problems/pancake-sorting/) (Medium)
- [ ] [1605. Find Valid Matrix Given Row and Column Sums](https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/) (Medium)
- [ ] [2375. Construct Smallest Number From DI String](https://leetcode.cn/problems/construct-smallest-number-from-di-string/) (Medium)
- [ ] [324. Wiggle Sort II](https://leetcode.cn/problems/wiggle-sort-ii/) (Medium)
- [ ] [667. Beautiful Arrangement II](https://leetcode.cn/problems/beautiful-arrangement-ii/) (Medium)
- [ ] [2122. Recover the Original Array](https://leetcode.cn/problems/recover-the-original-array/) (Hard)
- [ ] [932. Beautiful Array](https://leetcode.cn/problems/beautiful-array/) (Medium)
- [ ] [3311. Construct 2D Grid Matching Graph Layout](https://leetcode.cn/problems/construct-2d-grid-matching-graph-layout/) (Hard)
- [ ] [2573. Find the String with LCP](https://leetcode.cn/problems/find-the-string-with-lcp/) (Hard)
- [ ] [1982. Find Array Given Subset Sums](https://leetcode.cn/problems/find-array-given-subset-sums/) (Hard)
- [x] [280. Wiggle Sort](https://leetcode.cn/problems/wiggle-sort/) (Medium) 👑
- [ ] [484. Find Permutation](https://leetcode.cn/problems/find-permutation/) (Medium) 👑
- [ ] [1980. Find Unique Binary String](https://leetcode.cn/problems/find-unique-binary-string/) (Medium)

## 942. DI String Match

-   [LeetCode](https://leetcode.com/problems/di-string-match/) | [LeetCode CH](https://leetcode.cn/problems/di-string-match/) (Easy)

-   Tags: array, two pointers, string, greedy

## 1968. Array With Elements Not Equal to Average of Neighbors

-   [LeetCode](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/) | [LeetCode CH](https://leetcode.cn/problems/array-with-elements-not-equal-to-average-of-neighbors/) (Medium)

-   Tags: array, greedy, sorting

## 1253. Reconstruct a 2-Row Binary Matrix

-   [LeetCode](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/) | [LeetCode CH](https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/) (Medium)

-   Tags: array, greedy, matrix

## 2182. Construct String With Repeat Limit

-   [LeetCode](https://leetcode.com/problems/construct-string-with-repeat-limit/) | [LeetCode CH](https://leetcode.cn/problems/construct-string-with-repeat-limit/) (Medium)

-   Tags: hash table, string, greedy, heap priority queue, counting

## 969. Pancake Sorting

-   [LeetCode](https://leetcode.com/problems/pancake-sorting/) | [LeetCode CH](https://leetcode.cn/problems/pancake-sorting/) (Medium)

-   Tags: array, two pointers, greedy, sorting

## 1605. Find Valid Matrix Given Row and Column Sums

-   [LeetCode](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/) | [LeetCode CH](https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/) (Medium)

-   Tags: array, greedy, matrix

## 2375. Construct Smallest Number From DI String

-   [LeetCode](https://leetcode.com/problems/construct-smallest-number-from-di-string/) | [LeetCode CH](https://leetcode.cn/problems/construct-smallest-number-from-di-string/) (Medium)

-   Tags: string, backtracking, stack, greedy

## 324. Wiggle Sort II

-   [LeetCode](https://leetcode.com/problems/wiggle-sort-ii/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-sort-ii/) (Medium)

-   Tags: array, divide and conquer, greedy, sorting, quickselect

## 667. Beautiful Arrangement II

-   [LeetCode](https://leetcode.com/problems/beautiful-arrangement-ii/) | [LeetCode CH](https://leetcode.cn/problems/beautiful-arrangement-ii/) (Medium)

-   Tags: array, math

## 2122. Recover the Original Array

-   [LeetCode](https://leetcode.com/problems/recover-the-original-array/) | [LeetCode CH](https://leetcode.cn/problems/recover-the-original-array/) (Hard)

-   Tags: array, hash table, two pointers, sorting, enumeration

## 932. Beautiful Array

-   [LeetCode](https://leetcode.com/problems/beautiful-array/) | [LeetCode CH](https://leetcode.cn/problems/beautiful-array/) (Medium)

-   Tags: array, math, divide and conquer

## 3311. Construct 2D Grid Matching Graph Layout

-   [LeetCode](https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/) | [LeetCode CH](https://leetcode.cn/problems/construct-2d-grid-matching-graph-layout/) (Hard)

-   Tags: array, hash table, graph, matrix

## 2573. Find the String with LCP

-   [LeetCode](https://leetcode.com/problems/find-the-string-with-lcp/) | [LeetCode CH](https://leetcode.cn/problems/find-the-string-with-lcp/) (Hard)

-   Tags: array, string, dynamic programming, greedy, union find, matrix

## 1982. Find Array Given Subset Sums

-   [LeetCode](https://leetcode.com/problems/find-array-given-subset-sums/) | [LeetCode CH](https://leetcode.cn/problems/find-array-given-subset-sums/) (Hard)

-   Tags: array, divide and conquer

## 280. Wiggle Sort

-   [LeetCode](https://leetcode.com/problems/wiggle-sort/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-sort/) (Medium)

-   Tags: array, greedy, sorting

```cpp title="280. Wiggle Sort - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

void wiggleSort(vector<int>& nums) {
    int n = nums.size();

    for (int i = 0; i < n - 1; i++) {
        if (i % 2 == 0) {
            if (nums[i] > nums[i + 1]) swap(nums[i], nums[i + 1]);
        } else {
            if (nums[i] < nums[i + 1]) swap(nums[i], nums[i + 1]);
        }
    }
}

int main() {
    vector<int> nums = {3, 5, 2, 1, 6, 4};
    wiggleSort(nums);
    // 3 5 1 6 2 4
    for (size_t i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}

```

## 484. Find Permutation

-   [LeetCode](https://leetcode.com/problems/find-permutation/) | [LeetCode CH](https://leetcode.cn/problems/find-permutation/) (Medium)

-   Tags: array, string, stack, greedy

## 1980. Find Unique Binary String

-   [LeetCode](https://leetcode.com/problems/find-unique-binary-string/) | [LeetCode CH](https://leetcode.cn/problems/find-unique-binary-string/) (Medium)

-   Tags: array, hash table, string, backtracking
