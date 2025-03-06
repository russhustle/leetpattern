#include <string>
#include <stack>
#include <unordered_map>
#include <cassert>
using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        unordered_map<char, char> map = {
            {')', '('},
            {']', '['},
            {'}', '{'}};

        stack<char> stack;

        for (char c : s)
        {
            if (map.find(c) != map.end())
            {
                char topElement = stack.empty() ? '#' : stack.top();
                if (topElement != map[c])
                {
                    return false;
                }
                stack.pop();
            }
            else
            {
                stack.push(c);
            }
        }

        return stack.empty();
    }
};

int main()
{
    Solution s;
    assert(s.isValid("()") == true);
    assert(s.isValid("()[]{}") == true);
    assert(s.isValid("(]") == false);
    assert(s.isValid("([)]") == false);
    assert(s.isValid("{[]}") == true);
    return 0;
}
