"""
-   Classic sliding window problem. Use a set to keep track of the characters in the current window.
-   Return the length of the longest substring without repeating characters.

<iframe width="560" height="315" src="https://www.youtube.com/embed/wiGpQwVHdE0?si=GlOc9C5w5Vy71iTN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
"""


# Sliding Window Variable Size
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    window = set()
    left = 0
    res = 0

    for right in range(n):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        res = max(res, right - left + 1)

    return res


s = "abcabcbb"
assert lengthOfLongestSubstring(s) == 3
