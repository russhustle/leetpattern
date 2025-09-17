#include <cassert>
#include <vector>
using namespace std;

class Solution {
   public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = m - 1, p2 = n - 1, t = m + n - 1;

        while (p1 >= 0 || p2 >= 0) {
            if (p1 == -1) {
                nums1[t] = nums2[p2];
                p2--;
            } else if (p2 == -1) {
                nums1[t] = nums1[p1];
                p1--;
            } else if (nums1[p1] > nums2[p2]) {
                nums1[t] = nums1[p1];
                p1--;
            } else {
                nums1[t] = nums2[p2];
                p2--;
            }
            t--;
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums1 = {1, 3, 6, 0, 0, 0};
    vector<int> nums2 = {2, 5, 6};
    vector<int> output = {1, 2, 3, 5, 6, 6};
    solution.merge(nums1, 3, nums2, 3);
    assert(nums1 == output);
    return 0;
}