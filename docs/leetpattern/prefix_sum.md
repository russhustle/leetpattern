---
comments: True
---

# Prefix Sum

- [x] [2574. Left and Right Sum Differences](https://leetcode.cn/problems/left-and-right-sum-differences/) (Easy)
- [x] [1732. Find the Highest Altitude](https://leetcode.cn/problems/find-the-highest-altitude/) (Easy)
- [x] [303. Range Sum Query - Immutable](https://leetcode.cn/problems/range-sum-query-immutable/) (Easy)
- [x] [304. Range Sum Query 2D - Immutable](https://leetcode.cn/problems/range-sum-query-2d-immutable/) (Medium)
- [x] [560. Subarray Sum Equals K](https://leetcode.cn/problems/subarray-sum-equals-k/) (Medium)
- [x] [238. Product of Array Except Self](https://leetcode.cn/problems/product-of-array-except-self/) (Medium)
- [x] [974. Subarray Sums Divisible by K](https://leetcode.cn/problems/subarray-sums-divisible-by-k/) (Medium)
- [x] [209. Minimum Size Subarray Sum](https://leetcode.cn/problems/minimum-size-subarray-sum/) (Medium)
- [x] [523. Continuous Subarray Sum](https://leetcode.cn/problems/continuous-subarray-sum/) (Medium)
- [x] [1248. Count Number of Nice Subarrays](https://leetcode.cn/problems/count-number-of-nice-subarrays/) (Medium)
- [x] [325. Maximum Size Subarray Sum Equals k](https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/) (Medium) 👑
- [x] [862. Shortest Subarray with Sum at Least K](https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/) (Hard)
- [x] [1171. Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) (Medium)

## 2574. Left and Right Sum Differences

-   [LeetCode](https://leetcode.com/problems/left-and-right-sum-differences/) | [LeetCode CH](https://leetcode.cn/problems/left-and-right-sum-differences/) (Easy)

-   Tags: array, prefix sum

```python title="2574. Left and Right Sum Differences - Python Solution"
from typing import List


# Prefix Sum
def leftRightDifferenceSum(nums: List[int]) -> List[int]:
    n = len(nums)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]

    for i in range(1, n):
        left[i] = left[i - 1] + nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] + nums[i + 1]

    return [abs(left[i] - right[i]) for i in range(n)]


# Left Right Pointers
def leftRightDifferencePointer(nums: List[int]) -> List[int]:
    left, right = 0, sum(nums)
    result = []

    for num in nums:
        right -= num
        result.append(abs(left - right))
        left += num

    return result


nums = [10, 4, 8, 3]
print(leftRightDifferenceSum(nums))  # [15, 1, 11, 22]
print(leftRightDifferencePointer(nums))  # [15, 1, 11, 22]

```

## 1732. Find the Highest Altitude

-   [LeetCode](https://leetcode.com/problems/find-the-highest-altitude/) | [LeetCode CH](https://leetcode.cn/problems/find-the-highest-altitude/) (Easy)

-   Tags: array, prefix sum

```python title="1732. Find the Highest Altitude - Python Solution"
from typing import List


def largestAltitude(gain: List[int]) -> int:
    result, altitude = 0, 0

    for i in gain:
        altitude += i
        result = max(result, altitude)

    return result


gain = [-5, 1, 5, 0, -7]
print(largestAltitude(gain))  # 1

```

## 303. Range Sum Query - Immutable

-   [LeetCode](https://leetcode.com/problems/range-sum-query-immutable/) | [LeetCode CH](https://leetcode.cn/problems/range-sum-query-immutable/) (Easy)

-   Tags: array, design, prefix sum

```python title="303. Range Sum Query - Immutable - Python Solution"
from typing import List


# Prefix Sum
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.ps = [0 for _ in range(n + 1)]  # prefix sum
        for i in range(1, n + 1):
            self.ps[i] = self.ps[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right + 1] - self.ps[left]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
assert obj.sumRange(0, 2) == 1
assert obj.sumRange(2, 5) == -1
assert obj.sumRange(0, 5) == -3
print("PASSED")

```

## 304. Range Sum Query 2D - Immutable

-   [LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/) | [LeetCode CH](https://leetcode.cn/problems/range-sum-query-2d-immutable/) (Medium)

-   Tags: array, design, matrix, prefix sum

```python title="304. Range Sum Query 2D - Immutable - Python Solution"
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return None

        self.sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.sum[i - 1][j]
                    + self.sum[i][j - 1]
                    - self.sum[i - 1][j - 1]  # to avoid double counting
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sum[row2 + 1][col2 + 1]
            - self.sum[row1][col2 + 1]
            - self.sum[row2 + 1][col1]
            + self.sum[row1][col1]
        )


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]
obj = NumMatrix(matrix)
assert obj.sumRegion(2, 1, 4, 3) == 8
assert obj.sumRegion(1, 1, 2, 2) == 11
assert obj.sumRegion(1, 2, 2, 4) == 12
print("PASSED")

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

## 209. Minimum Size Subarray Sum

-   [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-size-subarray-sum/) (Medium)

-   Tags: array, binary search, sliding window, prefix sum

```python title="209. Minimum Size Subarray Sum - Python Solution"
import bisect
from typing import List


# Prefix Sum
def minSubArrayLenPS(target: int, nums: List[int]) -> int:
    n = len(nums)
    prefix_sums = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

    minLen = float("inf")

    for i in range(n + 1):
        new_target = target + prefix_sums[i]
        bound = bisect.bisect_left(prefix_sums, new_target)
        if bound != len(prefix_sums):
            minLen = min(minLen, bound - i)

    return 0 if minLen == float("inf") else minLen


# Sliding Window Variable Size
def minSubArrayLenSW(target: int, nums: List[int]) -> int:
    res, cur = float("inf"), 0
    left = 0

    for right in range(len(nums)):
        cur += nums[right]

        while cur >= target:
            res = min(res, right - left + 1)
            cur -= nums[left]
            left += 1

    return res if res != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLenPS(target, nums))  # 2
print(minSubArrayLenSW(target, nums))  # 2

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

## 862. Shortest Subarray with Sum at Least K

-   [LeetCode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | [LeetCode CH](https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/) (Hard)

-   Tags: array, binary search, queue, sliding window, heap priority queue, prefix sum, monotonic queue

```python title="862. Shortest Subarray with Sum at Least K - Python Solution"
from collections import deque
from typing import List


# Prefix Sum + Monotonic Queue
def shortestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    ps = [0 for _ in range(n + 1)]

    for i in range(n):
        ps[i + 1] = ps[i] + nums[i]

    res = float("inf")
    q = deque()

    for i in range(n + 1):
        while q and ps[i] - ps[q[0]] >= k:
            res = min(res, i - q.popleft())
        while q and ps[i] <= ps[q[-1]]:
            q.pop()
        q.append(i)

    return res if res != float("inf") else -1


nums = [2, -1, 2]
k = 3
print(shortestSubarray(nums, k))  # 3

```

## 1171. Remove Zero Sum Consecutive Nodes from Linked List

-   [LeetCode](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) (Medium)

-   Tags: hash table, linked list

```python title="1171. Remove Zero Sum Consecutive Nodes from Linked List - Python Solution"
from typing import Optional

from template import ListNode


# Prefix Sum
def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    prefix_sum = 0
    seen = {0: dummy}

    while cur:
        prefix_sum += cur.val
        if prefix_sum in seen:
            node = seen[prefix_sum].next
            temp_sum = prefix_sum
            while node != cur:
                temp_sum += node.val
                del seen[temp_sum]
                node = node.next
            seen[prefix_sum].next = cur.next
        else:
            seen[prefix_sum] = cur
        cur = cur.next

    return dummy.next


head = ListNode().create([1, 2, -3, 3, 1])
print(removeZeroSumSublists(head))  # 3 -> 1

```
