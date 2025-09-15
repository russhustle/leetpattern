#include <cassert>
#include <vector>
using namespace std;

class Solution {
   public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalTank = 0, currTank = 0;
        int start = 0;
        int n = gas.size();

        for (int i = 0; i < n; i++) {
            int diff = gas[i] - cost[i];
            totalTank += diff;
            currTank += diff;

            if (currTank < 0) {
                start = i + 1;
                currTank = 0;
            }
        }

        return (totalTank >= 0) ? start : -1;
    }
};

int main() {
    Solution obj;
    vector<int> gas{1, 2, 3, 4, 5};
    vector<int> cost{3, 4, 5, 1, 2};
    int res = obj.canCompleteCircuit(gas, cost);
    assert(res == 3);
    return 0;
}