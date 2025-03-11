---
comments: True
---

# Double Sequence Pairing

- [x] [2037. Minimum Number of Moves to Seat Everyone](https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/) (Easy)
- [x] [455. Assign Cookies](https://leetcode.cn/problems/assign-cookies/) (Easy)
- [ ] [2410. Maximum Matching of Players With Trainers](https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/) (Medium)
- [ ] [1433. Check If a String Can Break Another String](https://leetcode.cn/problems/check-if-a-string-can-break-another-string/) (Medium)
- [ ] [870. Advantage Shuffle](https://leetcode.cn/problems/advantage-shuffle/) (Medium)
- [ ] [826. Most Profit Assigning Work](https://leetcode.cn/problems/most-profit-assigning-work/) (Medium)
- [ ] [2449. Minimum Number of Operations to Make Arrays Similar](https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/) (Hard)
- [ ] [1889. Minimum Space Wasted From Packaging](https://leetcode.cn/problems/minimum-space-wasted-from-packaging/) (Hard)
- [ ] [2561. Rearranging Fruits](https://leetcode.cn/problems/rearranging-fruits/) (Hard)
- [ ] [2323. Find Minimum Time to Finish All Jobs II](https://leetcode.cn/problems/find-minimum-time-to-finish-all-jobs-ii/) (Medium) 👑

## 2037. Minimum Number of Moves to Seat Everyone

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/) (Easy)

-   Tags: array, greedy, sorting, counting sort
-   Return the minimum number of moves needed to seat everyone.

```python title="2037. Minimum Number of Moves to Seat Everyone - Python Solution"
from typing import List


# Greedy
def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()
    moves = 0

    for i, j in zip(seats, students):
        moves += abs(i - j)

    return moves


print(minMovesToSeat([3, 1, 5], [2, 7, 4]))  # 4

```

## 455. Assign Cookies

-   [LeetCode](https://leetcode.com/problems/assign-cookies/) | [LeetCode CH](https://leetcode.cn/problems/assign-cookies/) (Easy)

-   Tags: array, two pointers, greedy, sorting
-   Return the maximum number of your content children that can be satisfied.

```python title="455. Assign Cookies - Python Solution"
from typing import List


# Greedy
def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    i, j = 0, 0

    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            i += 1
        j += 1

    return i


# |-------------|-------------|--------------|
# |   Approach  |    Time     |    Space     |
# |-------------|-------------|--------------|
# |   Greedy    | O(N * logN) |    O(1)      |
# |-------------|-------------|--------------|


g = [1, 2, 3]
s = [1, 1]
print(findContentChildren(g, s))  # 1

```

## 2410. Maximum Matching of Players With Trainers

-   [LeetCode](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/) | [LeetCode CH](https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/) (Medium)

-   Tags: array, two pointers, greedy, sorting

## 1433. Check If a String Can Break Another String

-   [LeetCode](https://leetcode.com/problems/check-if-a-string-can-break-another-string/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-string-can-break-another-string/) (Medium)

-   Tags: string, greedy, sorting

## 870. Advantage Shuffle

-   [LeetCode](https://leetcode.com/problems/advantage-shuffle/) | [LeetCode CH](https://leetcode.cn/problems/advantage-shuffle/) (Medium)

-   Tags: array, two pointers, greedy, sorting

## 826. Most Profit Assigning Work

-   [LeetCode](https://leetcode.com/problems/most-profit-assigning-work/) | [LeetCode CH](https://leetcode.cn/problems/most-profit-assigning-work/) (Medium)

-   Tags: array, two pointers, binary search, greedy, sorting

## 2449. Minimum Number of Operations to Make Arrays Similar

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/) (Hard)

-   Tags: array, greedy, sorting

## 1889. Minimum Space Wasted From Packaging

-   [LeetCode](https://leetcode.com/problems/minimum-space-wasted-from-packaging/) | [LeetCode CH](https://leetcode.cn/problems/minimum-space-wasted-from-packaging/) (Hard)

-   Tags: array, binary search, sorting, prefix sum

## 2561. Rearranging Fruits

-   [LeetCode](https://leetcode.com/problems/rearranging-fruits/) | [LeetCode CH](https://leetcode.cn/problems/rearranging-fruits/) (Hard)

-   Tags: array, hash table, greedy

## 2323. Find Minimum Time to Finish All Jobs II

-   [LeetCode](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-minimum-time-to-finish-all-jobs-ii/) (Medium)

-   Tags: array, greedy, sorting
