"""
-   Return the itinerary in order that visits every airport exactly once.
-   The starting airport is `JFK`.
-   If there are multiple valid itineraries, return the lexicographically smallest one.
-   Eulerian path: A path that visits every edge exactly once.
"""

from collections import defaultdict
from typing import List


# Hierholzer
def findItinerary1(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    for u, v in sorted(tickets, reverse=True):
        graph[u].append(v)

    route = []

    def dfs(node):
        while graph[node]:
            dest = graph[node].pop()
            dfs(dest)
        route.append(node)

    dfs("JFK")

    return route[::-1]


# Backtracking
def findItinerary2(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    tickets.sort()
    for u, v in tickets:
        graph[u].append(v)

    route = ["JFK"]

    def backtraking(node):
        if len(route) == len(tickets) + 1:
            return True
        if node not in graph:
            return False

        temp = list(graph[node])
        for i, v in enumerate(temp):
            graph[node].pop(i)
            route.append(v)

            if backtraking(v):
                return True

            graph[node].insert(i, v)
            route.pop()

        return False

    backtraking("JFK")

    return route


tickets = tickets = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
    ["ATL", "SFO"],
]
print(findItinerary1(tickets))
# ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
print(findItinerary2(tickets))
# ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
