from collections import defaultdict
from typing import List


# DFS
def maxAmount(
    initialCurrency: str,
    pairs1: List[List[str]],
    rates1: List[float],
    pairs2: List[List[str]],
    rates2: List[float],
) -> float:

    def cal_amount(pairs, rates, initialCurrency):
        graph = defaultdict(list)

        for (u, v), r in zip(pairs, rates):
            graph[u].append((v, r))
            graph[v].append((u, 1.0 / r))

        amount = {}

        def dfs(x, cur):
            amount[x] = cur
            for to, rate in graph[x]:
                if to not in amount:
                    dfs(to, cur * rate)

        dfs(initialCurrency, 1.0)

        return amount

    day1 = cal_amount(pairs1, rates1, initialCurrency)
    day2 = cal_amount(pairs2, rates2, initialCurrency)

    return max(day1.get(x, 0.0) / a2 for x, a2 in day2.items())


if __name__ == "__main__":
    initialCurrency = "EUR"
    pairs1 = [["EUR", "USD"], ["USD", "JPY"]]
    rates1 = [2.0, 3.0]
    pairs2 = [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]]
    rates2 = [4.0, 5.0, 6.0]

    assert maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2) == 720.0
