---
comments: true
---

# Array

## LeetCode Problems

1. 0414 - [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) | [第三大的数](https://leetcode.cn/problems/third-maximum-number/) (Easy)
2. 0169 - [Majority Element](https://leetcode.com/problems/majority-element/) | [多数元素](https://leetcode-cn.com/problems/majority-element/) (Easy)
3. 2022 - [Convert 1D Array Into 2D Array](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | [将一维数组转变成二维数组](https://leetcode.cn/problems/convert-1d-array-into-2d-array/) (Easy)
4. 0054 - [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/) (Medium)
5. 0059 - [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | [螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/) (Medium)

## 414. Third Maximum Number

-   Return the third maximum number in an array. If the third maximum does not exist, return the maximum number.

```python
--8<-- "0414_third_maximum_number.py"
```

## 169. Majority Element

-   Return the majority element in an array. The majority element is the element that appears more than `n // 2` times.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7pnhv842keE?si=fBYlNfKzdkiLgkF1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python
--8<-- "0169_majority_element.py"
```

| `num` | `count` | `res` |
| ----- | ------- | ----- |
| 2     | 1       | 2     |
| 2     | 2       | 2     |
| 1     | 1       | 2     |
| 1     | 0       | 2     |
| 1     | 1       | 1     |
| 2     | 0       | 1     |
| 2     | 1       | 2     |

## 2022. Convert 1D Array Into 2D Array

```python
--8<-- "2022_convert_1d_array_into_2d_array.py"
```

## 54. Spiral Matrix

-   Return all elements of the matrix in spiral order.

```python
--8<-- "0054_spiral_matrix.py"
```

## 59. Spiral Matrix II

-   Return a square matrix filled with elements from 1 to n^2 in spiral order.

```python
--8<-- "0059_spiral_matrix_ii.py"
```
