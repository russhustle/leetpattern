import pytest
from leetpattern.utils.trie import TrieNode, Trie


# Tests for TrieNode
def test_trienode_creation():
    node = TrieNode()
    assert node.children == {}
    assert node.is_word is False


def test_trienode_manual_setup():
    node = TrieNode()
    node.children["a"] = TrieNode()
    node.is_word = True

    assert "a" in node.children
    assert isinstance(node.children["a"], TrieNode)
    assert node.is_word is True


# Tests for Trie initialization
def test_trie_creation():
    trie = Trie()
    assert isinstance(trie.root, TrieNode)
    assert trie.root.children == {}
    assert trie.root.is_word is False


# Tests for add_word
def test_add_word_single():
    trie = Trie()
    trie.add_word("cat")

    assert "c" in trie.root.children
    assert "a" in trie.root.children["c"].children
    assert "t" in trie.root.children["c"].children["a"].children
    assert trie.root.children["c"].children["a"].children["t"].is_word is True


def test_add_word_multiple():
    trie = Trie()
    trie.add_word("cat")
    trie.add_word("car")

    # Check shared prefix "ca"
    assert "c" in trie.root.children
    assert "a" in trie.root.children["c"].children

    # Check diverging paths
    ca_node = trie.root.children["c"].children["a"]
    assert "t" in ca_node.children
    assert "r" in ca_node.children

    # Check word endings
    assert ca_node.children["t"].is_word is True
    assert ca_node.children["r"].is_word is True


def test_add_word_empty():
    trie = Trie()
    trie.add_word("")
    assert trie.root.is_word is True


def test_add_word_single_char():
    trie = Trie()
    trie.add_word("a")
    assert "a" in trie.root.children
    assert trie.root.children["a"].is_word is True


def test_add_word_overlapping():
    trie = Trie()
    trie.add_word("car")
    trie.add_word("card")

    # "car" should be a complete word
    car_node = trie.root.children["c"].children["a"].children["r"]
    assert car_node.is_word is True

    # "card" should also be a complete word
    assert "d" in car_node.children
    assert car_node.children["d"].is_word is True


def test_add_word_duplicate():
    trie = Trie()
    trie.add_word("hello")
    trie.add_word("hello")

    # Should still work correctly
    hello_node = (
        trie.root.children["h"].children["e"].children["l"].children["l"].children["o"]
    )
    assert hello_node.is_word is True


# Tests for search
def test_search_existing_word():
    trie = Trie()
    trie.add_word("hello")
    assert trie.search("hello") is True


def test_search_non_existing_word():
    trie = Trie()
    trie.add_word("hello")
    assert trie.search("world") is False


def test_search_empty_trie():
    trie = Trie()
    assert trie.search("anything") is False


def test_search_empty_string():
    trie = Trie()
    assert trie.search("") is False

    trie.add_word("")
    assert trie.search("") is True


def test_search_prefix_not_word():
    trie = Trie()
    trie.add_word("hello")
    assert trie.search("hel") is False
    assert trie.search("hell") is False


def test_search_word_is_prefix():
    trie = Trie()
    trie.add_word("car")
    trie.add_word("card")

    assert trie.search("car") is True
    assert trie.search("card") is True
    assert trie.search("ca") is False


def test_search_single_char():
    trie = Trie()
    trie.add_word("a")
    assert trie.search("a") is True
    assert trie.search("b") is False


def test_search_case_sensitive():
    trie = Trie()
    trie.add_word("Hello")
    assert trie.search("Hello") is True
    assert trie.search("hello") is False


# Tests for starts_with
def test_starts_with_existing_prefix():
    trie = Trie()
    trie.add_word("hello")
    assert trie.starts_with("hel") is True
    assert trie.starts_with("hell") is True
    assert trie.starts_with("hello") is True


def test_starts_with_non_existing_prefix():
    trie = Trie()
    trie.add_word("hello")
    assert trie.starts_with("world") is False
    assert trie.starts_with("hi") is False


def test_starts_with_empty_trie():
    trie = Trie()
    assert trie.starts_with("anything") is False


def test_starts_with_empty_string():
    trie = Trie()
    assert trie.starts_with("") is True

    trie.add_word("hello")
    assert trie.starts_with("") is True


def test_starts_with_longer_than_words():
    trie = Trie()
    trie.add_word("hi")
    assert trie.starts_with("hello") is False


def test_starts_with_exact_word():
    trie = Trie()
    trie.add_word("hello")
    assert trie.starts_with("hello") is True


def test_starts_with_multiple_words():
    trie = Trie()
    trie.add_word("cat")
    trie.add_word("car")
    trie.add_word("card")

    assert trie.starts_with("c") is True
    assert trie.starts_with("ca") is True
    assert trie.starts_with("car") is True
    assert trie.starts_with("card") is True
    assert trie.starts_with("cat") is True
    assert trie.starts_with("cb") is False


# Integration tests
def test_comprehensive_operations():
    trie = Trie()
    words = ["apple", "app", "application", "apply", "banana", "band"]

    # Add all words
    for word in words:
        trie.add_word(word)

    # Test search for all added words
    for word in words:
        assert trie.search(word) is True

    # Test search for non-existing words
    non_words = ["appl", "ap", "bana", "ban", "bandana"]
    for word in non_words:
        assert trie.search(word) is False

    # Test prefix searches
    assert trie.starts_with("app") is True
    assert trie.starts_with("ban") is True
    assert trie.starts_with("xyz") is False


def test_edge_cases():
    trie = Trie()

    # Test with special characters
    trie.add_word("hello-world")
    trie.add_word("test_case")
    trie.add_word("123")

    assert trie.search("hello-world") is True
    assert trie.search("test_case") is True
    assert trie.search("123") is True

    assert trie.starts_with("hello-") is True
    assert trie.starts_with("test_") is True
    assert trie.starts_with("12") is True


def test_unicode_support():
    trie = Trie()
    trie.add_word("café")
    trie.add_word("naïve")

    assert trie.search("café") is True
    assert trie.search("naïve") is True
    assert trie.starts_with("caf") is True
    assert trie.starts_with("naï") is True


def test_performance_with_many_words():
    trie = Trie()
    words = [f"word{i}" for i in range(1000)]

    # Add many words
    for word in words:
        trie.add_word(word)

    # Test searching
    assert trie.search("word500") is True
    assert trie.search("word999") is True
    assert trie.search("word1000") is False

    # Test prefix searching
    assert trie.starts_with("word5") is True
    assert trie.starts_with("word99") is True
    assert trie.starts_with("notword") is False
