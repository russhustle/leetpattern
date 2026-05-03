import heapq


class TaskManager:
    def __init__(self, tasks):
        self.heap = []
        self.tasks = {}  # taskId -> (userId, priority)

        for userId, taskId, priority in tasks:
            self.tasks[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, userId))

    def add(self, userId, taskId, priority):
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId, newPriority):
        userId, _ = self.tasks[taskId]
        self.tasks[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId):
        if taskId in self.tasks:
            del self.tasks[taskId]

    def execTop(self):
        # lazy deletion: pop from heap until we find a valid task
        while self.heap:
            priority, taskId, userId = heapq.heappop(self.heap)
            taskId = -taskId
            priority = -priority

            if taskId in self.tasks and self.tasks[taskId] == (userId, priority):
                del self.tasks[taskId]
                return userId

        return -1


def test_TaskManager():
    tm = TaskManager([[1, 1, 10], [2, 2, 20], [3, 3, 15]])
    assert tm.execTop() == 2
    tm.edit(1, 25)
    assert tm.execTop() == 1
    tm.rmv(3)
    assert tm.execTop() == -1
    tm.add(4, 4, 30)
    assert tm.execTop() == 4
    print("All test cases passed!")
