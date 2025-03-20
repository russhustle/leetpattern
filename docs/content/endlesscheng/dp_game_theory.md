---
comments: True
---

# DP Game Theory

## Table of Contents

- [x] [1025. Divisor Game](https://leetcode.cn/problems/divisor-game/) (Easy)
- [ ] [877. Stone Game](https://leetcode.cn/problems/stone-game/) (Medium)
- [ ] [486. Predict the Winner](https://leetcode.cn/problems/predict-the-winner/) (Medium)
- [ ] [1510. Stone Game IV](https://leetcode.cn/problems/stone-game-iv/) (Hard)
- [ ] [1690. Stone Game VII](https://leetcode.cn/problems/stone-game-vii/) (Medium)
- [ ] [1406. Stone Game III](https://leetcode.cn/problems/stone-game-iii/) (Hard)
- [ ] [1140. Stone Game II](https://leetcode.cn/problems/stone-game-ii/) (Medium)
- [ ] [1563. Stone Game V](https://leetcode.cn/problems/stone-game-v/) (Hard)
- [ ] [464. Can I Win](https://leetcode.cn/problems/can-i-win/) (Medium)
- [ ] [1872. Stone Game VIII](https://leetcode.cn/problems/stone-game-viii/) (Hard)
- [ ] [913. Cat and Mouse](https://leetcode.cn/problems/cat-and-mouse/) (Hard)
- [ ] [1728. Cat and Mouse II](https://leetcode.cn/problems/cat-and-mouse-ii/) (Hard)
- [ ] [294. Flip Game II](https://leetcode.cn/problems/flip-game-ii/) (Medium) 👑

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

## 877. Stone Game

-   [LeetCode](https://leetcode.com/problems/stone-game/) | [LeetCode CH](https://leetcode.cn/problems/stone-game/) (Medium)

-   Tags: array, math, dynamic programming, game theory

## 486. Predict the Winner

-   [LeetCode](https://leetcode.com/problems/predict-the-winner/) | [LeetCode CH](https://leetcode.cn/problems/predict-the-winner/) (Medium)

-   Tags: array, math, dynamic programming, recursion, game theory

## 1510. Stone Game IV

-   [LeetCode](https://leetcode.com/problems/stone-game-iv/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-iv/) (Hard)

-   Tags: math, dynamic programming, game theory

## 1690. Stone Game VII

-   [LeetCode](https://leetcode.com/problems/stone-game-vii/) | [LeetCode CH](https://leetcode.cn/problems/stone-game-vii/) (Medium)

-   Tags: array, math, dynamic programming, game theory

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
