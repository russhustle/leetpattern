-   ![42](../assets/0042.png)
-   Method 1: Dynamic Programing

| index                           | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  |
| :------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value                           | 0   | 1   | 0   | 2   | 1   | 0   | 1   | 3   | 2   | 1   | 2   | 1   |
| `maxLeft`                       | 0   | 0   | 1   | 1   | 2   | 2   | 2   | 2   | 3   | 3   | 3   | 3   |
| `maxRight`                      | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 2   | 2   | 2   | 1   | 0   |
| `hold = min(maxLeft, maxRight)` | 0   | 0   | 1   | 1   | 2   | 2   | 2   | 2   | 2   | 2   | 1   | 0   |
| `trap = max(0, hold - value)`   | 0   | 0   | 1   | 0   | 1   | 2   | 1   | 0   | 0   | 1   | 0   | 0   |

So, In total we have trap `1 + 1 + 2 + 1 + 1 = 6` water.

-   Method 2: Left Right Pointers, because we always need to care about the minimum of left right maximum numbers. So, we can use two pointers to keep track of the left and right maximum numbers.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZI2z5pq0TqA?si=OEYg01dbmzvmtIwZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
