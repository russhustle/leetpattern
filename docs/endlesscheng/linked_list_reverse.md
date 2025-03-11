---
comments: True
---

# Linked List Reverse

- [x] [206. Reverse Linked List](https://leetcode.cn/problems/reverse-linked-list/) (Easy)
- [x] [92. Reverse Linked List II](https://leetcode.cn/problems/reverse-linked-list-ii/) (Medium)
- [x] [24. Swap Nodes in Pairs](https://leetcode.cn/problems/swap-nodes-in-pairs/) (Medium)
- [ ] [25. Reverse Nodes in k-Group](https://leetcode.cn/problems/reverse-nodes-in-k-group/) (Hard)
- [ ] [2074. Reverse Nodes in Even Length Groups](https://leetcode.cn/problems/reverse-nodes-in-even-length-groups/) (Medium)

## 206. Reverse Linked List

-   [LeetCode](https://leetcode.com/problems/reverse-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/reverse-linked-list/) (Easy)

-   Tags: linked list, recursion
- Reverse a singly linked list.

```mermaid
graph LR
A((1)) --> B((2))
B --> C((3))
C --> D((4))
D --> E((5))
```

```mermaid
graph RL
E((5)) --> D((4))
D --> C((3))
C --> B((2))
B --> A((1))
```

```python title="206. Reverse Linked List - Python Solution"
--8<-- "0206_reverse_linked_list.py"
```

## 92. Reverse Linked List II

-   [LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/) | [LeetCode CH](https://leetcode.cn/problems/reverse-linked-list-ii/) (Medium)

-   Tags: linked list
- Reverse a linked list from position left to position right. Return the linked list after reversing.

```mermaid
graph LR
A((1)) --> B((2))
B --> C((3))
C --> D((4))
D --> E((5))
```

```mermaid
graph LR
A((1)) --> B((4))
B --> C((3))
C --> D((2))
D --> E((5))
```

```python title="92. Reverse Linked List II - Python Solution"
--8<-- "0092_reverse_linked_list_ii.py"
```

## 24. Swap Nodes in Pairs

-   [LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/) | [LeetCode CH](https://leetcode.cn/problems/swap-nodes-in-pairs/) (Medium)

-   Tags: linked list, recursion
-   Given a linked list, swap every two adjacent nodes and return its head.

```python title="24. Swap Nodes in Pairs - Python Solution"
--8<-- "0024_swap_nodes_in_pairs.py"
```

## 25. Reverse Nodes in k-Group

-   [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [LeetCode CH](https://leetcode.cn/problems/reverse-nodes-in-k-group/) (Hard)

-   Tags: linked list, recursion

## 2074. Reverse Nodes in Even Length Groups

-   [LeetCode](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/) | [LeetCode CH](https://leetcode.cn/problems/reverse-nodes-in-even-length-groups/) (Medium)

-   Tags: linked list
