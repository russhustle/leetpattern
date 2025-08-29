"""
### Trie

- A trie is a tree-like data structure whose nodes store the letters of an alphabet.

```mermaid
flowchart TD
Root(( ))
Root --- C1(("C"))
Root --- D((D))
C1 --- A1(("A"))
A1 --- T1(("T"))
A1 --- R1(("R"))
A1 --- N((N))
Root --- B1((B))
B1 --- A2((A))
A2 --- T2((T))
A2 --- R2((R))
```
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("word"))  # False
print(obj.startsWith("app"))  # True
