---
comments: true
---

# Hash Map

## LeetCode Problems

1. 0383 - [Ransom Note](https://leetcode.com/problems/ransom-note/) | [赎金信](https://leetcode.cn/problems/ransom-note/) (Easy)
2. 0350 - [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | [两个数组的交集 II](https://leetcode.cn/problems/intersection-of-two-arrays-ii/) (Easy)
3. 0001 - [Two Sum](https://leetcode.com/problems/two-sum/) | [两数之和](https://leetcode.cn/problems/two-sum/) (Easy)
4. 0409 - [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | [最长回文串](https://leetcode.cn/problems/longest-palindrome/) (Easy)
5. 1365 - [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | [有多少小于当前数字的数字](https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/) (Easy)
6. 0202 - [Happy Number](https://leetcode.com/problems/happy-number/) | [快乐数](https://leetcode.cn/problems/happy-number/) (Easy)
7. 0454 - [4Sum II](https://leetcode.com/problems/4sum-ii/) | [四数相加 II](https://leetcode.cn/problems/4sum-ii/) (Medium)

## 383. Ransom Note

-   Return `True` if the ransom note can be constructed from the magazines, otherwise, return `False`.

```mermaid
graph LR
    A["Magazine: abcdef"] --> C(True)
    B["Ransom Note: abc"] --> C
```

```python
--8<-- "0383_ransom_note.py"
```

## 350. Intersection of Two Arrays II

-   Return the intersection of two arrays.

```python
--8<-- "0350_intersection_of_two_arrays_ii.py"
```

## 1. Two Sum

-   Return the indices of the two numbers such that they add up to a specific target.

```python
--8<-- "0001_two_sum.py"
```

## 409. Longest Palindrome

-   Return the length of the longest palindrome that can be built with the characters in the string.

```python
--8<-- "0409_longest_palindrome.py"
```

## 1365. How Many Numbers Are Smaller Than the Current Number

-   For each number in the array, return how many numbers are smaller than it.

```python
--8<-- "1365_how_many_numbers_are_smaller_than_the_current_number.py"
```

## 202. Happy Number

-   Return `True` if the number is a happy number, otherwise, return `False`.
-   A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

```python
--8<-- "0202_happy_number.py"
```

## 454. 4Sum II

-   Return the number of tuples `(i, j, k, l)` such that `A[i] + B[j] + C[k] + D[l] == 0`.

```python
--8<-- "0454_4sum_ii.py"
```
