---
comments: True
---

# Interval Selection

- [x] [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)
- [ ] [757. Set Intersection Size At Least Two](https://leetcode.cn/problems/set-intersection-size-at-least-two/) (Hard)

## 452. Minimum Number of Arrows to Burst Balloons

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)

-   Tags: array, greedy, sorting
-   Return the minimum number of arrows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lPmkKnvNPrw?si=P0rkcvTOxRGoFpkG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

-   Differece between two versions
    1. Start from 1: if there is no overlap, we add one more arrow.
    2. Start from the number of balloons: if there is overlap, we need to reduce one arrow.

```python title="452. Minimum Number of Arrows to Burst Balloons - Python Solution"
--8<-- "0452_minimum_number_of_arrows_to_burst_balloons.py"
```

## 757. Set Intersection Size At Least Two

-   [LeetCode](https://leetcode.com/problems/set-intersection-size-at-least-two/) | [LeetCode CH](https://leetcode.cn/problems/set-intersection-size-at-least-two/) (Hard)

-   Tags: array, greedy, sorting
