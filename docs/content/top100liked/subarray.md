---
comments: True
---

# Subarray

## Table of Contents

- [x] [560. Subarray Sum Equals K](https://leetcode.cn/problems/subarray-sum-equals-k/) (Medium)
- [x] [239. Sliding Window Maximum](https://leetcode.cn/problems/sliding-window-maximum/) (Hard)
- [x] [76. Minimum Window Substring](https://leetcode.cn/problems/minimum-window-substring/) (Hard)

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

## 239. Sliding Window Maximum

-   [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) | [LeetCode CH](https://leetcode.cn/problems/sliding-window-maximum/) (Hard)

-   Tags: array, queue, sliding window, heap priority queue, monotonic queue

```python title="239. Sliding Window Maximum - Python Solution"
from collections import deque
from typing import List


# Monotonic Queue
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []

    for i, num in enumerate(nums):
        if q and q[0] < i - k + 1:
            q.popleft()

        while q and nums[q[-1]] < num:
            q.pop()

        q.append(i)

        if i >= k - 1:
            res.append(nums[q[0]])

    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # [3, 3, 5, 5, 6, 7]

```

## 76. Minimum Window Substring

-   [LeetCode](https://leetcode.com/problems/minimum-window-substring/) | [LeetCode CH](https://leetcode.cn/problems/minimum-window-substring/) (Hard)

-   Tags: hash table, string, sliding window

```python title="76. Minimum Window Substring - Python Solution"
from collections import Counter


def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    counts = Counter(t)
    required = len(counts)

    left, right = 0, 0
    formed = 0
    window_counts = dict()

    result = float("inf"), None, None

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in counts and window_counts[char] == counts[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            window_counts[char] -= 1
            if char in counts and window_counts[char] < counts[char]:
                formed -= 1
            left += 1

        right += 1

    return "" if result[0] == float("inf") else s[result[1] : result[2] + 1]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # BANC

```
