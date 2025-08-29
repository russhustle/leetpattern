---
comments: True
---

# Game Theory

## Table of Contents

- [ ] [292. Nim Game](https://leetcode.cn/problems/nim-game/) (Easy)
- [x] [1025. Divisor Game](https://leetcode.cn/problems/divisor-game/) (Easy)
- [ ] [3227. Vowels Game in a String](https://leetcode.cn/problems/vowels-game-in-a-string/) (Medium)
- [ ] [2038. Remove Colored Pieces if Both Neighbors are the Same Color](https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) (Medium)
- [ ] [877. Stone Game](https://leetcode.cn/problems/stone-game/) (Medium)
- [ ] [1510. Stone Game IV](https://leetcode.cn/problems/stone-game-iv/) (Hard)
- [ ] [486. Predict the Winner](https://leetcode.cn/problems/predict-the-winner/) (Medium)
- [ ] [1690. Stone Game VII](https://leetcode.cn/problems/stone-game-vii/) (Medium)
- [ ] [1686. Stone Game VI](https://leetcode.cn/problems/stone-game-vi/) (Medium)
- [ ] [1927. Sum Game](https://leetcode.cn/problems/sum-game/) (Medium)
- [ ] [1406. Stone Game III](https://leetcode.cn/problems/stone-game-iii/) (Hard)
- [ ] [1140. Stone Game II](https://leetcode.cn/problems/stone-game-ii/) (Medium)
- [ ] [1563. Stone Game V](https://leetcode.cn/problems/stone-game-v/) (Hard)
- [ ] [464. Can I Win](https://leetcode.cn/problems/can-i-win/) (Medium)
- [ ] [2029. Stone Game IX](https://leetcode.cn/problems/stone-game-ix/) (Medium)
- [ ] [810. Chalkboard XOR Game](https://leetcode.cn/problems/chalkboard-xor-game/) (Hard)
- [ ] [1872. Stone Game VIII](https://leetcode.cn/problems/stone-game-viii/) (Hard)
- [ ] [913. Cat and Mouse](https://leetcode.cn/problems/cat-and-mouse/) (Hard)
- [ ] [1728. Cat and Mouse II](https://leetcode.cn/problems/cat-and-mouse-ii/) (Hard)
- [ ] [294. Flip Game II](https://leetcode.cn/problems/flip-game-ii/) (Medium) 👑
- [ ] [1908. Game of Nim](https://leetcode.cn/problems/game-of-nim/) (Medium) 👑
- [ ] [2005. Subtree Removal Game with Fibonacci Tree](https://leetcode.cn/problems/subtree-removal-game-with-fibonacci-tree/) (Hard) 👑
- [ ] [2868. The Wording Game](https://leetcode.cn/problems/the-wording-game/) (Hard) 👑

## 292. Nim Game

-   [LeetCode](https://leetcode.com/problems/nim-game/) | [LeetCode CH](https://leetcode.cn/problems/nim-game/) (Easy)

-   Tags: math, brainteaser, game theory
## 1025. Divisor Game

-   [LeetCode](https://leetcode.com/problems/divisor-game/) | [LeetCode CH](https://leetcode.cn/problems/divisor-game/) (Easy)

-   Tags: math, dynamic programming, brainteaser, game theory
-   Return `True` if Alice wins the game, assuming both players play optimally.
-   `dp[n]` stores the result of the game when the number is `n`.
-   Initialize `dp[1] = False`.

```python title="1025. Divisor Game - Python Solution"
# DP
def divisorGameDP(n: int) -> bool:
    if n <= 1:
        return False

    dp = [False for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0 and not dp[i - j]:
                dp[i] = True
                break

    return dp[n]


# Math
def divisorGameDPMath(n: int) -> bool:
    return n % 2 == 0


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |  DP         |      O(n^2)     |    O(n)      |
# |  Math       |      O(1)       |    O(1)      |
# |-------------|-----------------|--------------|

n = 2
print(divisorGameDP(n))  # True
print(divisorGameDPMath(n))  # True

```

## 3227. Vowels Game in a String

-   [LeetCode](https://leetcode.com/problems/vowels-game-in-a-string/) | [LeetCode CH](https://leetcode.cn/problems/vowels-game-in-a-string/) (Medium)

-   Tags: math, string, brainteaser, game theory
## 2038. Remove Colored Pieces if Both Neighbors are the Same Color

-   [LeetCode](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) | [LeetCode CH](https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) (Medium)

-   Tags: math, string, greedy, game theory
## 877. Stone Game

-   [LeetCode](https://leetcode.com/problems/stone-game/) | [LeetCode CH](https://leetcode.cn/problems/stone-game/) (Medium)

-   Tags: array, math, dynamic programming, game theory
## 1510. Stone Game IV

-   [LeetCode](https://leetcode.com/problems/stone-game-iv/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-iv/) (Hard)

-   Tags: math, dynamic programming, game theory
## 486. Predict the Winner

-   [LeetCode](https://leetcode.com/problems/predict-the-winner/) | [LeetCode CH](https://leetcode.cn/problems/predict-the-winner/) (Medium)

-   Tags: array, math, dynamic programming, recursion, game theory
## 1690. Stone Game VII

-   [LeetCode](https://leetcode.com/problems/stone-game-vii/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-vii/) (Medium)

-   Tags: array, math, dynamic programming, game theory
## 1686. Stone Game VI

-   [LeetCode](https://leetcode.com/problems/stone-game-vi/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-vi/) (Medium)

-   Tags: array, math, greedy, sorting, heap priority queue, game theory
## 1927. Sum Game

-   [LeetCode](https://leetcode.com/problems/sum-game/) | [LeetCode CH](https://leetcode.cn/problems/sum-game/) (Medium)

-   Tags: math, string, greedy, game theory
## 1406. Stone Game III

-   [LeetCode](https://leetcode.com/problems/stone-game-iii/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-iii/) (Hard)

-   Tags: array, math, dynamic programming, game theory
## 1140. Stone Game II

-   [LeetCode](https://leetcode.com/problems/stone-game-ii/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-ii/) (Medium)

-   Tags: array, math, dynamic programming, prefix sum, game theory
## 1563. Stone Game V

-   [LeetCode](https://leetcode.com/problems/stone-game-v/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-v/) (Hard)

-   Tags: array, math, dynamic programming, game theory
## 464. Can I Win

-   [LeetCode](https://leetcode.com/problems/can-i-win/) | [LeetCode CH](https://leetcode.cn/problems/can-i-win/) (Medium)

-   Tags: math, dynamic programming, bit manipulation, memoization, game theory, bitmask
## 2029. Stone Game IX

-   [LeetCode](https://leetcode.com/problems/stone-game-ix/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-ix/) (Medium)

-   Tags: array, math, greedy, counting, game theory
## 810. Chalkboard XOR Game

-   [LeetCode](https://leetcode.com/problems/chalkboard-xor-game/) | [LeetCode CH](https://leetcode.cn/problems/chalkboard-xor-game/) (Hard)

-   Tags: array, math, bit manipulation, brainteaser, game theory
## 1872. Stone Game VIII

-   [LeetCode](https://leetcode.com/problems/stone-game-viii/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-viii/) (Hard)

-   Tags: array, math, dynamic programming, prefix sum, game theory
## 913. Cat and Mouse

-   [LeetCode](https://leetcode.com/problems/cat-and-mouse/) | [LeetCode CH](https://leetcode.cn/problems/cat-and-mouse/) (Hard)

-   Tags: math, dynamic programming, graph, topological sort, memoization, game theory
## 1728. Cat and Mouse II

-   [LeetCode](https://leetcode.com/problems/cat-and-mouse-ii/) | [LeetCode CH](https://leetcode.cn/problems/cat-and-mouse-ii/) (Hard)

-   Tags: array, math, dynamic programming, graph, topological sort, memoization, matrix, game theory
## 294. Flip Game II

-   [LeetCode](https://leetcode.com/problems/flip-game-ii/) | [LeetCode CH](https://leetcode.cn/problems/flip-game-ii/) (Medium)

-   Tags: math, dynamic programming, backtracking, memoization, game theory
## 1908. Game of Nim

-   [LeetCode](https://leetcode.com/problems/game-of-nim/) | [LeetCode CH](https://leetcode.cn/problems/game-of-nim/) (Medium)

-   Tags: array, math, dynamic programming, bit manipulation, brainteaser, game theory
## 2005. Subtree Removal Game with Fibonacci Tree

-   [LeetCode](https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/) | [LeetCode CH](https://leetcode.cn/problems/subtree-removal-game-with-fibonacci-tree/) (Hard)

-   Tags: math, dynamic programming, tree, binary tree, game theory
## 2868. The Wording Game

-   [LeetCode](https://leetcode.com/problems/the-wording-game/) | [LeetCode CH](https://leetcode.cn/problems/the-wording-game/) (Hard)

-   Tags: array, math, two pointers, string, greedy, game theory
