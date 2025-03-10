---
comments: True
---

# Techniques

- [x] [136. Single Number](https://leetcode.cn/problems/single-number/) (Easy)
- [x] [169. Majority Element](https://leetcode.cn/problems/majority-element/) (Easy)
- [x] [75. Sort Colors](https://leetcode.cn/problems/sort-colors/) (Medium)
- [x] [31. Next Permutation](https://leetcode.cn/problems/next-permutation/) (Medium)
- [x] [287. Find the Duplicate Number](https://leetcode.cn/problems/find-the-duplicate-number/) (Medium)

## 136. Single Number

-   [LeetCode](https://leetcode.com/problems/single-number/) | [LeetCode CH](https://leetcode.cn/problems/single-number/) (Easy)

-   Tags: array, bit manipulation

```python title="136. Single Number - Python Solution"
--8<-- "0136_single_number.py"
```

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

## 75. Sort Colors

-   [LeetCode](https://leetcode.com/problems/sort-colors/) | [LeetCode CH](https://leetcode.cn/problems/sort-colors/) (Medium)

-   Tags: array, two pointers, sorting

```python title="75. Sort Colors - Python Solution"
--8<-- "0075_sort_colors.py"
```

## 31. Next Permutation

-   [LeetCode](https://leetcode.com/problems/next-permutation/) | [LeetCode CH](https://leetcode.cn/problems/next-permutation/) (Medium)

-   Tags: array, two pointers

```python title="31. Next Permutation - Python Solution"
--8<-- "0031_next_permutation.py"
```

## 287. Find the Duplicate Number

-   [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) | [LeetCode CH](https://leetcode.cn/problems/find-the-duplicate-number/) (Medium)

-   Tags: array, two pointers, binary search, bit manipulation
-   Find the duplicate number in an array containing `n + 1` integers where each integer is between `1` and `n` inclusive.

```python title="287. Find the Duplicate Number - Python Solution"
--8<-- "0287_find_the_duplicate_number.py"
```
