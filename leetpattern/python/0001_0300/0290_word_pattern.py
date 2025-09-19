def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    p2w, w2p = {}, {}
    for p, w in zip(pattern, words):
        if (p in p2w and p2w[p] != w) or (w in w2p and w2p[w] != p):
            return False
        p2w[p] = w
        w2p[w] = p
    return True


def test_wordPattern():
    assert wordPattern("abba", "dog cat cat dog")
    assert not wordPattern("abba", "dog cat cat fish")
    assert not wordPattern("aaaa", "dog cat cat dog")
    assert not wordPattern("abba", "dog dog dog dog")
    assert wordPattern("abc", "b c a")
    assert not wordPattern("abc", "b c a a")
    assert not wordPattern("ab", "b b")
