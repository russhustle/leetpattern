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
    ListNode* detectCycle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (fast == slow) {
                slow = head;
                while (slow != fast) {
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }
        return nullptr;
    }
};

int main() {
    Solution sol;

    ListNode* head = new ListNode(3);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(-4);
    head->next->next->next->next = head->next;  // Create a cycle
    assert(sol.detectCycle(head) == head->next);

    ListNode* head2 = new ListNode(1);
    head2->next = new ListNode(2);
    head2->next->next = head2;  // Create a cycle
    assert(sol.detectCycle(head2) == head2);

    ListNode* head3 = new ListNode(1);
    assert(sol.detectCycle(head3) == nullptr);

    ListNode* head4 = nullptr;
    assert(sol.detectCycle(head4) == nullptr);

    return 0;
}
