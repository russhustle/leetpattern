---
comments: True
---

# Bipartite Graph Coloring

- [x] [785. Is Graph Bipartite?](https://leetcode.cn/problems/is-graph-bipartite/) (Medium)
- [x] [886. Possible Bipartition](https://leetcode.cn/problems/possible-bipartition/) (Medium)

## 785. Is Graph Bipartite?

-   [LeetCode](https://leetcode.com/problems/is-graph-bipartite/) | [LeetCode CH](https://leetcode.cn/problems/is-graph-bipartite/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph
-   Determine if a graph is bipartite.

How to group

|          | Uncolored | Color 1 | Color 2 | Operation   |
| -------- | --------- | ------- | ------- | ----------- |
| Method 1 | -1        | 0       | 1       | `1 - color` |
| Method 2 | 0         | 1       | -1      | `-color`    |

```python title="785. Is Graph Bipartite? - Python Solution"
--8<-- "0785_is_graph_bipartite.py"
```

## 886. Possible Bipartition

-   [LeetCode](https://leetcode.com/problems/possible-bipartition/) | [LeetCode CH](https://leetcode.cn/problems/possible-bipartition/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph
-   Determine if a graph can be divided into two groups such that no two nodes of the same group are connected.

```python title="886. Possible Bipartition - Python Solution"
--8<-- "0886_possible_bipartition.py"
```
