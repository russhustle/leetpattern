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
