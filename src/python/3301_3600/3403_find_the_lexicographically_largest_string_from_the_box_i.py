# Lexicographically Smallest/Largest
def answerString(word: str, numFriends: int) -> str:
    if numFriends == 1:
        return word

    n = len(word)
    return max(word[i : i + n - numFriends + 1] for i in range(n))


if __name__ == "__main__":
    assert answerString("dbca", 2) == "dbc"
