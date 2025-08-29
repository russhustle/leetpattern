from collections import Counter

# Basic
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(data)
print(counter)
# Counter({"apple": 3, "banana": 2, "orange": 1})


# Create
c1 = Counter()  # Empty
print(c1)  # Counter()

c2 = Counter("aabbc")  # String
print(c2)
# Counter({"a": 2, "b": 2, "c": 1})

c3 = Counter({"a": 2, "b": 1})  # Dictionary
print(c3)  # Counter({"a": 2, "b": 1})

c4 = Counter(a=2, b=1)  # Keyword arguments
print(c4)  # Counter({"a": 2, "b": 1})


# Update
counter = Counter(["a", "b", "c"])
print(counter)
# Counter({"a": 1, "b": 1, "c": 1})
counter.update(["a", "b", "c", "a"])  # <--
print(counter)
# Counter({"a": 3, "b": 2, "c": 2})


# 4.Subtract
counter.subtract(["a"])
print(counter)
# Counter({"a": 2, "b": 2, "c": 2})


# 5. Access
print(counter["a"])  # 2


# 6. Delete
del counter["a"]
print(counter)
# Counter({"b": 2, "c": 2})


# 7. Existence
print("a" in counter)  # False
print("b" in counter)  # True


# 8. Elements
counter = Counter(a=2, b=1, c=3)
print(list(counter.elements()))  # ["a", "a", "b", "c", "c", "c"]


# 9. Most common
print(counter.most_common(2))  # [("c", 3), ("a", 2)]
