from typing import List


def binary_search(a: List[int], x: int) -> int:
    """
    Perform binary search to find the index of x in sorted list a.
    Returns the index if found, else -1.

    Args:
        a (List[int]): Sorted list of integers.
        x (int): Target value to search for.

    Returns:
        int: Index of x if found, else -1.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        if a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1


def bisect_left(a: List[int], x: int) -> int:
    """
    Locate the insertion point for x in sorted list a to maintain sorted order (left).

    Args:
        a (List[int]): Sorted list of integers.
        x (int): Target value to search for.

    Returns:
        int: Index to insert x to keep a sorted (leftmost).

    Examples:
        >>> bisect_left([1, 2, 4, 4, 5], 4)
        2
        >>> bisect_left([1, 2, 4, 4, 5], 3)
        2
    """
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l


def bisect_right(a: List[int], x: int) -> int:
    """
    Locate the insertion point for x in sorted list a to maintain sorted order (right).

    Args:
        a (List[int]): Sorted list of integers.
        x (int): Target value to search for.

    Returns:
        int: Index to insert x to keep a sorted (rightmost).

    Examples:
        >>> bisect_right([1, 2, 4, 4, 5], 4)
        4
        >>> bisect_right([1, 2, 4, 4, 5], 3)
        2
    """
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] <= x:
            l = m + 1
        else:
            r = m
    return l


def find_first(a: List[int], x: int) -> int:
    i = bisect_left(a, x)
    return i if i < len(a) and a[i] == x else -1


def find_last(a: List[int], x: int) -> int:
    i = bisect_right(a, x) - 1
    return i if i >= 0 and a[i] == x else -1


def count_occurrences(a: List[int], x: int) -> int:
    first = find_first(a, x)
    if first == -1:
        return 0
    last = find_last(a, x)
    return last - first + 1


def closest_element(a: List[int], x: int) -> int:
    if not a:
        return -1

    l, r = 0, len(a) - 1
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m

    if l == 0:
        return 0

    return l - 1 if abs(a[l - 1] - x) <= abs(a[l] - x) else l


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binary_search(nums, target))  # 4
