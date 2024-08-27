# Binary Tree Traversal

![tree](imgs/binary-tree.png)

| Traversal   | Order             | Method         | Result                        |
| ----------- | ----------------- | -------------- | ----------------------------- |
| Preorder    | Root, Left, Right | DFS or Stack   | `[0, 1, 3, 4, 2, 5, 6]`       |
| Inorder     | Left, Root, Right | DFS or Stack   | `[3, 1, 4, 0, 5, 2, 6]`       |
| Postorder   | Left, Right, Root | DFS or Stack   | `[3, 4, 1, 5, 6, 2, 0]`       |
| Level Order | Level by Level    | BFS with Queue | `[[0], [1, 2], [3, 4, 5, 6]]` |

## LeetCode Problems

1. 0144 - [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) (Easy)
2. 0094 - [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (Easy)
3. 0145 - [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) (Easy)
4. 0102 - [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (Medium)
5. 0107 - [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) (Medium)
6. 0103 - [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) (Medium)

## 144. Binary Tree Preorder Traversal

```python
--8<-- "0144_binary_tree_preorder_traversal.py"
```

## 94. Binary Tree Inorder Traversal

```python
--8<-- "0094_binary_tree_inorder_traversal.py"
```

## 145. Binary Tree Postorder Traversal

```python
--8<-- "0145_binary_tree_postorder_traversal.py"
```

## 102. Binary Tree Level Order Traversal

```python
--8<-- "0102_binary_tree_level_order_traversal.py"
```

## 107. Binary Tree Level Order Traversal II

```python
--8<-- "0107_binary_tree_level_order_traversal_ii.py"
```

## 103. Binary Tree Zigzag Level Order Traversal

```python
--8<-- "0103_binary_tree_zigzag_level_order_traversal.py"
```
