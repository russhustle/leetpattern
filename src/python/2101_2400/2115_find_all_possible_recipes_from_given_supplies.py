from collections import defaultdict, deque
from typing import List


# Topological Sort
def findAllRecipes(
    recipes: List[str], ingredients: List[List[str]], supplies: List[str]
) -> List[str]:
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for a, b in zip(recipes, ingredients):
        for i in b:
            graph[i].append(a)
        indegree[a] = len(b)

    res = []
    q = deque(supplies)

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
                res.append(nxt)
    return res


if __name__ == "__main__":
    recipes = ["bread"]
    ingredients = [["yeast", "flour"]]
    supplies = ["yeast", "flour", "corn"]
    assert findAllRecipes(recipes, ingredients, supplies) == ["bread"]
