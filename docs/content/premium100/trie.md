---
comments: True
---

# Trie

## Table of Contents

- [x] [588. Design In-Memory File System](https://leetcode.cn/problems/design-in-memory-file-system/) (Hard) 👑
- [ ] [642. Design Search Autocomplete System](https://leetcode.cn/problems/design-search-autocomplete-system/) (Hard) 👑

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

## 642. Design Search Autocomplete System

-   [LeetCode](https://leetcode.com/problems/design-search-autocomplete-system/) | [LeetCode CH](https://leetcode.cn/problems/design-search-autocomplete-system/) (Hard)

-   Tags: string, depth first search, design, trie, sorting, heap priority queue, data stream
