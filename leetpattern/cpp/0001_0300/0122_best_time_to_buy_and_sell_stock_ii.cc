#include <array>
#include <cassert>
#include <climits>
#include <vector>
using namespace std;

class Solution {
   public:
    int maxProfitMemo(vector<int>& prices) {
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

    int maxProfitIterative(vector<int>& prices) {
        int n = prices.size();
        vector<array<int, 2>> dp(n, {0, 0});
        dp[0][0] = -prices[0];
        dp[0][1] = 0;

        for (int i = 1; i < n; i++) {
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]);  // buy
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i]);  // sell
        }
        return dp[n - 1][1];
    }

    int maxProfitIterativeOptimized(vector<int>& prices) {
        int n = prices.size();
        if (n <= 1) return 0;

        int hold = -prices[0], res = 0;

        for (int i = 1; i < n; i++) {
            hold = max(hold, res - prices[i]);  // buy
            res = max(res, hold + prices[i]);   // sell
        }
        return res;
    }

    int maxProfitGreedy(vector<int>& prices) {
        int n = prices.size();
        if (n <= 1) return 0;

        int res = 0;

        for (int i = 1; i < n; i++) {
            if (prices[i] > prices[i - 1]) {
                res += prices[i] - prices[i - 1];
            }
        }
        return res;
    }
};

int main() {
    Solution solution;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    assert(solution.maxProfitMemo(prices) == 7);
    assert(solution.maxProfitIterative(prices) == 7);
    assert(solution.maxProfitIterativeOptimized(prices) == 7);
    assert(solution.maxProfitGreedy(prices) == 7);
    return 0;
}
