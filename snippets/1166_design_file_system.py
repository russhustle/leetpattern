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
