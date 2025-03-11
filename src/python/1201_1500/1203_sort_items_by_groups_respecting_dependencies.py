from collections import defaultdict, deque
from typing import List


# BFS - Kahn's algorithm (Topological Sort)
def sortItems(
    n: int, m: int, group: List[int], beforeItems: List[List[int]]
) -> List[int]:
    def topological_sort(graph, indegree, nodes):
        q = deque([node for node in nodes if indegree[node] == 0])
        result = []

        while q:
            node = q.popleft()
            result.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return result if len(result) == len(nodes) else []

    groupItems = defaultdict(list)
    groupGraph = defaultdict(set)
    groupIndegree = defaultdict(int)
    itemGraph = defaultdict(set)
    itemIndegree = defaultdict(int)

    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1
        groupItems[group[i]].append(i)

    for i, beforeItem in enumerate(beforeItems):
        for before in beforeItem:
            if group[before] != group[i]:
                if group[i] not in groupGraph[group[before]]:
                    groupGraph[group[before]].add(group[i])
                    groupIndegree[group[i]] += 1
            else:
                itemGraph[before].add(i)
                itemIndegree[i] += 1

    allGroups = list(set(group))
    groupOrder = topological_sort(groupGraph, groupIndegree, allGroups)
    if not groupOrder:
        return []

    result = []
    for g in groupOrder:
        items = groupItems[g]
        itemOrder = topological_sort(itemGraph, itemIndegree, items)
        if not itemOrder:
            return []
        result.extend(itemOrder)

    return result


n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
print(sortItems(n, m, group, beforeItems))
