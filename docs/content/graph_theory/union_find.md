---
comments: True
---

# Union Find

## Table of Contents

- [x] [721. Accounts Merge](https://leetcode.cn/problems/accounts-merge/) (Medium)
- [x] [990. Satisfiability of Equality Equations](https://leetcode.cn/problems/satisfiability-of-equality-equations/) (Medium)
- [x] [1061. Lexicographically Smallest Equivalent String](https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/) (Medium)
- [x] [839. Similar String Groups](https://leetcode.cn/problems/similar-string-groups/) (Hard)

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

## 1061. Lexicographically Smallest Equivalent String

-   [LeetCode](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/) (Medium)

-   Tags: string, union find
```python title="1061. Lexicographically Smallest Equivalent String - Python Solution"
# Union Find
def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    parent = {chr(i): chr(i) for i in range(ord("a"), ord("z") + 1)}

    def find(n):
        p = parent[n]
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2

    for i in range(len(s1)):
        union(s1[i], s2[i])

    result = []
    for c in baseStr:
        result.append(find(c))

    return "".join(result)


if __name__ == "__main__":
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    assert smallestEquivalentString(s1, s2, baseStr) == "makkek"

```

## 839. Similar String Groups

-   [LeetCode](https://leetcode.com/problems/similar-string-groups/) | [LeetCode CH](https://leetcode.cn/problems/similar-string-groups/) (Hard)

-   Tags: array, hash table, string, depth first search, breadth first search, union find
```python title="839. Similar String Groups - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def numSimilarGroups(strs: List[str]) -> int:
    n = len(strs)
    parent = list(range(n))
    rank = [0 for _ in range(n)]

    def find(n):
        p = parent[n]
        while parent[p] != p:
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

    def is_similar(s1, s2):
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
            if diff > 2:
                return False
        return True

    for i in range(n):
        for j in range(i + 1, n):
            if is_similar(strs[i], strs[j]):
                union(i, j)

    return sum(find(i) == i for i in range(n))


strs = ["tars", "rats", "arts", "star"]
print(numSimilarGroups(strs))  # 2

```

