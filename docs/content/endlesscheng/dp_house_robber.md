---
comments: True
---

# DP House Robber

- [x] [198. House Robber](https://leetcode.cn/problems/house-robber/) (Medium)
- [x] [740. Delete and Earn](https://leetcode.cn/problems/delete-and-earn/) (Medium)
- [ ] [2320. Count Number of Ways to Place Houses](https://leetcode.cn/problems/count-number-of-ways-to-place-houses/) (Medium)
- [x] [213. House Robber II](https://leetcode.cn/problems/house-robber-ii/) (Medium)
- [ ] [3186. Maximum Total Damage With Spell Casting](https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/) (Medium)

## 198. House Robber

-   [LeetCode](https://leetcode.com/problems/house-robber/) | [LeetCode CH](https://leetcode.cn/problems/house-robber/) (Medium)

-   Tags: array, dynamic programming
-   Return the maximum amount of money that can be robbed from the houses. No two adjacent houses can be robbed.

-   `dp[n]` stores the maximum amount of money that can be robbed from the first `n` houses.
-   Formula: `dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])`.
    -   Skip: `dp[n]` → `dp[n - 1]`
    -   Rob: `dp[n]` → `dp[n - 2] + nums[n]`
-   Initialize `dp[0] = nums[0]` and `dp[1] = max(nums[0], nums[1])`.
-   Return `dp[-1]`.
-   Example: `nums = [2, 7, 9, 3, 1]`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |
|  4  |     1     |    11     |    11     |         12          |   12    |

```python title="198. House Robber - Python Solution"
from typing import List


# DP (House Robber)
def rob1(nums: List[int]) -> int:
    if len(nums) < 3:
        return max(nums)

    dp = [0 for _ in range(len(nums))]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


# DP (House Robber) Optimized
def rob2(nums: List[int]) -> int:
    f0, f1 = 0, 0

    for num in nums:
        f0, f1 = f1, max(f1, f0 + num)

    return f1


nums = [2, 7, 9, 3, 1]
print(rob1(nums))  # 12
print(rob2(nums))  # 12

```

```cpp title="198. House Robber - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

int rob(vector<int> &nums) {
    int prev = 0, cur = 0, temp = 0;

    for (int num : nums) {
        temp = cur;
        cur = max(cur, prev + num);
        prev = temp;
    }
    return cur;
}

int main() {
    vector<int> nums = {2, 7, 9, 3, 1};
    cout << rob(nums) << endl;  // 12
    return 0;
}

```

## 740. Delete and Earn

-   [LeetCode](https://leetcode.com/problems/delete-and-earn/) | [LeetCode CH](https://leetcode.cn/problems/delete-and-earn/) (Medium)

-   Tags: array, hash table, dynamic programming

```python title="740. Delete and Earn - Python Solution"
from typing import List


# DP (House Robber)
def deleteAndEarn(nums: List[int]) -> int:
    def rob(nums):
        f0, f1 = 0, 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)
        return f1

    res = [0 for _ in range(max(nums) + 1)]

    for x in nums:
        res[x] += x

    return rob(res)


nums = [2, 2, 3, 3, 3, 4]
print(deleteAndEarn(nums))  # 9

```

## 2320. Count Number of Ways to Place Houses

-   [LeetCode](https://leetcode.com/problems/count-number-of-ways-to-place-houses/) | [LeetCode CH](https://leetcode.cn/problems/count-number-of-ways-to-place-houses/) (Medium)

-   Tags: dynamic programming

## 213. House Robber II

-   [LeetCode](https://leetcode.com/problems/house-robber-ii/) | [LeetCode CH](https://leetcode.cn/problems/house-robber-ii/) (Medium)

-   Tags: array, dynamic programming
-   Return the maximum amount of money that can be robbed from the houses arranged in a circle.
-   Circular → Linear: `nums[0]` and `nums[-1]` cannot be robbed together.
-   Rob from `0` to `n - 2`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |

-   Rob from `1` to `n - 1`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  1  |     7     |     -     |     -     |          -          |    7    |
|  2  |     9     |     -     |     7     |          -          |    9    |
|  3  |     3     |     7     |     9     |         10          |   10    |
|  4  |     1     |     9     |    10     |         10          |   10    |

```python title="213. House Robber II - Python Solution"
from typing import List


# DP
def rob(nums: List[int]) -> int:
    if len(nums) <= 3:
        return max(nums)

    def robLinear(nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    # circle -> linear
    a = robLinear(nums[1:])  # 2nd house to the last house
    b = robLinear(nums[:-1])  # 1st house to the 2nd last house

    return max(a, b)


nums = [2, 7, 9, 3, 1]
print(rob(nums))  # 11

```

```cpp title="213. House Robber II - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// DP
int robDP(vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) return *max_element(nums.begin(), nums.end());

    vector<int> dp1(n, 0), dp2(n, 0);

    dp1[0] = nums[0];
    dp2[1] = max(nums[0], nums[1]);
    for (int i = 2; i < n - 1; i++) {
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }

    dp2[1] = nums[1];
    dp2[2] = max(nums[1], nums[2]);
    for (int i = 3; i < n; i++) {
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }

    return max(dp1[n - 2], dp2[n - 1]);
}

// DP (Space Optimized)
int robDPOptimized(vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) return *max_element(nums.begin(), nums.end());

    int f1 = nums[0];
    int f2 = max(nums[0], nums[1]);
    int res1;
    for (int i = 2; i < n - 1; i++) {
        res1 = max(f2, f1 + nums[i]);
        f1 = f2;
        f2 = res1;
    }

    f1 = nums[1];
    f2 = max(nums[1], nums[2]);
    int res2;
    for (int i = 3; i < n; i++) {
        res2 = max(f2, f1 + nums[i]);
        f1 = f2;
        f2 = res2;
    }

    return max(res1, res2);
}

int main() {
    vector<int> nums = {2, 3, 2};
    cout << robDP(nums) << endl;           // 3
    cout << robDPOptimized(nums) << endl;  // 3

    nums = {1, 2, 3, 1};
    cout << robDP(nums) << endl;           // 4
    cout << robDPOptimized(nums) << endl;  // 4

    return 0;
}

```

## 3186. Maximum Total Damage With Spell Casting

-   [LeetCode](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/) | [LeetCode CH](https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/) (Medium)

-   Tags: array, hash table, two pointers, binary search, dynamic programming, sorting, counting
