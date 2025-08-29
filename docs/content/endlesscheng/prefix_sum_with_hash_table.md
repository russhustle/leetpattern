---
comments: True
---

# Prefix Sum with Hash Table

## Table of Contents

- [ ] [930. Binary Subarrays With Sum](https://leetcode.cn/problems/binary-subarrays-with-sum/) (Medium)
- [x] [560. Subarray Sum Equals K](https://leetcode.cn/problems/subarray-sum-equals-k/) (Medium)
- [ ] [1524. Number of Sub-arrays With Odd Sum](https://leetcode.cn/problems/number-of-sub-arrays-with-odd-sum/) (Medium)
- [x] [974. Subarray Sums Divisible by K](https://leetcode.cn/problems/subarray-sums-divisible-by-k/) (Medium)
- [x] [523. Continuous Subarray Sum](https://leetcode.cn/problems/continuous-subarray-sum/) (Medium)
- [x] [437. Path Sum III](https://leetcode.cn/problems/path-sum-iii/) (Medium)
- [x] [2588. Count the Number of Beautiful Subarrays](https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays/) (Medium)
- [ ] [525. Contiguous Array](https://leetcode.cn/problems/contiguous-array/) (Medium)
- [ ] [3026. Maximum Good Subarray Sum](https://leetcode.cn/problems/maximum-good-subarray-sum/) (Medium)
- [ ] [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.cn/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/) (Medium)
- [ ] [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](https://leetcode.cn/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) (Medium)
- [ ] [1124. Longest Well-Performing Interval](https://leetcode.cn/problems/longest-well-performing-interval/) (Medium)
- [ ] [3381. Maximum Subarray Sum With Length Divisible by K](https://leetcode.cn/problems/maximum-subarray-sum-with-length-divisible-by-k/) (Medium)
- [ ] [2488. Count Subarrays With Median K](https://leetcode.cn/problems/count-subarrays-with-median-k/) (Hard)
- [ ] [1590. Make Sum Divisible by P](https://leetcode.cn/problems/make-sum-divisible-by-p/) (Medium)
- [ ] [2845. Count of Interesting Subarrays](https://leetcode.cn/problems/count-of-interesting-subarrays/) (Medium)
- [ ] [1442. Count Triplets That Can Form Two Arrays of Equal XOR](https://leetcode.cn/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) (Medium)
- [ ] [2949. Count Beautiful Substrings II](https://leetcode.cn/problems/count-beautiful-substrings-ii/) (Hard)
- [x] [325. Maximum Size Subarray Sum Equals k](https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/) (Medium) 👑
- [ ] [548. Split Array with Equal Sum](https://leetcode.cn/problems/split-array-with-equal-sum/) (Hard) 👑
- [ ] [1983. Widest Pair of Indices With Equal Range Sum](https://leetcode.cn/problems/widest-pair-of-indices-with-equal-range-sum/) (Medium) 👑
- [ ] [2489. Number of Substrings With Fixed Ratio](https://leetcode.cn/problems/number-of-substrings-with-fixed-ratio/) (Medium) 👑
- [ ] [2950. Number of Divisible Substrings](https://leetcode.cn/problems/number-of-divisible-substrings/) (Medium) 👑
- [ ] [3364. Minimum Positive Sum Subarray ](https://leetcode.cn/problems/minimum-positive-sum-subarray/) (Easy)
- [ ] [2025. Maximum Number of Ways to Partition an Array](https://leetcode.cn/problems/maximum-number-of-ways-to-partition-an-array/) (Hard)

## 930. Binary Subarrays With Sum

-   [LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/) | [LeetCode CH](https://leetcode.cn/problems/binary-subarrays-with-sum/) (Medium)

-   Tags: array, hash table, sliding window, prefix sum
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

## 1524. Number of Sub-arrays With Odd Sum

-   [LeetCode](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/) | [LeetCode CH](https://leetcode.cn/problems/number-of-sub-arrays-with-odd-sum/) (Medium)

-   Tags: array, math, dynamic programming, prefix sum
## 974. Subarray Sums Divisible by K

-   [LeetCode](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | [LeetCode CH](https://leetcode.cn/problems/subarray-sums-divisible-by-k/) (Medium)

-   Tags: array, hash table, prefix sum
```python title="974. Subarray Sums Divisible by K - Python Solution"
from typing import List


def subarraysDivByK_1(nums: List[int], k: int) -> int:
    mods = {0: 1}
    prefixSum, result = 0, 0

    for num in nums:
        prefixSum += num
        mod = prefixSum % k

        if mod < 0:
            mod += k

        if mod in mods:
            result += mods[mod]

        if mod in mods:
            mods[mod] += 1
        else:
            mods[mod] = 1

    return result


def subarraysDivByK_2(nums: List[int], k: int) -> int:
    mods = {0: 1}
    prefixSum, result = 0, 0

    for num in nums:
        prefixSum += num
        mod = prefixSum % k
        result += mods.get(mod, 0)
        mods[mod] = mods.get(mod, 0) + 1

    return result


nums = [4, 5, 0, -2, -3, 1]
k = 5
print(subarraysDivByK_1(nums, k))  # 7
print(subarraysDivByK_2(nums, k))  # 7

```

## 523. Continuous Subarray Sum

-   [LeetCode](https://leetcode.com/problems/continuous-subarray-sum/) | [LeetCode CH](https://leetcode.cn/problems/continuous-subarray-sum/) (Medium)

-   Tags: array, hash table, math, prefix sum
```python title="523. Continuous Subarray Sum - Python Solution"
from typing import List


# Prefix Sum
def checkSubarraySum(nums: List[int], k: int) -> bool:
    if k == 0:
        for i in range(1, len(nums)):
            if nums[i - 1] == 0 and nums[i] == 0:
                return True

    prefix_sum = 0
    mod_dict = {0: -1}

    for i, num in enumerate(nums):
        prefix_sum += num
        mod = prefix_sum % k

        if mod in mod_dict:
            if i - mod_dict[mod] > 1:
                return True
        else:
            mod_dict[mod] = i

    return False


nums = [23, 2, 4, 6, 7]
k = 6
print(checkSubarraySum(nums, k))  # True

```

## 437. Path Sum III

-   [LeetCode](https://leetcode.com/problems/path-sum-iii/) | [LeetCode CH](https://leetcode.cn/problems/path-sum-iii/) (Medium)

-   Tags: tree, depth first search, binary tree
```cpp title="437. Path Sum III - C++ Solution"
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

class Solution {
   public:
    int pathSum(TreeNode *root, int targetSum) {
        int res = 0;
        unordered_map<long long, int> cnt{{0, 1}};

        auto dfs = [&](auto &&self, TreeNode *node, long long cur) {
            if (!node) return;
            cur += node->val;

            if (cnt.find(cur - targetSum) != cnt.end())
                res += cnt[cur - targetSum];

            cnt[cur]++;
            self(self, node->left, cur);
            self(self, node->right, cur);
            cnt[cur]--;
        };

        dfs(dfs, root, 0);
        return res;
    }
};

int main() {
    Solution s;
    {
        TreeNode *root = new TreeNode(10);
        root->left = new TreeNode(5);
        root->right = new TreeNode(-3);
        root->left->left = new TreeNode(3);
        root->left->right = new TreeNode(2);
        root->right->right = new TreeNode(11);
        root->left->left->left = new TreeNode(3);
        root->left->left->right = new TreeNode(-2);
        root->left->right->right = new TreeNode(1);
        cout << s.pathSum(root, 8) << endl;  // 3
    }
    {
        TreeNode *root = new TreeNode(5);
        root->left = new TreeNode(4);
        root->right = new TreeNode(8);
        root->left->left = new TreeNode(11);
        root->right->left = new TreeNode(13);
        root->right->right = new TreeNode(4);
        root->left->left->left = new TreeNode(7);
        root->left->left->right = new TreeNode(2);
        root->right->right->left = new TreeNode(5);
        root->right->right->right = new TreeNode(1);
        cout << s.pathSum(root, 22) << endl;  // 3
    }
    return 0;
}
```

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

## 525. Contiguous Array

-   [LeetCode](https://leetcode.com/problems/contiguous-array/) | [LeetCode CH](https://leetcode.cn/problems/contiguous-array/) (Medium)

-   Tags: array, hash table, prefix sum
## 3026. Maximum Good Subarray Sum

-   [LeetCode](https://leetcode.com/problems/maximum-good-subarray-sum/) | [LeetCode CH](https://leetcode.cn/problems/maximum-good-subarray-sum/) (Medium)

-   Tags: array, hash table, prefix sum
## 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

-   [LeetCode](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/) | [LeetCode CH](https://leetcode.cn/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/) (Medium)

-   Tags: array, hash table, binary search, dynamic programming, sliding window
## 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) (Medium)

-   Tags: array, hash table, greedy, prefix sum
## 1124. Longest Well-Performing Interval

-   [LeetCode](https://leetcode.com/problems/longest-well-performing-interval/) | [LeetCode CH](https://leetcode.cn/problems/longest-well-performing-interval/) (Medium)

-   Tags: array, hash table, stack, monotonic stack, prefix sum
## 3381. Maximum Subarray Sum With Length Divisible by K

-   [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray-sum-with-length-divisible-by-k/) (Medium)

-   Tags: array, hash table, prefix sum
## 2488. Count Subarrays With Median K

-   [LeetCode](https://leetcode.com/problems/count-subarrays-with-median-k/) | [LeetCode CH](https://leetcode.cn/problems/count-subarrays-with-median-k/) (Hard)

-   Tags: array, hash table, prefix sum
## 1590. Make Sum Divisible by P

-   [LeetCode](https://leetcode.com/problems/make-sum-divisible-by-p/) | [LeetCode CH](https://leetcode.cn/problems/make-sum-divisible-by-p/) (Medium)

-   Tags: array, hash table, prefix sum
## 2845. Count of Interesting Subarrays

-   [LeetCode](https://leetcode.com/problems/count-of-interesting-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/count-of-interesting-subarrays/) (Medium)

-   Tags: array, hash table, prefix sum
## 1442. Count Triplets That Can Form Two Arrays of Equal XOR

-   [LeetCode](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) | [LeetCode CH](https://leetcode.cn/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) (Medium)

-   Tags: array, hash table, math, bit manipulation, prefix sum
## 2949. Count Beautiful Substrings II

-   [LeetCode](https://leetcode.com/problems/count-beautiful-substrings-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-beautiful-substrings-ii/) (Hard)

-   Tags: hash table, math, string, number theory, prefix sum
## 325. Maximum Size Subarray Sum Equals k

-   [LeetCode](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) | [LeetCode CH](https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/) (Medium)

-   Tags: array, hash table, prefix sum
```python title="325. Maximum Size Subarray Sum Equals k - Python Solution"
from typing import List


# Prefix Sum
def maxSubArrayLen(nums: List[int], k: int) -> int:
    res = 0
    prefix = 0
    sumMap = {0: -1}  # sum -> index

    for i, num in enumerate(nums):
        prefix += num
        if prefix - k in sumMap:
            res = max(res, i - sumMap[prefix - k])
        if prefix not in sumMap:
            sumMap[prefix] = i

    return res


nums = [1, -1, 5, -2, 3]
k = 3
print(maxSubArrayLen(nums, k))  # 4

```

## 548. Split Array with Equal Sum

-   [LeetCode](https://leetcode.com/problems/split-array-with-equal-sum/) | [LeetCode CH](https://leetcode.cn/problems/split-array-with-equal-sum/) (Hard)

-   Tags: array, hash table, prefix sum
## 1983. Widest Pair of Indices With Equal Range Sum

-   [LeetCode](https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/) | [LeetCode CH](https://leetcode.cn/problems/widest-pair-of-indices-with-equal-range-sum/) (Medium)

-   Tags: array, hash table, prefix sum
## 2489. Number of Substrings With Fixed Ratio

-   [LeetCode](https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/) | [LeetCode CH](https://leetcode.cn/problems/number-of-substrings-with-fixed-ratio/) (Medium)

-   Tags: hash table, math, string, prefix sum
## 2950. Number of Divisible Substrings

-   [LeetCode](https://leetcode.com/problems/number-of-divisible-substrings/) | [LeetCode CH](https://leetcode.cn/problems/number-of-divisible-substrings/) (Medium)

-   Tags: hash table, string, counting, prefix sum
## 3364. Minimum Positive Sum Subarray 

-   [LeetCode](https://leetcode.com/problems/minimum-positive-sum-subarray/) | [LeetCode CH](https://leetcode.cn/problems/minimum-positive-sum-subarray/) (Easy)

-   Tags: array, sliding window, prefix sum
## 2025. Maximum Number of Ways to Partition an Array

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-ways-to-partition-an-array/) (Hard)

-   Tags: array, hash table, counting, enumeration, prefix sum
