---
comments: True
---

# Trie Advanced

- [ ] [676. Implement Magic Dictionary](https://leetcode.cn/problems/implement-magic-dictionary/) (Medium)
- [x] [212. Word Search II](https://leetcode.cn/problems/word-search-ii/) (Hard)
- [ ] [3093. Longest Common Suffix Queries](https://leetcode.cn/problems/longest-common-suffix-queries/) (Hard)
- [ ] [745. Prefix and Suffix Search](https://leetcode.cn/problems/prefix-and-suffix-search/) (Hard)
- [ ] [3045. Count Prefix and Suffix Pairs II](https://leetcode.cn/problems/count-prefix-and-suffix-pairs-ii/) (Hard)
- [ ] [336. Palindrome Pairs](https://leetcode.cn/problems/palindrome-pairs/) (Hard)
- [ ] [1948. Delete Duplicate Folders in System](https://leetcode.cn/problems/delete-duplicate-folders-in-system/) (Hard)
- [ ] [425. Word Squares](https://leetcode.cn/problems/word-squares/) (Hard) 👑
- [ ] [527. Word Abbreviation](https://leetcode.cn/problems/word-abbreviation/) (Hard) 👑
- [x] [588. Design In-Memory File System](https://leetcode.cn/problems/design-in-memory-file-system/) (Hard) 👑
- [ ] [616. Add Bold Tag in String](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium) 👑
- [ ] [758. Bold Words in String](https://leetcode.cn/problems/bold-words-in-string/) (Medium) 👑
- [ ] [642. Design Search Autocomplete System](https://leetcode.cn/problems/design-search-autocomplete-system/) (Hard) 👑
- [ ] [1065. Index Pairs of a String](https://leetcode.cn/problems/index-pairs-of-a-string/) (Easy) 👑
- [x] [1166. Design File System](https://leetcode.cn/problems/design-file-system/) (Medium) 👑
- [ ] [1858. Longest Word With All Prefixes](https://leetcode.cn/problems/longest-word-with-all-prefixes/) (Medium) 👑

## 676. Implement Magic Dictionary

-   [LeetCode](https://leetcode.com/problems/implement-magic-dictionary/) | [LeetCode CH](https://leetcode.cn/problems/implement-magic-dictionary/) (Medium)

-   Tags: hash table, string, depth first search, design, trie

## 212. Word Search II

-   [LeetCode](https://leetcode.com/problems/word-search-ii/) | [LeetCode CH](https://leetcode.cn/problems/word-search-ii/) (Hard)

-   Tags: array, string, backtracking, trie, matrix

```python title="212. Word Search II - Python Solution"
from typing import List

from template import TrieNode


# Backtracking + Trie
def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for word in words:
        root.addWord(word)

    m, n = len(board), len(board[0])
    result, visit = set(), set()

    def dfs(r, c, node, word):
        if (
            r < 0
            or r >= m
            or c < 0
            or c >= n
            or (r, c) in visit
            or board[r][c] not in node.children
        ):
            return None

        visit.add((r, c))

        node = node.children[board[r][c]]
        word += board[r][c]
        if node.isWord:
            result.add(word)

        dfs(r - 1, c, node, word)
        dfs(r + 1, c, node, word)
        dfs(r, c - 1, node, word)
        dfs(r, c + 1, node, word)

        visit.remove((r, c))

    for r in range(m):
        for c in range(n):
            dfs(r, c, root, "")

    return list(result)


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
print(findWords(board, words))
# ['eat', 'oath']

```

## 3093. Longest Common Suffix Queries

-   [LeetCode](https://leetcode.com/problems/longest-common-suffix-queries/) | [LeetCode CH](https://leetcode.cn/problems/longest-common-suffix-queries/) (Hard)

-   Tags: array, string, trie

## 745. Prefix and Suffix Search

-   [LeetCode](https://leetcode.com/problems/prefix-and-suffix-search/) | [LeetCode CH](https://leetcode.cn/problems/prefix-and-suffix-search/) (Hard)

-   Tags: array, hash table, string, design, trie

## 3045. Count Prefix and Suffix Pairs II

-   [LeetCode](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-prefix-and-suffix-pairs-ii/) (Hard)

-   Tags: array, string, trie, rolling hash, string matching, hash function

## 336. Palindrome Pairs

-   [LeetCode](https://leetcode.com/problems/palindrome-pairs/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-pairs/) (Hard)

-   Tags: array, hash table, string, trie

## 1948. Delete Duplicate Folders in System

-   [LeetCode](https://leetcode.com/problems/delete-duplicate-folders-in-system/) | [LeetCode CH](https://leetcode.cn/problems/delete-duplicate-folders-in-system/) (Hard)

-   Tags: array, hash table, string, trie, hash function

## 425. Word Squares

-   [LeetCode](https://leetcode.com/problems/word-squares/) | [LeetCode CH](https://leetcode.cn/problems/word-squares/) (Hard)

-   Tags: array, string, backtracking, trie

## 527. Word Abbreviation

-   [LeetCode](https://leetcode.com/problems/word-abbreviation/) | [LeetCode CH](https://leetcode.cn/problems/word-abbreviation/) (Hard)

-   Tags: array, string, greedy, trie, sorting

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

## 616. Add Bold Tag in String

-   [LeetCode](https://leetcode.com/problems/add-bold-tag-in-string/) | [LeetCode CH](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium)

-   Tags: array, hash table, string, trie, string matching

## 758. Bold Words in String

-   [LeetCode](https://leetcode.com/problems/bold-words-in-string/) | [LeetCode CH](https://leetcode.cn/problems/bold-words-in-string/) (Medium)

-   Tags: array, hash table, string, trie, string matching

## 642. Design Search Autocomplete System

-   [LeetCode](https://leetcode.com/problems/design-search-autocomplete-system/) | [LeetCode CH](https://leetcode.cn/problems/design-search-autocomplete-system/) (Hard)

-   Tags: string, depth first search, design, trie, sorting, heap priority queue, data stream

## 1065. Index Pairs of a String

-   [LeetCode](https://leetcode.com/problems/index-pairs-of-a-string/) | [LeetCode CH](https://leetcode.cn/problems/index-pairs-of-a-string/) (Easy)

-   Tags: array, string, trie, sorting

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

## 1858. Longest Word With All Prefixes

-   [LeetCode](https://leetcode.com/problems/longest-word-with-all-prefixes/) | [LeetCode CH](https://leetcode.cn/problems/longest-word-with-all-prefixes/) (Medium)

-   Tags: depth first search, trie
