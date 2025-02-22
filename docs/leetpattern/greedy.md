---
comments: True
---

# Greedy

## 455. Assign Cookies

-  [LeetCode](https://leetcode.com/problems/assign-cookies/) | [LeetCode CH](https://leetcode.cn/problems/assign-cookies/) (Easy)

-   Return the maximum number of your content children that can be satisfied.

=== "Python"

    ```python
    --8<-- "0455_assign_cookies.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0455_assign_cookies.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0455_assign_cookies.ts"
    ```

## 1005. Maximize Sum Of Array After K Negations

-  [LeetCode](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) | [LeetCode CH](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/) (Easy)

-   Return the maximum sum of the array after changing at most `k` elements.

=== "Python"

    ```python
    --8<-- "1005_maximize_sum_of_array_after_k_negations.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1005_maximize_sum_of_array_after_k_negations.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1005_maximize_sum_of_array_after_k_negations.ts"
    ```

## 860. Lemonade Change

-  [LeetCode](https://leetcode.com/problems/lemonade-change/) | [LeetCode CH](https://leetcode.cn/problems/lemonade-change/) (Easy)

-   Return `True` if and only if you can provide every customer with correct change.

=== "Python"

    ```python
    --8<-- "0860_lemonade_change.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0860_lemonade_change.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0860_lemonade_change.ts"
    ```

## 2037. Minimum Number of Moves to Seat Everyone

-  [LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/) (Easy)

-   Return the minimum number of moves needed to seat everyone.

=== "Python"

    ```python
    --8<-- "2037_minimum_number_of_moves_to_seat_everyone.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/2037_minimum_number_of_moves_to_seat_everyone.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/2037_minimum_number_of_moves_to_seat_everyone.ts"
    ```

## 376. Wiggle Subsequence

-  [LeetCode](https://leetcode.com/problems/wiggle-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)

-   Return the length of the longest wiggle subsequence.
-   `up[n]` stores the length of the longest wiggle subsequence ending at `n` with a rising wiggle.
-   `down[n]` stores the length of the longest wiggle subsequence ending at `n` with a falling wiggle.
-   Initialize `up[0] = 1` and `down[0] = 1`.
-   Example: `nums = [1, 7, 4, 9, 2, 5]`

| `nums[n]` | `nums[n-1]` | `up[n-1]` | `down[n-1]` | `up[n]` | `down[n]` |
| :-------: | :---------: | :-------: | :---------: | :-----: | :-------: |
|     1     |      -      |     -     |      -      |    1    |     1     |
|     7     |      1      |     1     |      1      |    2    |     1     |
|     4     |      7      |     2     |      1      |    2    |     3     |
|     9     |      4      |     2     |      3      |    4    |     3     |
|     2     |      9      |     4     |      3      |    4    |     5     |
|     5     |      2      |     4     |      5      |    6    |     5     |

=== "Python"

    ```python
    --8<-- "0376_wiggle_subsequence.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0376_wiggle_subsequence.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0376_wiggle_subsequence.ts"
    ```

## 738. Monotone Increasing Digits

-  [LeetCode](https://leetcode.com/problems/monotone-increasing-digits/) | [LeetCode CH](https://leetcode.cn/problems/monotone-increasing-digits/) (Medium)

-   Return the largest number that is less than or equal to `n` with monotone increasing digits.

=== "Python"

    ```python
    --8<-- "0738_monotone_increasing_digits.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0738_monotone_increasing_digits.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0738_monotone_increasing_digits.ts"
    ```

## 122. Best Time to Buy and Sell Stock II

-  [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) (Medium)

-   Return the maximum profit you can achieve.

=== "Python"

    ```python
    --8<-- "0122_best_time_to_buy_and_sell_stock_ii.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0122_best_time_to_buy_and_sell_stock_ii.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0122_best_time_to_buy_and_sell_stock_ii.ts"
    ```

## 714. Best Time to Buy and Sell Stock with Transaction Fee

-  [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) (Medium)

-   Return the maximum profit you can achieve with the given transaction fee.

=== "Python"

    ```python
    --8<-- "0714_best_time_to_buy_and_sell_stock_with_transaction_fee.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0714_best_time_to_buy_and_sell_stock_with_transaction_fee.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0714_best_time_to_buy_and_sell_stock_with_transaction_fee.ts"
    ```

## 135. Candy

-  [LeetCode](https://leetcode.com/problems/candy/) | [LeetCode CH](https://leetcode.cn/problems/candy/) (Hard)

-   Return the minimum number of candies you must give.

=== "Python"

    ```python
    --8<-- "0135_candy.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0135_candy.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0135_candy.ts"
    ```

## 406. Queue Reconstruction by Height

-  [LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/) | [LeetCode CH](https://leetcode.cn/problems/queue-reconstruction-by-height/) (Medium)

-   Reconstruct the queue.

=== "Python"

    ```python
    --8<-- "0406_queue_reconstruction_by_height.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0406_queue_reconstruction_by_height.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0406_queue_reconstruction_by_height.ts"
    ```

## 3075. Maximize Happiness of Selected Children

-  [LeetCode](https://leetcode.com/problems/maximize-happiness-of-selected-children/) | [LeetCode CH](https://leetcode.cn/problems/maximize-happiness-of-selected-children/) (Medium)

=== "Python"

    ```python
    --8<-- "3075_maximize_happiness_of_selected_children.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/3075_maximize_happiness_of_selected_children.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/3075_maximize_happiness_of_selected_children.ts"
    ```

## 945. Minimum Increment to Make Array Unique

-  [LeetCode](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) | [LeetCode CH](https://leetcode.cn/problems/minimum-increment-to-make-array-unique/) (Medium)

=== "Python"

    ```python
    --8<-- "0945_minimum_increment_to_make_array_unique.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0945_minimum_increment_to_make_array_unique.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0945_minimum_increment_to_make_array_unique.ts"
    ```

## 53. Maximum Subarray

-  [LeetCode](https://leetcode.com/problems/maximum-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray/) (Medium)

=== "Python"

    ```python
    --8<-- "0053_maximum_subarray.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0053_maximum_subarray.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0053_maximum_subarray.ts"
    ```

## 134. Gas Station

-  [LeetCode](https://leetcode.com/problems/gas-station/) | [LeetCode CH](https://leetcode.cn/problems/gas-station/) (Medium)

=== "Python"

    ```python
    --8<-- "0134_gas_station.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0134_gas_station.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0134_gas_station.ts"
    ```

## 968. Binary Tree Cameras

-  [LeetCode](https://leetcode.com/problems/binary-tree-cameras/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-cameras/) (Hard)

=== "Python"

    ```python
    --8<-- "0968_binary_tree_cameras.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0968_binary_tree_cameras.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0968_binary_tree_cameras.ts"
    ```

## 1589. Maximum Sum Obtained of Any Permutation

-  [LeetCode](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/) (Medium)

=== "Python"

    ```python
    --8<-- "1589_maximum_sum_obtained_of_any_permutation.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1589_maximum_sum_obtained_of_any_permutation.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/1589_maximum_sum_obtained_of_any_permutation.ts"
    ```
