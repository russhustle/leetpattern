from collections import defaultdict
from typing import List


# Hierholzer's Algorithm
def findItinerary1(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    for u, v in sorted(tickets, reverse=True):
        graph[u].append(v)

    route = []

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop())
        route.append(node)

    dfs("JFK")

    return route[::-1]


# DFS + Backtracking
def findItinerary2(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    tickets.sort()
    for u, v in tickets:
        graph[u].append(v)

    res = ["JFK"]

    def dfs(node):
        if len(res) == len(tickets) + 1:
            return True
        if node not in graph:
            return False

        temp = list(graph[node])
        for i, v in enumerate(temp):
            graph[node].pop(i)
            res.append(v)
            if dfs(v):
                return True
            graph[node].insert(i, v)
            res.pop()
        return False

    dfs("JFK")

    return res


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(findItinerary1(tickets))
# ["JFK", "MUC", "LHR", "SFO", "SJC"]
print(findItinerary2(tickets))
# ["JFK", "MUC", "LHR", "SFO", "SJC"]
