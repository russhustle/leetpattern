---
comments: True
---

# DP Jump Game

## Table of Contents

- [x] [1306. Jump Game III](https://leetcode.cn/problems/jump-game-iii/) (Medium)
- [ ] [2770. Maximum Number of Jumps to Reach the Last Index](https://leetcode.cn/problems/maximum-number-of-jumps-to-reach-the-last-index/) (Medium)
- [ ] [403. Frog Jump](https://leetcode.cn/problems/frog-jump/) (Hard)
- [ ] [1340. Jump Game V](https://leetcode.cn/problems/jump-game-v/) (Hard)
- [ ] [1871. Jump Game VII](https://leetcode.cn/problems/jump-game-vii/) (Medium)
- [ ] [1696. Jump Game VI](https://leetcode.cn/problems/jump-game-vi/) (Medium)
- [ ] [975. Odd Even Jump](https://leetcode.cn/problems/odd-even-jump/) (Hard)
- [ ] [1654. Minimum Jumps to Reach Home](https://leetcode.cn/problems/minimum-jumps-to-reach-home/) (Medium)
- [ ] [656. Coin Path](https://leetcode.cn/problems/coin-path/) (Hard) 👑
- [ ] [2297. Jump Game VIII](https://leetcode.cn/problems/jump-game-viii/) (Medium) 👑

## 1306. Jump Game III

-   [LeetCode](https://leetcode.com/problems/jump-game-iii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-iii/) (Medium)

-   Tags: array, depth first search, breadth first search

```python title="1306. Jump Game III - Python Solution"
from collections import deque
from typing import List


# BFS
def canReach(arr: List[int], start: int) -> bool:
    n = len(arr)
    visited = [False for _ in range(n)]
    q = deque([start])

    while q:
        i = q.popleft()

        if arr[i] == 0:
            return True

        visited[i] = True

        for j in [i - arr[i], i + arr[i]]:
            if j in range(n) and not visited[j]:
                q.append(j)

    return False


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(canReach(arr, start))  # True

```

## 2770. Maximum Number of Jumps to Reach the Last Index

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-jumps-to-reach-the-last-index/) (Medium)

-   Tags: array, dynamic programming

## 403. Frog Jump

-   [LeetCode](https://leetcode.com/problems/frog-jump/) | [LeetCode CH](https://leetcode.cn/problems/frog-jump/) (Hard)

-   Tags: array, dynamic programming

## 1340. Jump Game V

-   [LeetCode](https://leetcode.com/problems/jump-game-v/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-v/) (Hard)

-   Tags: array, dynamic programming, sorting

## 1871. Jump Game VII

-   [LeetCode](https://leetcode.com/problems/jump-game-vii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-vii/) (Medium)

-   Tags: string, dynamic programming, sliding window, prefix sum

## 1696. Jump Game VI

-   [LeetCode](https://leetcode.com/problems/jump-game-vi/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-vi/) (Medium)

-   Tags: array, dynamic programming, queue, heap priority queue, monotonic queue

## 975. Odd Even Jump

-   [LeetCode](https://leetcode.com/problems/odd-even-jump/) | [LeetCode CH](https://leetcode.cn/problems/odd-even-jump/) (Hard)

-   Tags: array, dynamic programming, stack, monotonic stack, ordered set

## 1654. Minimum Jumps to Reach Home

-   [LeetCode](https://leetcode.com/problems/minimum-jumps-to-reach-home/) | [LeetCode CH](https://leetcode.cn/problems/minimum-jumps-to-reach-home/) (Medium)

-   Tags: array, dynamic programming, breadth first search

## 656. Coin Path

-   [LeetCode](https://leetcode.com/problems/coin-path/) | [LeetCode CH](https://leetcode.cn/problems/coin-path/) (Hard)

-   Tags: array, dynamic programming

## 2297. Jump Game VIII

-   [LeetCode](https://leetcode.com/problems/jump-game-viii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-viii/) (Medium)

-   Tags: array, dynamic programming, stack, graph, monotonic stack, shortest path
