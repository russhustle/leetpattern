---
comments: True
---

# Standard Traversal

- [x] [547. Number of Provinces](https://leetcode.cn/problems/number-of-provinces/) (Medium)
- [x] [802. Find Eventual Safe States](https://leetcode.cn/problems/find-eventual-safe-states/) (Medium)
- [x] [841. Keys and Rooms](https://leetcode.cn/problems/keys-and-rooms/) (Medium)
- [x] [1129. Shortest Path with Alternating Colors](https://leetcode.cn/problems/shortest-path-with-alternating-colors/) (Medium)
- [x] [1376. Time Needed to Inform All Employees](https://leetcode.cn/problems/time-needed-to-inform-all-employees/) (Medium)
- [x] [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)
- [x] [797. All Paths From Source to Target](https://leetcode.cn/problems/all-paths-from-source-to-target/) (Medium)
- [x] [1192. Critical Connections in a Network](https://leetcode.cn/problems/critical-connections-in-a-network/) (Hard)

## 547. Number of Provinces

-   [LeetCode](https://leetcode.com/problems/number-of-provinces/) | [LeetCode CH](https://leetcode.cn/problems/number-of-provinces/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph
-   Return the number of provinces.

### Union Find

-   Find by Path Compression
-   Union by Rank
-   Time Complexity: O(log(n))
-   Space Complexity: O(n)

```python title="template/union_find.py"
--8<-- "template/union_find.py"
```

```python title="547. Number of Provinces - Python Solution"
--8<-- "0547_number_of_provinces.py"
```

## 802. Find Eventual Safe States

-   [LeetCode](https://leetcode.com/problems/find-eventual-safe-states/) | [LeetCode CH](https://leetcode.cn/problems/find-eventual-safe-states/) (Medium)

-   Tags: depth first search, breadth first search, graph, topological sort

```python title="802. Find Eventual Safe States - Python Solution"
--8<-- "0802_find_eventual_safe_states.py"
```

## 841. Keys and Rooms

-   [LeetCode](https://leetcode.com/problems/keys-and-rooms/) | [LeetCode CH](https://leetcode.cn/problems/keys-and-rooms/) (Medium)

-   Tags: depth first search, breadth first search, graph

```python title="841. Keys and Rooms - Python Solution"
--8<-- "0841_keys_and_rooms.py"
```

## 1129. Shortest Path with Alternating Colors

-   [LeetCode](https://leetcode.com/problems/shortest-path-with-alternating-colors/) | [LeetCode CH](https://leetcode.cn/problems/shortest-path-with-alternating-colors/) (Medium)

-   Tags: breadth first search, graph

```python title="1129. Shortest Path with Alternating Colors - Python Solution"
--8<-- "1129_shortest_path_with_alternating_colors.py"
```

## 1376. Time Needed to Inform All Employees

-   [LeetCode](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | [LeetCode CH](https://leetcode.cn/problems/time-needed-to-inform-all-employees/) (Medium)

-   Tags: tree, depth first search, breadth first search

```python title="1376. Time Needed to Inform All Employees - Python Solution"
--8<-- "1376_time_needed_to_inform_all_employees.py"
```

## 1466. Reorder Routes to Make All Paths Lead to the City Zero

-   [LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | [LeetCode CH](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (Medium)

-   Tags: depth first search, breadth first search, graph
-   ![1466](https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png)

```python title="1466. Reorder Routes to Make All Paths Lead to the City Zero - Python Solution"
--8<-- "1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero.py"
```

## 797. All Paths From Source to Target

-   [LeetCode](https://leetcode.com/problems/all-paths-from-source-to-target/) | [LeetCode CH](https://leetcode.cn/problems/all-paths-from-source-to-target/) (Medium)

-   Tags: backtracking, depth first search, breadth first search, graph

```python title="797. All Paths From Source to Target - Python Solution"
--8<-- "0797_all_paths_from_source_to_target.py"
```

## 1192. Critical Connections in a Network

-   [LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/) | [LeetCode CH](https://leetcode.cn/problems/critical-connections-in-a-network/) (Hard)

-   Tags: depth first search, graph, biconnected component

```python title="1192. Critical Connections in a Network - Python Solution"
--8<-- "1192_critical_connections_in_a_network.py"
```
