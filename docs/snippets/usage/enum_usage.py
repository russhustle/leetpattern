from enum import Enum, auto


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = auto()


# Accessing enum members
print(Color.RED)  # Color.RED
print(Color.RED.name)  # RED
print(Color.RED.value)  # 1
print(Color.BLUE.value)  # 3

# Iterating over the enum
for color in Color:
    print(color)
# Color.RED
# Color.GREEN
# Color.BLUE


# Comparing enum members
print(Color.RED == Color.GREEN)  # False
print(Color.RED == Color.RED)  # True

# Accessing enum members by name
print(Color["RED"])  # Color.RED

# Accessing enum members by value
print(Color(1))  # Color.RED
