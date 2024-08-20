from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            self.parent[rootQ] = rootP


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    email_to_id = {}
    uf = UnionFind(len(accounts))

    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_id:
                uf.union(i, email_to_id[email])
            email_to_id[email] = i

    id_to_emails = defaultdict(list)
    for email, id_ in email_to_id.items():
        id_to_emails[uf.find(id_)].append(email)

    return [
        [accounts[id_][0]] + sorted(emails)
        for id_, emails in id_to_emails.items()
    ]


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]

print(accountsMerge(accounts))
# [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
#  ['Mary', 'mary@mail.com'],
#  ['John', 'johnnybravo@mail.com']]
