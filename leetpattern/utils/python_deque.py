from collections import deque

# Initialize a deque with some initial tasks
dq = deque(["a", "b", "c"])

# Append new tasks to the right (end of the queue)
dq.append("d")
dq.append("e")
# dq: deque(['a', 'b', 'c', 'd', 'e'])

# Append urgent tasks to the left (start of the queue)
dq.appendleft("urgent_task1")
dq.appendleft("urgent_task2")
# dq: deque(['urgent_task2', 'urgent_task1', 'a', 'b', 'c', 'd', 'e'])

# Pop tasks from the right (end of the queue)
b = dq.pop()
# b: 'e', dq: deque(['urgent_task2', 'urgent_task1', 'a', 'b', 'c', 'd'])

# Pop tasks from the left (start of the queue)
c = dq.popleft()
# c: 'urgent_task2', dq: deque(['urgent_task1', 'a', 'b', 'c', 'd'])

# Access the next task to be processed (by index)
d = dq[0]
# d: 'urgent_task1'

# Extend the deque by adding more tasks to the right
dq.extend(["task6", "task7"])
# dq: deque(['urgent_task1', 'a', 'b', 'c', 'd', 'task6', 'task7'])

# Extend the deque by adding more urgent tasks to the left
dq.extendleft(["urgent_task3", "urgent_task4"])
# dq: deque(['urgent_task4', 'urgent_task3', 'urgent_task1', 'a', 'b', 'c', 'd', 'task6', 'task7'])

# Rotate the deque to prioritize the last task
dq.rotate(1)
# dq: deque(['task7', 'urgent_task4', 'urgent_task3', 'urgent_task1', 'a', 'b', 'c', 'd', 'task6'])

# Clear all tasks from the deque
dq.clear()
# dq: deque([])

# Check if there are no tasks left
e = len(dq) == 0
# e: True
