# Hash Set
def areSentencesSimilar(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False

    sim = set(map(tuple, similarPairs))

    for i in range(len(sentence1)):
        s1, s2 = sentence1[i], sentence2[i]
        if s1 == s2 or (s1, s2) in sim or (s2, s1) in sim:
            continue
        return False

    return True


if __name__ == "__main__":
    sentence1 = ["great", "acting", "skills"]
    sentence2 = ["fine", "drama", "talent"]
    similarPairs = [
        ["great", "fine"],
        ["drama", "acting"],
        ["skills", "talent"],
    ]
    print(areSentencesSimilar(sentence1, sentence2, similarPairs))  # True
