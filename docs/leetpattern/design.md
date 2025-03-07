---
comments: True
---

# Design

- [x] [146. LRU Cache](https://leetcode.cn/problems/lru-cache/) (Medium)
- [x] [355. Design Twitter](https://leetcode.cn/problems/design-twitter/) (Medium)
- [x] [588. Design In-Memory File System](https://leetcode.cn/problems/design-in-memory-file-system/) (Hard) 👑
- [x] [460. LFU Cache](https://leetcode.cn/problems/lfu-cache/) (Hard)
- [x] [1166. Design File System](https://leetcode.cn/problems/design-file-system/) (Medium) 👑
- [x] [380. Insert Delete GetRandom O(1)](https://leetcode.cn/problems/insert-delete-getrandom-o1/) (Medium)
- [x] [362. Design Hit Counter](https://leetcode.cn/problems/design-hit-counter/) (Medium) 👑
- [x] [297. Serialize and Deserialize Binary Tree](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) (Hard)
- [x] [622. Design Circular Queue](https://leetcode.cn/problems/design-circular-queue/) (Medium)
- [x] [353. Design Snake Game](https://leetcode.cn/problems/design-snake-game/) (Medium) 👑
- [x] [1244. Design A Leaderboard](https://leetcode.cn/problems/design-a-leaderboard/) (Medium) 👑

## 146. LRU Cache

-   [LeetCode](https://leetcode.com/problems/lru-cache/) | [LeetCode CH](https://leetcode.cn/problems/lru-cache/) (Medium)

-   Tags: hash table, linked list, design, doubly linked list
- Design and implement a data structure for **Least Recently Used (LRU) cache**. It should support the following operations: get and put.
- [lru](https://media.geeksforgeeks.org/wp-content/uploads/20240909142802/Working-of-LRU-Cache-copy-2.webp)
- ![146](https://miro.medium.com/v2/resize:fit:650/0*fOwBd3z0XtHh7WN1.png)

| Data structure     | Description                   |
| ------------------ | ----------------------------- |
| Doubly Linked List | To store the key-value pairs. |
| Hash Map           | To store the key-node pairs.  |

```python title="146. LRU Cache - Python Solution"
--8<-- "0146_lru_cache.py"
```

```cpp title="146. LRU Cache - C++ Solution"
--8<-- "cpp/0146_lru_cache.cc"
```

## 355. Design Twitter

-   [LeetCode](https://leetcode.com/problems/design-twitter/) | [LeetCode CH](https://leetcode.cn/problems/design-twitter/) (Medium)

-   Tags: hash table, linked list, design, heap priority queue
-   Similar question: [23. Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard)

```python title="355. Design Twitter - Python Solution"
--8<-- "0355_design_twitter.py"
```

## 588. Design In-Memory File System

-   [LeetCode](https://leetcode.com/problems/design-in-memory-file-system/) | [LeetCode CH](https://leetcode.cn/problems/design-in-memory-file-system/) (Hard)

-   Tags: hash table, string, design, trie, sorting

```python title="588. Design In-Memory File System - Python Solution"
--8<-- "0588_design_in_memory_file_system.py"
```

## 460. LFU Cache

-   [LeetCode](https://leetcode.com/problems/lfu-cache/) | [LeetCode CH](https://leetcode.cn/problems/lfu-cache/) (Hard)

-   Tags: hash table, linked list, design, doubly linked list

```python title="460. LFU Cache - Python Solution"
--8<-- "0460_lfu_cache.py"
```

## 1166. Design File System

-   [LeetCode](https://leetcode.com/problems/design-file-system/) | [LeetCode CH](https://leetcode.cn/problems/design-file-system/) (Medium)

-   Tags: hash table, string, design, trie

```python title="1166. Design File System - Python Solution"
--8<-- "1166_design_file_system.py"
```

## 380. Insert Delete GetRandom O(1)

-   [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/) | [LeetCode CH](https://leetcode.cn/problems/insert-delete-getrandom-o1/) (Medium)

-   Tags: array, hash table, math, design, randomized

```python title="380. Insert Delete GetRandom O(1) - Python Solution"
--8<-- "0380_insert_delete_getrandom_o1.py"
```

## 362. Design Hit Counter

-   [LeetCode](https://leetcode.com/problems/design-hit-counter/) | [LeetCode CH](https://leetcode.cn/problems/design-hit-counter/) (Medium)

-   Tags: array, binary search, design, queue, data stream

```python title="362. Design Hit Counter - Python Solution"
--8<-- "0362_design_hit_counter.py"
```

## 297. Serialize and Deserialize Binary Tree

-   [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) (Hard)

-   Tags: string, tree, depth first search, breadth first search, design, binary tree

```python title="297. Serialize and Deserialize Binary Tree - Python Solution"
--8<-- "0297_serialize_and_deserialize_binary_tree.py"
```

## 622. Design Circular Queue

-   [LeetCode](https://leetcode.com/problems/design-circular-queue/) | [LeetCode CH](https://leetcode.cn/problems/design-circular-queue/) (Medium)

-   Tags: array, linked list, design, queue

```python title="622. Design Circular Queue - Python Solution"
--8<-- "0622_design_circular_queue.py"
```

## 353. Design Snake Game

-   [LeetCode](https://leetcode.com/problems/design-snake-game/) | [LeetCode CH](https://leetcode.cn/problems/design-snake-game/) (Medium)

-   Tags: array, hash table, design, queue, simulation

```python title="353. Design Snake Game - Python Solution"
--8<-- "0353_design_snake_game.py"
```

## 1244. Design A Leaderboard

-   [LeetCode](https://leetcode.com/problems/design-a-leaderboard/) | [LeetCode CH](https://leetcode.cn/problems/design-a-leaderboard/) (Medium)

-   Tags: hash table, design, sorting

```python title="1244. Design A Leaderboard - Python Solution"
--8<-- "1244_design_a_leaderboard.py"
```
