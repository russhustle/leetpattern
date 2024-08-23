def reversePrefix(word: str, ch: str) -> str:
    if ch not in word:
        return word

    wordList = list(word)
    left, right = 0, 0

    for i in range(len(wordList)):
        if wordList[i] == ch:
            right = i
            break

    while left < right:
        wordList[left], wordList[right] = wordList[right], wordList[left]
        left += 1
        right -= 1

    return "".join(wordList)


word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))  # "dcbaefd"
