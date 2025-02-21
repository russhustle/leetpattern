## 376. Wiggle Subsequence

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
