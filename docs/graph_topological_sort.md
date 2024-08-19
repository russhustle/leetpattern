# Graph - Topological Sort

Topological Sort

- DAG (Directed Acyclic Graph)
- Time complexity: O(V+E)
- Space complexity: O(V+E)

Table of Contents

1. 0207 - [Course Schedule](https://leetcode.com/problems/course-schedule/) (Medium)
2. 0210 - [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (Medium)

## 207. Course Schedule

```python
--8<-- "0207_course_schedule.py"
```

## 210. Course Schedule II

```python
--8<-- "0210_course_schedule_ii.py"
```

### BFS

- 解题思路：这道题本质上是一个有向图的问题，需要找出这个图的拓扑排序。如果图中存在环，则没有办法完成所有课程，这种情况下应该返回一个空数组。

- 图的表示：我们可以使用邻接表来表示这个有向图，同时需要一个数组 indegree 来记录每个节点的入度。

- 拓扑排序（Kahn 算法）：Kahn 算法是一种基于 BFS 的拓扑排序算法：

    - 首先找出所有入度为 0 的节点，将它们加入队列。
    - 从队列中依次取出节点，放入结果集中，并将该节点指向的节点的入度减 1。
    - 如果某个节点的入度减为 0，将其加入队列。
    - 重复上述过程直到队列为空。如果最终结果集中的节点数等于课程数，则返回结果集，否则返回空数组。

- 时间复杂度：O(V+E)，其中 V 是课程数量，E 是先修课程的数量。我们需要遍历每个节点和它的边。
- 空间复杂度：O(V+E)，用来存储图的结构和入度表。
