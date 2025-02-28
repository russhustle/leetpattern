---
comments: True
---

# Topological Sorting

- [x] [1557. Minimum Number of Vertices to Reach All Nodes](https://leetcode.cn/problems/minimum-number-of-vertices-to-reach-all-nodes/) (Medium)
- [x] [210. Course Schedule II](https://leetcode.cn/problems/course-schedule-ii/) (Medium)
- [ ] [1462. Course Schedule IV](https://leetcode.cn/problems/course-schedule-iv/) (Medium)
- [ ] [2115. Find All Possible Recipes from Given Supplies](https://leetcode.cn/problems/find-all-possible-recipes-from-given-supplies/) (Medium)
- [ ] [851. Loud and Rich](https://leetcode.cn/problems/loud-and-rich/) (Medium)
- [ ] [310. Minimum Height Trees](https://leetcode.cn/problems/minimum-height-trees/) (Medium)
- [ ] [2392. Build a Matrix With Conditions](https://leetcode.cn/problems/build-a-matrix-with-conditions/) (Hard)
- [x] [802. Find Eventual Safe States](https://leetcode.cn/problems/find-eventual-safe-states/) (Medium)
- [ ] [1591. Strange Printer II](https://leetcode.cn/problems/strange-printer-ii/) (Hard)
- [x] [1203. Sort Items by Groups Respecting Dependencies](https://leetcode.cn/problems/sort-items-by-groups-respecting-dependencies/) (Hard)
- [ ] [2603. Collect Coins in a Tree](https://leetcode.cn/problems/collect-coins-in-a-tree/) (Hard)
- [x] [269. Alien Dictionary](https://leetcode.cn/problems/alien-dictionary/) (Hard)
- [ ] [444. Sequence Reconstruction](https://leetcode.cn/problems/sequence-reconstruction/) (Medium)
- [ ] [1059. All Paths from Source Lead to Destination](https://leetcode.cn/problems/all-paths-from-source-lead-to-destination/) (Medium)
- [x] [1136. Parallel Courses](https://leetcode.cn/problems/parallel-courses/) (Medium)

## 1557. Minimum Number of Vertices to Reach All Nodes

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-vertices-to-reach-all-nodes/) (Medium)
-   Tags: graph
-   Return a list of integers representing the minimum number of vertices needed to traverse all the nodes.
-   ✅ Return the vertices with indegree 0.

![1557](../assets/1557.png){width=300px}

-   `edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]`
-   Initialization

|   `src`   |  0  |  0  |  2  |  3  |  4  |     |
| :-------: | :-: | :-: | :-: | :-: | :-: | :-: |
|   `dst`   |  1  |  2  |  5  |  4  |  2  |     |
|   node    |  0  |  1  |  2  |  3  |  4  |  5  |
| in-degree |  0  |  0  |  0  |  0  |  0  |  0  |

|   `src`   |   0   |   0   |  2  |  3  |  4  |     |
| :-------: | :---: | :---: | :-: | :-: | :-: | :-: |
|   `dst`   | **1** |   2   |  5  |  4  |  2  |     |
|   node    |   0   | **1** |  2  |  3  |  4  |  5  |
| in-degree |   0   | **1** |  0  |  0  |  0  |  0  |

|   `src`   |  0  |   0   |   2   |  3  |  4  |     |
| :-------: | :-: | :---: | :---: | :-: | :-: | :-: |
|   `dst`   |  1  | **2** |   5   |  4  |  2  |     |
|   node    |  0  |   1   | **2** |  3  |  4  |  5  |
| in-degree |  0  |   1   | **1** |  0  |  0  |  0  |

|   `src`   |  0  |  0  |   2   |  3  |  4  |       |
| :-------: | :-: | :-: | :---: | :-: | :-: | :---: |
|   `dst`   |  1  |  2  | **5** |  4  |  2  |       |
|   node    |  0  |  1  |   2   |  3  |  4  | **5** |
| in-degree |  0  |  1  |   1   |  0  |  0  | **1** |

|   `src`   |  0  |  0  |  2  |   3   |   4   |     |
| :-------: | :-: | :-: | :-: | :---: | :---: | :-: |
|   `dst`   |  1  |  2  |  5  | **4** |   2   |     |
|   node    |  0  |  1  |  2  |   3   | **4** |  5  |
| in-degree |  0  |  1  |  1  |   0   | **1** |  1  |

|   `src`   |  0  |  0  |   2   |  3  |   4   |     |
| :-------: | :-: | :-: | :---: | :-: | :---: | :-: |
|   `dst`   |  1  |  2  |   5   |  4  | **2** |     |
|   node    |  0  |  1  | **2** |  3  |   4   |  5  |
| in-degree |  0  |  1  | **2** |  0  |   1   |  1  |

```python title="1557. Minimum Number of Vertices to Reach All Nodes"
--8<-- "1557_minimum_number_of_vertices_to_reach_all_nodes.py"
```

## 210. Course Schedule II

-   [LeetCode](https://leetcode.com/problems/course-schedule-ii/) | [LeetCode CH](https://leetcode.cn/problems/course-schedule-ii/) (Medium)
-   Tags: depth first search, breadth first search, graph, topological sort
-   Return the ordering of courses you should take to finish all courses. If there are multiple valid answers, return any of them.

![0207](../assets/0207.png){width=300px}

```python title="210. Course Schedule II"
--8<-- "0210_course_schedule_ii.py"
```

## 1462. Course Schedule IV

-   [LeetCode](https://leetcode.com/problems/course-schedule-iv/) | [LeetCode CH](https://leetcode.cn/problems/course-schedule-iv/) (Medium)
-   Tags: depth first search, breadth first search, graph, topological sort

## 2115. Find All Possible Recipes from Given Supplies

-   [LeetCode](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/) | [LeetCode CH](https://leetcode.cn/problems/find-all-possible-recipes-from-given-supplies/) (Medium)
-   Tags: array, hash table, string, graph, topological sort

## 851. Loud and Rich

-   [LeetCode](https://leetcode.com/problems/loud-and-rich/) | [LeetCode CH](https://leetcode.cn/problems/loud-and-rich/) (Medium)
-   Tags: array, depth first search, graph, topological sort

## 310. Minimum Height Trees

-   [LeetCode](https://leetcode.com/problems/minimum-height-trees/) | [LeetCode CH](https://leetcode.cn/problems/minimum-height-trees/) (Medium)
-   Tags: depth first search, breadth first search, graph, topological sort

## 2392. Build a Matrix With Conditions

-   [LeetCode](https://leetcode.com/problems/build-a-matrix-with-conditions/) | [LeetCode CH](https://leetcode.cn/problems/build-a-matrix-with-conditions/) (Hard)
-   Tags: array, graph, topological sort, matrix

## 802. Find Eventual Safe States

-   [LeetCode](https://leetcode.com/problems/find-eventual-safe-states/) | [LeetCode CH](https://leetcode.cn/problems/find-eventual-safe-states/) (Medium)
-   Tags: depth first search, breadth first search, graph, topological sort

```python title="802. Find Eventual Safe States"
--8<-- "0802_find_eventual_safe_states.py"
```

## 1591. Strange Printer II

-   [LeetCode](https://leetcode.com/problems/strange-printer-ii/) | [LeetCode CH](https://leetcode.cn/problems/strange-printer-ii/) (Hard)
-   Tags: array, graph, topological sort, matrix

## 1203. Sort Items by Groups Respecting Dependencies

-   [LeetCode](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) | [LeetCode CH](https://leetcode.cn/problems/sort-items-by-groups-respecting-dependencies/) (Hard)
-   Tags: depth first search, breadth first search, graph, topological sort
-   Return any permutation of the items that satisfies the requirements.

```python title="1203. Sort Items by Groups Respecting Dependencies"
--8<-- "1203_sort_items_by_groups_respecting_dependencies.py"
```

## 2603. Collect Coins in a Tree

-   [LeetCode](https://leetcode.com/problems/collect-coins-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/collect-coins-in-a-tree/) (Hard)
-   Tags: array, tree, graph, topological sort

## 269. Alien Dictionary

-   [LeetCode](https://leetcode.com/problems/alien-dictionary/) | [LeetCode CH](https://leetcode.cn/problems/alien-dictionary/) (Hard)
-   Tags: array, string, depth first search, breadth first search, graph, topological sort
-   Return the correct order of characters in the alien language.

```python title="269. Alien Dictionary"
--8<-- "0269_alien_dictionary.py"
```

## 444. Sequence Reconstruction

-   [LeetCode](https://leetcode.com/problems/sequence-reconstruction/) | [LeetCode CH](https://leetcode.cn/problems/sequence-reconstruction/) (Medium)
-   Tags: array, graph, topological sort

## 1059. All Paths from Source Lead to Destination

-   [LeetCode](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/) | [LeetCode CH](https://leetcode.cn/problems/all-paths-from-source-lead-to-destination/) (Medium)
-   Tags: graph, topological sort

## 1136. Parallel Courses

-   [LeetCode](https://leetcode.com/problems/parallel-courses/) | [LeetCode CH](https://leetcode.cn/problems/parallel-courses/) (Medium)
-   Tags: graph, topological sort
-   Return the minimum number of semesters needed to take all courses.

![1136](../assets/1136.png){width=300px}

```python title="1136. Parallel Courses"
--8<-- "1136_parallel_courses.py"
```
