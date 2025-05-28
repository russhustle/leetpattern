---
comments: True
---

# Design

## Table of Contents

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
from collections import OrderedDict


# Doubly Linked List
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_last(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def move_to_last(self, node):
        self.remove(node)
        self.add_to_last(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_last(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_last(node)
            return None

        if len(self.cache) == self.cap:
            del self.cache[self.head.next.key]
            self.remove(self.head.next)

        node = Node(key=key, val=value)
        self.cache[key] = node
        self.add_to_last(node)


# OrderedDict
class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=True)
        return self.cache[key]

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
        elif len(self.cache) >= self.cap:
            self.cache.popitem(last=False)

        self.cache[key] = value


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4


cache = LRUCacheOrderedDict(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4

print("LRU Cache passed")
print("LRU Cache Ordered Dict passed")

```

```cpp title="146. LRU Cache - C++ Solution"
#include <iostream>
#include <unordered_map>
using namespace std;

class Node {
   public:
    int key;
    int val;
    Node *prev;
    Node *next;

    Node(int k = 0, int v = 0) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
   private:
    int cap;
    unordered_map<int, Node *> cache;
    Node *head;
    Node *tail;

    void remove(Node *node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void insert_to_last(Node *node) {
        tail->prev->next = node;
        node->prev = tail->prev;
        tail->prev = node;
        node->next = tail;
    }

    void move_to_last(Node *node) {
        remove(node);
        insert_to_last(node);
    }

   public:
    LRUCache(int capacity) {
        this->cap = capacity;
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (cache.find(key) != cache.end()) {
            Node *node = cache[key];
            move_to_last(node);
            return node->val;
        }
        return -1;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            Node *node = cache[key];
            node->val = value;
            move_to_last(node);
        } else {
            Node *newNode = new Node(key, value);
            cache[key] = newNode;
            insert_to_last(newNode);

            if ((int)cache.size() > cap) {
                Node *removed = head->next;
                remove(removed);
                cache.erase(removed->key);
                delete removed;
            }
        }
    }
};

int main() {
    LRUCache lru(2);
    lru.put(1, 1);
    lru.put(2, 2);
    cout << lru.get(1) << endl;  // 1
    lru.put(3, 3);
    cout << lru.get(2) << endl;  // -1
    lru.put(4, 4);
    cout << lru.get(1) << endl;  // -1
    cout << lru.get(3) << endl;  // 3
    cout << lru.get(4) << endl;  // 4
    return 0;
}

```

## 355. Design Twitter

-   [LeetCode](https://leetcode.com/problems/design-twitter/) | [LeetCode CH](https://leetcode.cn/problems/design-twitter/) (Medium)

-   Tags: hash table, linked list, design, heap priority queue
-   Similar question: [23. Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard)


```python title="355. Design Twitter - Python Solution"
import heapq
from collections import defaultdict
from typing import List


# Design
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        news_feed.extend(self.tweets[userId])
        for followee in self.followees[userId]:
            news_feed.extend(self.tweets[followee])

        return [tweet for _, tweet in heapq.nlargest(10, news_feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].discard(followeeId)


twitter = Twitter()
print(twitter.postTweet(1, 5))  # None
print(twitter.getNewsFeed(1))  # [5]
print(twitter.follow(1, 2))  # None
print(twitter.postTweet(2, 6))  # None
print(twitter.getNewsFeed(1))  # [6, 5]
print(twitter.unfollow(1, 2))  # None
print(twitter.getNewsFeed(1))  # [5]

```

## 588. Design In-Memory File System

-   [LeetCode](https://leetcode.com/problems/design-in-memory-file-system/) | [LeetCode CH](https://leetcode.cn/problems/design-in-memory-file-system/) (Hard)

-   Tags: hash table, string, design, trie, sorting

```python title="588. Design In-Memory File System - Python Solution"
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.content = ""


# Trie
class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> list:
        cur = self.root

        if path != "/":
            paths = path.split("/")[1:]
            for p in paths:
                cur = cur.children[p]
        if cur.content:
            return [path.split("/")[-1]]

        return sorted(cur.children.keys())

    def mkdir(self, path: str) -> None:
        cur = self.root
        paths = path.split("/")[1:]
        for p in paths:
            cur = cur.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        paths = filePath.split("/")[1:]
        for p in paths:
            cur = cur.children[p]
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        paths = filePath.split("/")[1:]
        for p in paths:
            cur = cur.children[p]
        return cur.content


obj = FileSystem()
obj.mkdir("/a/b/c")
obj.addContentToFile("/a/b/c/d", "hello")
print(obj.ls("/"))  # ["a"]
print(obj.readContentFromFile("/a/b/c/d"))  # "hello"

```

## 460. LFU Cache

-   [LeetCode](https://leetcode.com/problems/lfu-cache/) | [LeetCode CH](https://leetcode.cn/problems/lfu-cache/) (Hard)

-   Tags: hash table, linked list, design, doubly linked list

```python title="460. LFU Cache - Python Solution"
from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # key -> [val, freq]
        self.key_to_val_freq = {}
        # freq -> OrderedDict of keys
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def remove_least_frequent(self):

        lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        del self.key_to_val_freq[lfu_key]

        # If the frequency list is empty after removal, delete it
        if not self.freq_to_keys[self.min_freq]:
            del self.freq_to_keys[self.min_freq]

    def update_freq(self, key):
        """Updates the frequency of an existing key."""
        value, freq = self.key_to_val_freq[key]

        # Remove key from current frequency group
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Update key frequency
        new_freq = freq + 1
        self.key_to_val_freq[key] = [value, new_freq]
        self.freq_to_keys[new_freq][key] = None

    def add_new_key(self, key, value):
        if len(self.key_to_val_freq) >= self.cap:
            self.remove_least_frequent()

        # Insert the new key with frequency 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self.update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self.update_freq(key)
        else:
            self.add_new_key(key, value)


lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # 1
lfu.put(3, 3)
print(lfu.get(2))  # -1
print(lfu.get(3))  # 3
lfu.put(4, 4)
print(lfu.get(1))  # -1
print(lfu.get(3))  # 3

```

## 1166. Design File System

-   [LeetCode](https://leetcode.com/problems/design-file-system/) | [LeetCode CH](https://leetcode.cn/problems/design-file-system/) (Medium)

-   Tags: hash table, string, design, trie

```python title="1166. Design File System - Python Solution"
from collections import defaultdict


class TrieNode:
    def __init__(self, name):
        self.name = name
        self.children = defaultdict(TrieNode)
        self.value = -1


# Trie
class FileSystem:
    def __init__(self):
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split("/")[1:]
        cur = self.root

        for idx, path in enumerate(paths):
            if path not in cur.children:
                if idx == len(paths) - 1:
                    cur.children[path] = TrieNode(path)
                else:
                    return False
            cur = cur.children[path]

        if cur.value != -1:
            return False
        cur.value = value
        return True

    def get(self, path: str) -> int:
        cur = self.root
        paths = path.split("/")[1:]

        for path in paths:
            if path not in cur.children:
                return -1
            cur = cur.children[path]

        return cur.value


# Your FileSystem object will be instantiated and called as such:
path = "/a"
value = 1
obj = FileSystem()
print(obj.createPath(path, value))  # False
print(obj.get(path))  # 1

```

## 380. Insert Delete GetRandom O(1)

-   [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/) | [LeetCode CH](https://leetcode.cn/problems/insert-delete-getrandom-o1/) (Medium)

-   Tags: array, hash table, math, design, randomized

```python title="380. Insert Delete GetRandom O(1) - Python Solution"
import random


class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_element = self.list[-1]
        idx = self.dict[val]
        self.list[idx] = last_element
        self.dict[last_element] = idx
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


obj = RandomizedSet()
print(obj.insert(1))  # True
print(obj.remove(2))  # False
print(obj.insert(2))  # True
print(obj.getRandom())  # 1 or 2
print(obj.remove(1))  # True

```

## 362. Design Hit Counter

-   [LeetCode](https://leetcode.com/problems/design-hit-counter/) | [LeetCode CH](https://leetcode.cn/problems/design-hit-counter/) (Medium)

-   Tags: array, binary search, design, queue, data stream

```python title="362. Design Hit Counter - Python Solution"
from collections import deque


class HitCounter:

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Remove hits that are older than 5 minutes (300 seconds)
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))  # 3
obj.hit(300)
print(obj.getHits(300))  # 4
print(obj.getHits(301))  # 3

```

## 297. Serialize and Deserialize Binary Tree

-   [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) (Hard)

-   Tags: string, tree, depth first search, breadth first search, design, binary tree

```python title="297. Serialize and Deserialize Binary Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
class BFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1

        while q:
            node = q.popleft()

            if nodes[index] != "null":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] != "null":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1

        return root


# DFS
class DFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ["null"]
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        return ",".join(dfs(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.index = 0

        def dfs():
            if nodes[self.index] == "null":
                self.index += 1
                return None

            node = TreeNode(int(nodes[self.index]))
            self.index += 1

            node.left = dfs()
            node.right = dfs()

            return node

        root = dfs()
        return root


root = build([1, 2, 3, None, None, 4, 5])
print(root)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

bfs = BFS()
data1 = bfs.serialize(root)
print(data1)  # "1,2,3,null,null,4,5,null,null,null,null"
root1 = bfs.deserialize(data1)
print(root1)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

dfs = DFS()
data2 = dfs.serialize(root)
print(data2)  # "1,2,null,null,3,4,null,null,5,null,null"
root2 = dfs.deserialize(data2)
print(root2)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

```

## 622. Design Circular Queue

-   [LeetCode](https://leetcode.com/problems/design-circular-queue/) | [LeetCode CH](https://leetcode.cn/problems/design-circular-queue/) (Medium)

-   Tags: array, linked list, design, queue

```python title="622. Design Circular Queue - Python Solution"
# Design
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.head = 0
        self.tail = -1
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


obj = MyCircularQueue(3)
print(obj.enQueue(1))  # True
print(obj.enQueue(2))  # True
print(obj.enQueue(3))  # True
print(obj.enQueue(4))  # False
print(obj.Rear())  # 3
print(obj.isFull())  # True
print(obj.deQueue())  # True

```

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
