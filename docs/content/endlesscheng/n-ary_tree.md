---
comments: True
---

# N-ary Tree

## Table of Contents

- [ ] [589. N-ary Tree Preorder Traversal](https://leetcode.cn/problems/n-ary-tree-preorder-traversal/) (Easy)
- [ ] [590. N-ary Tree Postorder Traversal](https://leetcode.cn/problems/n-ary-tree-postorder-traversal/) (Easy)
- [ ] [559. Maximum Depth of N-ary Tree](https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/) (Easy)
- [x] [429. N-ary Tree Level Order Traversal](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/) (Medium)
- [ ] [427. Construct Quad Tree](https://leetcode.cn/problems/construct-quad-tree/) (Medium)
- [ ] [558. Logical OR of Two Binary Grids Represented as Quad-Trees](https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/) (Medium)
- [x] [428. Serialize and Deserialize N-ary Tree](https://leetcode.cn/problems/serialize-and-deserialize-n-ary-tree/) (Hard) 👑
- [ ] [1490. Clone N-ary Tree](https://leetcode.cn/problems/clone-n-ary-tree/) (Medium) 👑
- [ ] [1506. Find Root of N-Ary Tree](https://leetcode.cn/problems/find-root-of-n-ary-tree/) (Medium) 👑
- [x] [1522. Diameter of N-Ary Tree](https://leetcode.cn/problems/diameter-of-n-ary-tree/) (Medium) 👑
- [ ] [1516. Move Sub-Tree of N-Ary Tree](https://leetcode.cn/problems/move-sub-tree-of-n-ary-tree/) (Hard) 👑

## 589. N-ary Tree Preorder Traversal

-   [LeetCode](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) | [LeetCode CH](https://leetcode.cn/problems/n-ary-tree-preorder-traversal/) (Easy)

-   Tags: stack, tree, depth first search
## 590. N-ary Tree Postorder Traversal

-   [LeetCode](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) | [LeetCode CH](https://leetcode.cn/problems/n-ary-tree-postorder-traversal/) (Easy)

-   Tags: stack, tree, depth first search
## 559. Maximum Depth of N-ary Tree

-   [LeetCode](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search
## 429. N-ary Tree Level Order Traversal

-   [LeetCode](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/) (Medium)

-   Tags: tree, breadth first search

```python title="429. N-ary Tree Level Order Traversal - Python Solution"
from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)

            for child in node.children:
                queue.append(child)

        result.append(level)

    return result


root = Node(
    1,
    [
        Node(
            3,
            [
                Node(5, []),
                Node(6, []),
            ],
        ),
        Node(2, []),
        Node(4, []),
    ],
)
print(levelOrder(root))  # [[1], [3, 2, 4], [5, 6]]

```

## 427. Construct Quad Tree

-   [LeetCode](https://leetcode.com/problems/construct-quad-tree/) | [LeetCode CH](https://leetcode.cn/problems/construct-quad-tree/) (Medium)

-   Tags: array, divide and conquer, tree, matrix
## 558. Logical OR of Two Binary Grids Represented as Quad-Trees

-   [LeetCode](https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/) | [LeetCode CH](https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/) (Medium)

-   Tags: divide and conquer, tree
## 428. Serialize and Deserialize N-ary Tree

-   [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/serialize-and-deserialize-n-ary-tree/) (Hard)

-   Tags: string, tree, depth first search, breadth first search

```python title="428. Serialize and Deserialize N-ary Tree - Python Solution"
from typing import List, Optional


class Node(object):
    def __init__(
        self,
        val: Optional[int] = None,
        children: Optional[List["Node"]] = None,
    ):
        if children is None:
            children = []
        self.val = val
        self.children = children


# DFS
class CodecDFS:
    def serialize(self, root: "Node") -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return "*"

        data = ""
        data += str(root.val) + "|" + str(len(root.children))
        for child in root.children:
            data += "|" + self.serialize(child)
        return data

    def deserialize(self, data: str) -> "Node":
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == "*":
            return None

        data = data.split("|")[::-1]

        def dfs(data):
            root = Node(int(data.pop()))
            size = int(data.pop())
            for i in range(size):
                root.children.append(dfs(data))
            return root

        return dfs(data)


if __name__ == "__main__":
    obj = CodecDFS()
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    data = obj.serialize(root)
    print(data)  # 1|3|3|2|5|0|6|0|2|0|4|0
    root = obj.deserialize(data)
    print(root.val)  # 1
    print(root.children[0].val)  # 3
    print(root.children[1].val)  # 2
    print(root.children[2].val)  # 4
    print(root.children[0].children[0].val)  # 5

```

## 1490. Clone N-ary Tree

-   [LeetCode](https://leetcode.com/problems/clone-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/clone-n-ary-tree/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search
## 1506. Find Root of N-Ary Tree

-   [LeetCode](https://leetcode.com/problems/find-root-of-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-root-of-n-ary-tree/) (Medium)

-   Tags: hash table, bit manipulation, tree, depth first search
## 1522. Diameter of N-Ary Tree

-   [LeetCode](https://leetcode.com/problems/diameter-of-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/diameter-of-n-ary-tree/) (Medium)

-   Tags: tree, depth first search

```python title="1522. Diameter of N-Ary Tree - Python Solution"
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: Optional[int] = None,
        children: Optional[List["Node"]] = None,
    ):
        self.val = val
        self.children = children if children is not None else []


def diameter(root: "Node") -> int:

    def dfs(node):
        if not node.children:
            return 1, 1
        mx0, mx1 = 0, 0
        mxf = 0
        for child in node.children:
            hl, fl = dfs(child)
            mxf = max(mxf, fl)
            if hl > mx1:
                if hl < mx0:
                    mx1 = hl
                else:
                    mx0, mx1 = hl, mx0
        return mx0 + 1, max(mxf, mx0 + mx1 + 1)

    return dfs(root)[1] - 1


root = [1, None, 2, None, 3, 4, None, 5, None, 6]
root = Node(1)
root.children = [Node(2)]
root.children[0].children = [Node(3), Node(4)]
root.children[0].children[0].children = [Node(5)]
root.children[0].children[1].children = [Node(6)]
print(diameter(root))  # 4

```

## 1516. Move Sub-Tree of N-Ary Tree

-   [LeetCode](https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/move-sub-tree-of-n-ary-tree/) (Hard)

-   Tags: tree, depth first search
