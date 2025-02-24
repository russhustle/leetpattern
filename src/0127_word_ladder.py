from collections import defaultdict, deque
from typing import List


# BFS
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    n = len(beginWord)
    graph = defaultdict(list)  # pattern: words
    wordList.append(beginWord)

    for word in wordList:
        for i in range(n):
            pattern = word[:i] + "*" + word[i + 1 :]
            graph[pattern].append(word)

    visited = set([beginWord])
    q = deque([beginWord])
    res = 1

    while q:
        size = len(q)
        for _ in range(size):
            word = q.popleft()
            if word == endWord:
                return res

            for i in range(n):
                pattern = word[:i] + "*" + word[i + 1 :]
                for neighbor in graph[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        res += 1

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord, endWord, wordList))  # 5
