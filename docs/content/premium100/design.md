---
comments: True
---

# Design

## Table of Contents

- [ ] [348. Design Tic-Tac-Toe](https://leetcode.cn/problems/design-tic-tac-toe/) (Medium) 👑
- [x] [353. Design Snake Game](https://leetcode.cn/problems/design-snake-game/) (Medium) 👑
- [ ] [604. Design Compressed String Iterator](https://leetcode.cn/problems/design-compressed-string-iterator/) (Easy) 👑
- [x] [271. Encode and Decode Strings](https://leetcode.cn/problems/encode-and-decode-strings/) (Medium) 👑
- [ ] [281. Zigzag Iterator](https://leetcode.cn/problems/zigzag-iterator/) (Medium) 👑
- [ ] [716. Max Stack](https://leetcode.cn/problems/max-stack/) (Hard) 👑
- [x] [1244. Design A Leaderboard](https://leetcode.cn/problems/design-a-leaderboard/) (Medium) 👑
- [x] [428. Serialize and Deserialize N-ary Tree](https://leetcode.cn/problems/serialize-and-deserialize-n-ary-tree/) (Hard) 👑
- [ ] [431. Encode N-ary Tree to Binary Tree](https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree/) (Hard) 👑

## 348. Design Tic-Tac-Toe

-   [LeetCode](https://leetcode.com/problems/design-tic-tac-toe/) | [LeetCode CH](https://leetcode.cn/problems/design-tic-tac-toe/) (Medium)

-   Tags: array, hash table, design, matrix, simulation
## 353. Design Snake Game

-   [LeetCode](https://leetcode.com/problems/design-snake-game/) | [LeetCode CH](https://leetcode.cn/problems/design-snake-game/) (Medium)

-   Tags: array, hash table, design, queue, simulation

```python title="353. Design Snake Game - Python Solution"
from collections import deque
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])  # Snake starts at the top-left corner
        self.snake_body = set([(0, 0)])  # To quickly check for collisions
        self.score = 0
        self.dirs = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}

    def move(self, direction: str) -> int:
        head = self.snake[0]
        dx, dy = self.dirs[direction]
        new_head = (head[0] + dx, head[1] + dy)

        # Check if the new head is out of bounds
        if not (
            0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width
        ):
            return -1

        # Check if the new head collides with the snake body (excluding the tail)
        if new_head in self.snake_body and new_head != self.snake[-1]:
            return -1

        # Check if the new head is on a food cell
        if self.food and self.food[0] == list(new_head):
            self.food.popleft()
            self.score += 1
        else:
            tail = self.snake.pop()
            self.snake_body.remove(tail)

        # Add the new head to the snake
        self.snake.appendleft(new_head)
        self.snake_body.add(new_head)

        return self.score


snake = SnakeGame(3, 2, [[1, 2], [0, 1]])
print(snake.move("R"))  # 0
print(snake.move("D"))  # 0
print(snake.move("R"))  # 1
print(snake.move("U"))  # 1
print(snake.move("L"))  # 2
print(snake.move("U"))  # -1

```

## 604. Design Compressed String Iterator

-   [LeetCode](https://leetcode.com/problems/design-compressed-string-iterator/) | [LeetCode CH](https://leetcode.cn/problems/design-compressed-string-iterator/) (Easy)

-   Tags: array, string, design, iterator
## 271. Encode and Decode Strings

-   [LeetCode](https://leetcode.com/problems/encode-and-decode-strings/) | [LeetCode CH](https://leetcode.cn/problems/encode-and-decode-strings/) (Medium)

-   Tags: array, string, design

```python title="271. Encode and Decode Strings - Python Solution"
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            strLen = int(s[i:j])
            decoded.append(s[j + 1 : j + 1 + strLen])
            i = j + 1 + strLen

        return decoded


# |-------------|-------------|--------------|
# |   Approach  |    Time     |    Space     |
# |-------------|-------------|--------------|
# | Two pointers|    O(n)     |     O(n)     |
# |-------------|-------------|--------------|


codec = Codec()
encoded = codec.encode(["hello", "world"])
print(encoded)  # "5#hello5#world"
decoded = codec.decode(encoded)
print(decoded)  # ["hello", "world"]

```

## 281. Zigzag Iterator

-   [LeetCode](https://leetcode.com/problems/zigzag-iterator/) | [LeetCode CH](https://leetcode.cn/problems/zigzag-iterator/) (Medium)

-   Tags: array, design, queue, iterator
## 716. Max Stack

-   [LeetCode](https://leetcode.com/problems/max-stack/) | [LeetCode CH](https://leetcode.cn/problems/max-stack/) (Hard)

-   Tags: linked list, stack, design, doubly linked list, ordered set
## 1244. Design A Leaderboard

-   [LeetCode](https://leetcode.com/problems/design-a-leaderboard/) | [LeetCode CH](https://leetcode.cn/problems/design-a-leaderboard/) (Medium)

-   Tags: hash table, design, sorting

```python title="1244. Design A Leaderboard - Python Solution"
class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

    def top(self, K: int) -> int:
        topK = sorted(self.scores.values(), reverse=True)[:K]
        return sum(topK)

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] = 0


board = Leaderboard()
board.addScore(1, 73)
board.addScore(2, 56)
board.addScore(3, 39)
board.addScore(4, 51)
print(board.top(1))  # 73
board.reset(1)
board.reset(2)
print(board.top(2))  # 90

```

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

## 431. Encode N-ary Tree to Binary Tree

-   [LeetCode](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree/) (Hard)

-   Tags: tree, depth first search, breadth first search, design, binary tree
