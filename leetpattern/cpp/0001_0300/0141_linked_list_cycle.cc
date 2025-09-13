#include <cassert>
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
   public:
    bool hasCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (fast == slow) return true;
        }
        return false;
    }
};

int main() {
    Solution sol;

    ListNode* head = new ListNode(3);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(-4);
    head->next->next->next->next = head->next;  // Create a cycle
    assert(sol.hasCycle(head) == true);

    ListNode* head2 = new ListNode(1);
    head2->next = new ListNode(2);
    assert(sol.hasCycle(head2) == false);

    ListNode* head3 = new ListNode(1);
    assert(sol.hasCycle(head3) == false);

    return 0;
}