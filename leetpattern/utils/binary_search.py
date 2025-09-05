from typing import List


def binary_search(arr: List[int], val: int) -> int:
    """
    Perform binary search to find the index of val in sorted list arr.
    Returns the index if found, else -1.

    Args:
        arr (List[int]): Sorted list of integers.
        val (int): Target value to search for.

    Returns:
        int: Index of val if found, else -1.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def bisect_left(arr: List[int], val: int) -> int:
    """
    Locate the insertion point for val in sorted list arr to maintain sorted order (left).

    Args:
        arr (List[int]): Sorted list of integers.
        val (int): Target value to search for.

    Returns:
        int: Index to insert val to keep arr sorted (leftmost).

    Examples:
        >>> bisect_left([1, 2, 4, 4, 5], 4)
        2
        >>> bisect_left([1, 2, 4, 4, 5], 3)
        2
    """
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < val:
            low = mid + 1
        else:
            high = mid
    return low


def bisect_right(arr: List[int], val: int) -> int:
    """
    Locate the insertion point for val in sorted list arr to maintain sorted order (right).

    Args:
        arr (List[int]): Sorted list of integers.
        val (int): Target value to search for.

    Returns:
        int: Index to insert val to keep arr sorted (rightmost).

    Examples:
        >>> bisect_right([1, 2, 4, 4, 5], 4)
        4
        >>> bisect_right([1, 2, 4, 4, 5], 3)
        2
    """
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= val:
            low = mid + 1
        else:
            high = mid
    return low


def find_first(arr: List[int], val: int) -> int:
    i = bisect_left(arr, val)
    return i if i < len(arr) and arr[i] == val else -1


def find_last(arr: List[int], val: int) -> int:
    i = bisect_right(arr, val) - 1
    return i if i >= 0 and arr[i] == val else -1


def count_occurrences(arr: List[int], val: int) -> int:
    first = find_first(arr, val)
    if first == -1:
        return 0
    last = find_last(arr, val)
    return last - first + 1


def closest_element(arr: List[int], val: int) -> int:
    if not arr:
        return -1

    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < val:
            low = mid + 1
        else:
            high = mid

    if low == 0:
        return 0

    return low - 1 if abs(arr[low - 1] - val) <= abs(arr[low] - val) else low


if __name__ == "__main__":
    arr = [-1, 0, 3, 5, 9, 12]
    val = 9
    print(binary_search(arr, val))  # 4
