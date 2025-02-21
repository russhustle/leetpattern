---
comments: true
---

# Graph - Coloring

## Bipartite Graph

![graph_bipartite](../assets/graph_bipartite.png){width=300px}

How to group

|          | Uncolored | Color 1 | Color 2 | Operation   |
| -------- | --------- | ------- | ------- | ----------- |
| Method 1 | -1        | 0       | 1       | `1 - color` |
| Method 2 | 0         | 1       | -1      | `-color`    |

## LeetCode Problems

1. 0785 - [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | [判断二分图](https://leetcode.cn/problems/is-graph-bipartite/) (Medium)
2. 0886 - [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) | [可能的二分法](https://leetcode.cn/problems/possible-bipartition/) (Medium)
3. 0924 - [Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/) | [尽量减少恶意软件的传播](https://leetcode.cn/problems/minimize-malware-spread/) (Hard)

## 785. Is Graph Bipartite?

-   Determine if a graph is bipartite.

```python
--8<-- "0785_is_graph_bipartite.py"
```

## 886. Possible Bipartition

-   Determine if a graph can be divided into two groups such that no two nodes of the same group are connected.

```python
--8<-- "0886_possible_bipartition.py"
```

## 0924. Minimize Malware Spread

```python
--8<-- "0924_minimize_malware_spread.py"
```
