#include <array>
#include <cassert>
#include <climits>
#include <vector>
using namespace std;

class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<array<int, 2>> memo(n, {-1, -1});

        auto dfs = [&](this auto&& dfs, int i, bool hold) -> int {
            if (i < 0) {
                return hold ? INT_MIN : 0;
            }
            int& res = memo[i][hold];
            if (res != -1) {
                return res;
            }
            if (hold) {
                return res = max(dfs(i - 1, true),                // skip
                                 dfs(i - 1, false) - prices[i]);  // buy
            } else {
                return res = max(dfs(i - 1, false),              // skip
                                 dfs(i - 1, true) + prices[i]);  // sell
            }
        };

        return dfs(n - 1, false);
    }
};

int main() {
    Solution solution;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    assert(solution.maxProfit(prices) == 7);
    return 0;
}
