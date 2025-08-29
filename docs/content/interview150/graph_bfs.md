---
comments: True
---

# Graph BFS

## Table of Contents

- [ ] [909. Snakes and Ladders](https://leetcode.cn/problems/snakes-and-ladders/) (Medium)
- [x] [433. Minimum Genetic Mutation](https://leetcode.cn/problems/minimum-genetic-mutation/) (Medium)
- [x] [127. Word Ladder](https://leetcode.cn/problems/word-ladder/) (Hard)

## 909. Snakes and Ladders

-   [LeetCode](https://leetcode.com/problems/snakes-and-ladders/) | [LeetCode CH](https://leetcode.cn/problems/snakes-and-ladders/) (Medium)

-   Tags: array, breadth first search, matrix
## 433. Minimum Genetic Mutation

-   [LeetCode](https://leetcode.com/problems/minimum-genetic-mutation/) | [LeetCode CH](https://leetcode.cn/problems/minimum-genetic-mutation/) (Medium)

-   Tags: hash table, string, breadth first search
```python title="433. Minimum Genetic Mutation - Python Solution"
from collections import deque
from typing import List


# BFS
def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    if endGene not in bank:
        return -1

    bank = set(bank)
    q = deque([(startGene, 0)])

    while q:
        gene, step = q.popleft()
        if gene == endGene:
            return step

        for i in range(8):
            for c in "ACGT":
                if gene[i] == c:
                    continue
                newGene = gene[:i] + c + gene[i + 1 :]
                if newGene in bank:
                    bank.remove(newGene)
                    q.append((newGene, step + 1))
    return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(minMutation(startGene, endGene, bank))  # 2

```

## 127. Word Ladder

-   [LeetCode](https://leetcode.com/problems/word-ladder/) | [LeetCode CH](https://leetcode.cn/problems/word-ladder/) (Hard)

-   Tags: hash table, string, breadth first search
-   The most classic BFS problem.
-   Return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
-   Approach: BFS
-   Time Complexity: O(n * m^2)
-   Space Complexity: O(n * m)

```python title="127. Word Ladder - Python Solution"
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

```

