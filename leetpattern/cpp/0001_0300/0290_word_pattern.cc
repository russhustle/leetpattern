#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

bool wordPattern(const string& pattern, const string& s) {
    vector<string> words;
    istringstream iss(s);
    string word;
    while (iss >> word) {
        words.push_back(word);
    }
    if (pattern.size() != words.size()) return false;

    unordered_map<char, string> p2w;
    unordered_map<string, char> w2p;

    for (size_t i = 0; i < pattern.size(); ++i) {
        char p = pattern[i];
        const string& w = words[i];
        if ((p2w.count(p) && p2w[p] != w) || (w2p.count(w) && w2p[w] != p)) {
            return false;
        }
        p2w[p] = w;
        w2p[w] = p;
    }
    return true;
}

int main() {
    assert(wordPattern("abba", "dog cat cat dog") == true);
    assert(wordPattern("abba", "dog cat cat fish") == false);
    assert(wordPattern("aaaa", "dog cat cat dog") == false);
    assert(wordPattern("abba", "dog dog dog dog") == false);
    assert(wordPattern("abc", "b c a") == true);
    assert(wordPattern("abc", "b c a a") == false);
    assert(wordPattern("ab", "b b") == false);
    cout << "All test cases pass" << endl;
    return 0;
}
