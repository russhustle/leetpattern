---
comments: True
---

# Union Find Basics

## Table of Contents

- [x] [990. Satisfiability of Equality Equations](https://leetcode.cn/problems/satisfiability-of-equality-equations/) (Medium)
- [x] [721. Accounts Merge](https://leetcode.cn/problems/accounts-merge/) (Medium)
- [ ] [737. Sentence Similarity II](https://leetcode.cn/problems/sentence-similarity-ii/) (Medium) 👑
- [x] [1101. The Earliest Moment When Everyone Become Friends](https://leetcode.cn/problems/the-earliest-moment-when-everyone-become-friends/) (Medium) 👑
- [ ] [1258. Synonymous Sentences](https://leetcode.cn/problems/synonymous-sentences/) (Medium) 👑

## 990. Satisfiability of Equality Equations

-   [LeetCode](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [LeetCode CH](https://leetcode.cn/problems/satisfiability-of-equality-equations/) (Medium)

-   Tags: array, string, union find, graph

```python title="990. Satisfiability of Equality Equations - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def equationsPossible(equations: List[str]) -> bool:
    parent = defaultdict(str)
    rank = defaultdict(int)

    def find(n):
        p = parent[n]
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return
        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p1] < rank[p2]:
            parent[p1] = p2
        else:
            parent[p2] = p1
            rank[p1] += 1

    for equation in equations:
        if equation[0] not in parent:
            parent[equation[0]] = equation[0]
            rank[equation[0]] = 1
        if equation[3] not in parent:
            parent[equation[3]] = equation[3]
            rank[equation[3]] = 1

    for equation in equations:
        if equation[1] == "=":
            union(equation[0], equation[3])

    for equation in equations:
        if equation[1] == "!":
            if find(equation[0]) == find(equation[3]):
                return False

    return True


equations = ["a==b", "b!=a"]
print(equationsPossible(equations))  # False

```

## 721. Accounts Merge

-   [LeetCode](https://leetcode.com/problems/accounts-merge/) | [LeetCode CH](https://leetcode.cn/problems/accounts-merge/) (Medium)

-   Tags: array, hash table, string, depth first search, breadth first search, union find, sorting

```python title="721. Accounts Merge - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    parent = defaultdict(str)
    rank = defaultdict(int)
    email_to_name = defaultdict(str)
    merged_accounts = defaultdict(list)

    def find(n):
        p = parent[n]
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return

        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p1] < rank[p2]:
            parent[p1] = p2
        else:
            parent[p2] = p1
            rank[p1] += 1

    for account in accounts:
        name = account[0]
        first_email = account[1]

        for email in account[1:]:
            if email not in parent:
                parent[email] = email
                rank[email] = 1
            email_to_name[email] = name
            union(first_email, email)

    for email in parent:
        root_email = find(email)
        merged_accounts[root_email].append(email)

    result = []
    for root_email, emails in merged_accounts.items():
        result.append([email_to_name[root_email]] + sorted(emails))

    return result


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
print(accountsMerge(accounts))
# [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# ['Mary', 'mary@mail.com'],
# ['John', 'johnnybravo@mail.com']]

```

## 737. Sentence Similarity II

-   [LeetCode](https://leetcode.com/problems/sentence-similarity-ii/) | [LeetCode CH](https://leetcode.cn/problems/sentence-similarity-ii/) (Medium)

-   Tags: array, hash table, string, depth first search, breadth first search, union find

## 1101. The Earliest Moment When Everyone Become Friends

-   [LeetCode](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) | [LeetCode CH](https://leetcode.cn/problems/the-earliest-moment-when-everyone-become-friends/) (Medium)

-   Tags: array, union find, sorting

```python title="1101. The Earliest Moment When Everyone Become Friends - Python Solution"
from typing import List


# Union Find
def earliestAcq(logs: List[List[int]], n: int) -> int:
    logs.sort()
    par = {i: i for i in range(n)}

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    for time, a, b in logs:
        pa, pb = find(a), find(b)
        if pa != pb:
            par[pa] = pb
            n -= 1
        if n == 1:
            return time
    return -1


logs = [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]]
n = 4
print(earliestAcq(logs, n))  # 3

```

## 1258. Synonymous Sentences

-   [LeetCode](https://leetcode.com/problems/synonymous-sentences/) | [LeetCode CH](https://leetcode.cn/problems/synonymous-sentences/) (Medium)

-   Tags: array, hash table, string, backtracking, union find
