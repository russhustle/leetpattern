---
comments: true
---

# Linked List

![Linked List Memes](../imgs/linked_list_memes.jpg){width=300px}

## LeetCode Problems

1. 0203 - [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) (Easy)
2. 0707 - [Design Linked List](https://leetcode.com/problems/design-linked-list/) (Medium)
3. 0206 - [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy)
4. 0237 - [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) (Easy)
5. 2487 - [Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list/) (Medium)
6. 0024 - [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (Medium)
7. 0019 - [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium)
8. 0160 - [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (Easy)
9. 0141 - [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy)
10. 0142 - [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium)
11. 2816 - [Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/) (Medium)
12. 0002 - [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (Medium)

```python title="template/linked_list.py"
--8<-- "template/linked_list.py"
```

## 203. Remove Linked List Elements

-   Remove all elements from a linked list of integers that have value `val`.

-   Before

```mermaid
graph LR
A[1] --> B[2]
B --> C[6]
C --> D[3]
D --> E[4]
E --> F[5]
F --> G[6]
G --> H[None]
```

-   After

```mermaid
graph LR
A[1] --> B[2]
B -.-> C[6]
C -.-> D[3]
D --> E[4]
E --> F[5]
F -.-> G[6]
B --> D[3]
F --> I[None]
```

```python
--8<-- "0203_remove_linked_list_elements.py"
```

## 707. Design Linked List

-   Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

```python
--8<-- "0707_design_linked_list.py"
```

## 206. Reverse Linked List

-   Reverse a singly linked list.

```mermaid
graph LR
A[1] --> B[2]
B --> C[3]
C --> D[4]
D --> E[5]
```

```mermaid
graph RL
E[5] --> D[4]
D --> C[3]
C --> B[2]
B --> A[1]
```

```python
--8<-- "0206_reverse_linked_list.py"
```

## 237. Delete Node in a Linked List

-   Delete a node in a singly linked list. You are given only the node to be deleted.

```python
--8<-- "0237_delete_node_in_a_linked_list.py"
```

## 2487. Remove Nodes From Linked List

-   Remove all nodes from a linked list that have a value greater than `maxValue`.

```python
--8<-- "2487_remove_nodes_from_linked_list.py"
```

## 24. Swap Nodes in Pairs

-   Given a linked list, swap every two adjacent nodes and return its head.

```python
--8<-- "0024_swap_nodes_in_pairs.py"
```

## 19. Remove Nth Node From End of List

-   Given the `head` of a linked list, remove the `n-th` node from the end of the list and return its head.

```python
--8<-- "0019_remove_nth_node_from_end_of_list.py"
```

## 160. Intersection of Two Linked Lists

-   Find the node at which the intersection of two singly linked lists begins.

```mermaid
graph LR
a1((a1)) --> a2((a2))
a2 --> c1((c1))
b1((b1)) --> b2((b2))
b2 --> b3((b3))
b3 --> c1
c1 --> c2((c2))
c2 --> c3((c3))
```

```python
--8<-- "0160_intersection_of_two_linked_lists.py"
```

## 141. Linked List Cycle

-   Determine if a linked list has a cycle in it.

```mermaid
graph LR
A[3] --> B[2]
B --> C[0]
C --> D[-4]
```

```mermaid
graph LR
A[3] --> B[2]
B --> C[0]
C --> D[-4]
D --> B
```

```python
--8<-- "0141_linked_list_cycle.py"
```

## 142. Linked List Cycle II

-   Given a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

```mermaid
graph LR
A[3] --> B[2]
B --> C[0]
C --> D[-4]
D --> B
```

```python
--8<-- "0142_linked_list_cycle_ii.py"
```

## 2816. Double a Number Represented as a Linked List

-   Given a number represented as a linked list, double it and return the resulting linked list.

```python
--8<-- "2816_double_a_number_represented_as_a_linked_list.py"
```

## 2. Add Two Numbers

-   Represent the sum of two numbers as a linked list.

```python
--8<-- "0002_add_two_numbers.py"
```
