---
comments: True
---

# Dijkstra's

## 787. Cheapest Flights Within K Stops

-   [LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | [LeetCode CH](https://leetcode.cn/problems/cheapest-flights-within-k-stops/) (Medium)
-   Tags: dynamic programming, depth first search, breadth first search, graph, heap priority queue, shortest path
-   Return the cheapest price from `src` to `dst` with at most `K` stops.

```mermaid
graph TD
0((0))
1((1))
2((2))
3((3))
0 --> |100| 1
1 --> |600| 3
1 --> |100| 2
2 --> |100| 0
2 --> |200| 3
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/5eIK3zUdYmE?si=aBR0VbHXTgNuVlGz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python
--8<-- "0787_cheapest_flights_within_k_stops.py"
```

## 1514. Path with Maximum Probability

-   [LeetCode](https://leetcode.com/problems/path-with-maximum-probability/) | [LeetCode CH](https://leetcode.cn/problems/path-with-maximum-probability/) (Medium)
-   Tags: array, graph, heap priority queue, shortest path

```python
--8<-- "1514_path_with_maximum_probability.py"
```

## 505. The Maze II

-   [LeetCode](https://leetcode.com/problems/the-maze-ii/) | [LeetCode CH](https://leetcode.cn/problems/the-maze-ii/) (Medium)
-   Tags: array, depth first search, breadth first search, graph, heap priority queue, matrix, shortest path

```python
--8<-- "0505_the_maze_ii.py"
```

## 499. The Maze III

-   [LeetCode](https://leetcode.com/problems/the-maze-iii/) | [LeetCode CH](https://leetcode.cn/problems/the-maze-iii/) (Hard)
-   Tags: array, string, depth first search, breadth first search, graph, heap priority queue, matrix, shortest path

```python
--8<-- "0499_the_maze_iii.py"
```
