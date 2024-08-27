# learn to use enum in python
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)