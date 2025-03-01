#include <vector>
#include <numeric>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

class Solution
{
public:
    int minimumBoxes(vector<int> &apple, vector<int> &capacity)
    {
        int s = accumulate(apple.begin(), apple.end(), 0);
        sort(capacity.begin(), capacity.end(), greater<int>());

        int i = 0;
        while (s > 0)
        {
            s -= capacity[i++];
        }
        return i;
    }
};

int main()
{
    Solution s;
    vector<int> apple = {1, 3, 2};
    vector<int> capacity = {4, 3, 1, 5, 2};
    cout << s.minimumBoxes(apple, capacity) << endl;
    return 0;
}
