#include <cassert>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
   public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* cur = &dummy;
        int carry = 0;

        while (l1 || l2 || carry) {
            if (l1) {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                carry += l2->val;
                l2 = l2->next;
            }
            cur->next = new ListNode(carry % 10);
            cur = cur->next;
            carry /= 10;
        }
        return dummy.next;
    }
};

int main() {
    Solution sol;

    ListNode* l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    ListNode* l2 = new ListNode(5, new ListNode(6, new ListNode(4)));
    ListNode* result = sol.addTwoNumbers(l1, l2);

    vector<int> expected = {7, 0, 8};
    for (int val : expected) {
        assert(result != nullptr && result->val == val);
        result = result->next;
    }
    assert(result == nullptr);  // End of list

    return 0;
}