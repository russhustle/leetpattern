#include <cassert>
#include <iostream>

#include "include/lists.hpp"
using namespace std;

class Solution {
   public:
    bool has_cycle(ListNode* head) {
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
    Solution solution;

    ListNode* head = LinkedList::build({3, 2, 0, -4});
    // create cycle
    head = LinkedList::make_cycle(head, 1);
    assert(solution.has_cycle(head) == true);
    // no cycle
    ListNode* head2 = LinkedList::build({1, 2});
    assert(solution.has_cycle(head2) == false);
    // no cycle
    ListNode* head3 = LinkedList::build({1});
    assert(solution.has_cycle(head3) == false);

    return 0;
}
