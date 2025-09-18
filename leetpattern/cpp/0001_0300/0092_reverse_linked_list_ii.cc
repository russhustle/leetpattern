#include <cassert>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
   public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* p0 = &dummy;

        for (int i = 0; i < left - 1; ++i) {
            p0 = p0->next;
        }

        ListNode* pre = nullptr;
        ListNode* cur = p0->next;
        int count = right - left + 1;

        while (count--) {
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }

        p0->next->next = cur;
        p0->next = pre;

        return dummy.next;
    }
};

int main() {
    Solution solution;

    ListNode* head1 = new ListNode(
        1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
    int left1 = 2, right1 = 4;
    ListNode* result1 = solution.reverseBetween(head1, left1, right1);
    ListNode* expected1 = new ListNode(
        1, new ListNode(4, new ListNode(3, new ListNode(2, new ListNode(5)))));
    for (ListNode *p = result1, *q = expected1; p != nullptr && q != nullptr;
         p = p->next, q = q->next) {
        assert(p->val == q->val);
    }

    ListNode* head2 = new ListNode(5);
    int left2 = 1, right2 = 1;
    ListNode* result2 = solution.reverseBetween(head2, left2, right2);
    ListNode* expected2 = new ListNode(5);
    for (ListNode *p = result2, *q = expected2; p != nullptr && q != nullptr;
         p = p->next, q = q->next) {
        assert(p->val == q->val);
    }

    return 0;
}