---
comments: True
---

# Boyer Moore

- [x] [169. Majority Element](https://leetcode.cn/problems/majority-element/) (Easy)
- [x] [229. Majority Element II](https://leetcode.cn/problems/majority-element-ii/) (Medium)
- [x] [287. Find the Duplicate Number](https://leetcode.cn/problems/find-the-duplicate-number/) (Medium)
- [ ] [1150. Check If a Number Is Majority Element in a Sorted Array](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy) 👑
- [ ] [1157. Online Majority Element In Subarray](https://leetcode.cn/problems/online-majority-element-in-subarray/) (Hard)
- [ ] [495. Teemo Attacking](https://leetcode.cn/problems/teemo-attacking/) (Easy)

## 169. Majority Element

-   [LeetCode](https://leetcode.com/problems/majority-element/) | [LeetCode CH](https://leetcode.cn/problems/majority-element/) (Easy)

-   Tags: array, hash table, divide and conquer, sorting, counting
-   Return the majority element in an array. The majority element is the element that appears more than `n // 2` times.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7pnhv842keE?si=fBYlNfKzdkiLgkF1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| `num` | `count` | `res` |
| ----- | ------- | ----- |
| 2     | 1       | 2     |
| 2     | 2       | 2     |
| 1     | 1       | 2     |
| 1     | 0       | 2     |
| 1     | 1       | 1     |
| 2     | 0       | 1     |
| 2     | 1       | 2     |

```python title="169. Majority Element - Python Solution"
--8<-- "0169_majority_element.py"
```

## 229. Majority Element II

-   [LeetCode](https://leetcode.com/problems/majority-element-ii/) | [LeetCode CH](https://leetcode.cn/problems/majority-element-ii/) (Medium)

-   Tags: array, hash table, sorting, counting

```python title="229. Majority Element II - Python Solution"
--8<-- "0229_majority_element_ii.py"
```

## 287. Find the Duplicate Number

-   [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) | [LeetCode CH](https://leetcode.cn/problems/find-the-duplicate-number/) (Medium)

-   Tags: array, two pointers, binary search, bit manipulation
-   Find the duplicate number in an array containing `n + 1` integers where each integer is between `1` and `n` inclusive.

```python title="287. Find the Duplicate Number - Python Solution"
--8<-- "0287_find_the_duplicate_number.py"
```

## 1150. Check If a Number Is Majority Element in a Sorted Array

-   [LeetCode](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy)

-   Tags: array, binary search

## 1157. Online Majority Element In Subarray

-   [LeetCode](https://leetcode.com/problems/online-majority-element-in-subarray/) | [LeetCode CH](https://leetcode.cn/problems/online-majority-element-in-subarray/) (Hard)

-   Tags: array, binary search, design, binary indexed tree, segment tree

## 495. Teemo Attacking

-   [LeetCode](https://leetcode.com/problems/teemo-attacking/) | [LeetCode CH](https://leetcode.cn/problems/teemo-attacking/) (Easy)

-   Tags: array, simulation
