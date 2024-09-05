from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True


# Backtracking + Trie
def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for w in words:
        root.addWord(w)

    m, n = len(board), len(board[0])
    result, visit = set(), set()

    def dfs(r, c, node, word):
        if (
            r not in range(m)
            or c not in range(n)
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
