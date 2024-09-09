from collections import defaultdict, deque
from typing import List


# BFS
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    # TC: O(N * M^2)
    # SC: O(N * M)
    # N = len(wordList), M = len(word)

    if endWord not in wordList:
        return 0

    graph = defaultdict(list)  # {pattern: [word1, word2, ...]}
    wordList.append(beginWord)

    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1 :]
            graph[pattern].append(word)

    visited = set([beginWord])
    q = deque([beginWord])
    steps = 1

    while q:
        for _ in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return steps

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                for neighbor in graph[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        steps += 1

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord, endWord, wordList))  # 5
