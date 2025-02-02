from bisect import bisect_left, bisect_right, insort_left, insort_right

array = [1, 3, 3, 3, 5, 7, 9, 9, 9]
x = 3

# 1. bisect_left: find the leftmost index to insert x
print(bisect_left(array, x))  # 1

# 2. bisect_right: find the rightmost index to insert x
print(bisect_right(array, x))  # 4

# 3. insort_left: insert x into the array at the leftmost index
insort_left(array, x)
print(array)  # [1, 3, 3, 3, 3, 5, 7, 9, 9, 9]

# 4. insort_right: insert x into the array at the rightmost index
insort_right(array, x)
print(array)  # [1, 3, 3, 3, 3, 3, 5, 7, 9, 9, 9]
