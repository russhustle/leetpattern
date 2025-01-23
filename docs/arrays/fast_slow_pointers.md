---
comments: true
---

# Fast Slow Pointers

-   Fast pouinter: explore the array
-   Slow pointer: point to the position to be replaced
-   Time complexity: $O(n)$
-   Space complexity: $O(1)$

## LeetCode Problems

|     | Number | LeetCode                                                                                                        | 力扣                                                                                              | Difficulty |
| --- | ------ | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------- |
| 1   | 0027   | [Remove Element](https://leetcode.com/problems/remove-element/)                                                 | [移除元素](https://leetcode.cn/problems/remove-element/)                                          | Easy       |
| 2   | 0026   | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)       | [删除排序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)       | Easy       |
| 3   | 0080   | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | [删除排序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/) | Medium     |
| 4   | 0283   | [Move Zeroes](https://leetcode.com/problems/move-zeroes/)                                                       | [移动零](https://leetcode.cn/problems/move-zeroes/)                                               | Easy       |
| 5   | 1089   | [Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)                                               | [复写零](https://leetcode.cn/problems/duplicate-zeros/)                                           | Easy       |
| 6   | 0287   | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)                           | [寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)                             | Medium     |

## 27. Remove Element

-   Remove all instances of a given value in-place.

```python
--8<-- "0027_remove_element.py"
```

## 26. Remove Duplicates from Sorted Array

-   Remove duplicates in-place.

```python
--8<-- "0026_remove_duplicates_from_sorted_array.py"
```

## 80. Remove Duplicates from Sorted Array II

-   Allow at most two duplicates.
-   fast pointer: explore the array
-   slow pointer: point to the position to be replaced

```python
--8<-- "0080_remove_duplicates_from_sorted_array_ii.py"
```

## 283. Move Zeroes

-   Move all zeroes to the end of the array while maintaining the relative order of the non-zero elements.

```python
--8<-- "0283_move_zeroes.py"
```

## 1089. Duplicate Zeros

-   Duplicate each occurrence of zero, shifting the remaining elements to the right.

```python
--8<-- "1089_duplicate_zeros.py"
```

## 287. Find the Duplicate Number

-   Find the duplicate number in an array containing `n + 1` integers where each integer is between `1` and `n` inclusive.

```python
--8<-- "0287_find_the_duplicate_number.py"
```
