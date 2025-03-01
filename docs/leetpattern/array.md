---
comments: True
---

# Array

- [x] [414. Third Maximum Number](https://leetcode.cn/problems/third-maximum-number/) (Easy)
- [x] [169. Majority Element](https://leetcode.cn/problems/majority-element/) (Easy)
- [x] [2022. Convert 1D Array Into 2D Array](https://leetcode.cn/problems/convert-1d-array-into-2d-array/) (Easy)
- [x] [54. Spiral Matrix](https://leetcode.cn/problems/spiral-matrix/) (Medium)
- [x] [59. Spiral Matrix II](https://leetcode.cn/problems/spiral-matrix-ii/) (Medium)

## 414. Third Maximum Number

-   [LeetCode](https://leetcode.com/problems/third-maximum-number/) | [LeetCode CH](https://leetcode.cn/problems/third-maximum-number/) (Easy)

-   Tags: array, sorting
-   Return the third maximum number in an array. If the third maximum does not exist, return the maximum number.

```python title="414. Third Maximum Number - Python Solution"
--8<-- "0414_third_maximum_number.py"
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

## 2022. Convert 1D Array Into 2D Array

-   [LeetCode](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | [LeetCode CH](https://leetcode.cn/problems/convert-1d-array-into-2d-array/) (Easy)

-   Tags: array, matrix, simulation

```python title="2022. Convert 1D Array Into 2D Array - Python Solution"
--8<-- "2022_convert_1d_array_into_2d_array.py"
```

## 54. Spiral Matrix

-   [LeetCode](https://leetcode.com/problems/spiral-matrix/) | [LeetCode CH](https://leetcode.cn/problems/spiral-matrix/) (Medium)

-   Tags: array, matrix, simulation
-   Return all elements of the matrix in spiral order.

```python title="54. Spiral Matrix - Python Solution"
--8<-- "0054_spiral_matrix.py"
```

## 59. Spiral Matrix II

-   [LeetCode](https://leetcode.com/problems/spiral-matrix-ii/) | [LeetCode CH](https://leetcode.cn/problems/spiral-matrix-ii/) (Medium)

-   Tags: array, matrix, simulation
-   Return a square matrix filled with elements from 1 to n^2 in spiral order.

```python title="59. Spiral Matrix II - Python Solution"
--8<-- "0059_spiral_matrix_ii.py"
```
