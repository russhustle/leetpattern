from collections import defaultdict
from typing import List


class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        """Parent Pointers: O(n + h) time, O(n) space.
        The first ancestor of region2 seen from region1's ancestor set is lowest.
        """
        r1 = region1
        r2 = region2

        # build a child -> parent mapping
        adj = defaultdict(str)
        for pair in regions:
            for child in pair[1:]:
                adj[child] = pair[0]

        # build the ancestor set of region1
        r1_set = set()

        while r1 in adj:
            r1_set.add(r1)
            r1 = adj[r1]

        # find the first ancestor of region2
        # that is in region1's ancestor set
        while r2 in adj:
            if r2 in r1_set:
                return r2
            r2 = adj[r2]

        return r2


def test_find_smallest_region():
    s = Solution()
    regions = [
        ["Earth", "North America", "South America"],
        ["North America", "United States", "Canada"],
        ["United States", "New York", "Boston"],
        ["Canada", "Ontario", "Quebec"],
        ["South America", "Brazil"],
    ]

    assert s.findSmallestRegion(regions, "Quebec", "New York") == "North America"
    assert s.findSmallestRegion(regions, "Canada", "Quebec") == "Canada"
    assert s.findSmallestRegion(regions, "Brazil", "Boston") == "Earth"
    assert Solution.findSmallestRegion.__doc__
