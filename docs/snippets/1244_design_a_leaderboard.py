class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

    def top(self, K: int) -> int:
        topK = sorted(self.scores.values(), reverse=True)[:K]
        return sum(topK)

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] = 0


board = Leaderboard()
board.addScore(1, 73)
board.addScore(2, 56)
board.addScore(3, 39)
board.addScore(4, 51)
print(board.top(1))  # 73
board.reset(1)
board.reset(2)
print(board.top(2))  # 90
