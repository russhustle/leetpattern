---
comments: True
---

# Arrays Strings

## Table of Contents

- [x] [624. Maximum Distance in Arrays](https://leetcode.cn/problems/maximum-distance-in-arrays/) (Medium)
- [x] [280. Wiggle Sort](https://leetcode.cn/problems/wiggle-sort/) (Medium) 👑
- [x] [1056. Confusing Number](https://leetcode.cn/problems/confusing-number/) (Easy) 👑
- [x] [1427. Perform String Shifts](https://leetcode.cn/problems/perform-string-shifts/) (Easy) 👑
- [ ] [161. One Edit Distance](https://leetcode.cn/problems/one-edit-distance/) (Medium) 👑
- [ ] [186. Reverse Words in a String II](https://leetcode.cn/problems/reverse-words-in-a-string-ii/) (Medium) 👑
- [ ] [1055. Shortest Way to Form String](https://leetcode.cn/problems/shortest-way-to-form-string/) (Medium) 👑

## 624. Maximum Distance in Arrays

-   [LeetCode](https://leetcode.com/problems/maximum-distance-in-arrays/) | [LeetCode CH](https://leetcode.cn/problems/maximum-distance-in-arrays/) (Medium)

-   Tags: array, greedy

```python title="624. Maximum Distance in Arrays - Python Solution"
from typing import List


# Array
def maxDistance(arrays: List[List[int]]) -> int:
    mn, mx = float("inf"), float("-inf")
    res = 0

    for arr in arrays:
        res = max(res, arr[-1] - mn, mx - arr[0])
        mn = min(mn, arr[0])
        mx = max(mx, arr[-1])

    return res


arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
print(maxDistance(arrays))  # 4

```

## 280. Wiggle Sort

-   [LeetCode](https://leetcode.com/problems/wiggle-sort/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-sort/) (Medium)

-   Tags: array, greedy, sorting

```python title="280. Wiggle Sort - Python Solution"
from typing import List


def wiggleSort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(n - 1):
        if i % 2 == 0:
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


num = [3, 5, 2, 1, 6, 4]
wiggleSort(num)
print(num)  # [3, 5, 1, 6, 2, 4]

```

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

## 1056. Confusing Number

-   [LeetCode](https://leetcode.com/problems/confusing-number/) | [LeetCode CH](https://leetcode.cn/problems/confusing-number/) (Easy)

-   Tags: math

```python title="1056. Confusing Number - Python Solution"
def confusingNumber(n: int) -> bool:
    rotate_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    original = str(n)
    rotated = ""

    for ch in reversed(original):
        if ch not in rotate_map:
            return False
        rotated += rotate_map[ch]

    return rotated != original


if __name__ == "__main__":
    print(confusingNumber(6))  # True
    print(confusingNumber(89))  # True
    print(confusingNumber(11))  # False

```

```cpp title="1056. Confusing Number - C++ Solution"
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
   public:
    bool confusingNumber(int n) {
        static const unordered_map<char, char> rotationMap = {
            {'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};

        string numStr = to_string(n);
        string rotated;
        rotated.reserve(numStr.size());

        for (int i = numStr.size() - 1; i >= 0; --i) {
            char currentDigit = numStr[i];

            auto it = rotationMap.find(currentDigit);
            if (it == rotationMap.end()) {
                return false;
            }

            rotated.push_back(it->second);
        }

        return rotated != numStr;
    }
};

int main() {
    Solution sol;
    cout << boolalpha;  // Print boolean values as true/false
    cout << sol.confusingNumber(6) << endl;    // true
    cout << sol.confusingNumber(89) << endl;   // true
    cout << sol.confusingNumber(11) << endl;   // false
    cout << sol.confusingNumber(25) << endl;   // false
    cout << sol.confusingNumber(916) << endl;  // true
    cout << sol.confusingNumber(101) << endl;  // false

    return 0;
}

```

## 1427. Perform String Shifts

-   [LeetCode](https://leetcode.com/problems/perform-string-shifts/) | [LeetCode CH](https://leetcode.cn/problems/perform-string-shifts/) (Easy)

-   Tags: array, math, string
-   Calculate the net shift direction and amount by combining all operations, then apply a single rotation to the string using slicing.

```python title="1427. Perform String Shifts - Python Solution"
from typing import List


def stringShift(s: str, shift: List[List[int]]) -> str:
    total_shift = 0
    for direction, amount in shift:
        if direction == 0:
            total_shift -= amount
        else:
            total_shift += amount

    total_shift %= len(s)

    if total_shift == 0:
        return s

    if total_shift > 0:
        return s[-total_shift:] + s[:-total_shift]
    else:
        total_shift = abs(total_shift)
        return s[total_shift:] + s[:total_shift]

```

```cpp title="1427. Perform String Shifts - C++ Solution"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int total_shift = 0;
        for (const auto& op : shift) {
            if (op[0] == 0) {
                total_shift -= op[1];
            } else {
                total_shift += op[1];
            }
        }

        int n = s.length();
        total_shift =
            ((total_shift % n) + n) % n;  // Handle negative shift properly

        if (total_shift == 0) {
            return s;
        }

        return s.substr(n - total_shift) + s.substr(0, n - total_shift);
    }
};

int main() {
    Solution solution;

    string s1 = "abc";
    vector<vector<int>> shift1 = {{0, 1}, {1, 2}};
    cout << "Input: s = \"abc\", shift = [[0,1],[1,2]]" << endl;
    cout << "Output: " << solution.stringShift(s1, shift1) << endl;

    string s2 = "abcdefg";
    vector<vector<int>> shift2 = {{1, 1}, {1, 1}, {0, 2}, {1, 3}};
    cout << "Input: s = \"abcdefg\", shift = [[1,1],[1,1],[0,2],[1,3]]" << endl;
    cout << "Output: " << solution.stringShift(s2, shift2) << endl;

    return 0;
}

```

## 161. One Edit Distance

-   [LeetCode](https://leetcode.com/problems/one-edit-distance/) | [LeetCode CH](https://leetcode.cn/problems/one-edit-distance/) (Medium)

-   Tags: two pointers, string

## 186. Reverse Words in a String II

-   [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-ii/) | [LeetCode CH](https://leetcode.cn/problems/reverse-words-in-a-string-ii/) (Medium)

-   Tags: two pointers, string

## 1055. Shortest Way to Form String

-   [LeetCode](https://leetcode.com/problems/shortest-way-to-form-string/) | [LeetCode CH](https://leetcode.cn/problems/shortest-way-to-form-string/) (Medium)

-   Tags: two pointers, string, binary search, greedy
