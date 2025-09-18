#ifndef LIST_UTILS_HPP
#define LIST_UTILS_HPP

#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class ListUtils {
   public:
    static ListNode* buildList(const vector<int>& values) {
        if (values.empty()) return nullptr;

        ListNode* head = new ListNode(values[0]);
        ListNode* current = head;

        for (size_t i = 1; i < values.size(); i++) {
            current->next = new ListNode(values[i]);
            current = current->next;
        }

        return head;
    }

    static vector<int> toVector(ListNode* head) {
        vector<int> result;
        while (head) {
            result.push_back(head->val);
            head = head->next;
        }
        return result;
    }

    static void printList(ListNode* head) {
        while (head) {
            cout << head->val;
            if (head->next) cout << " -> ";
            head = head->next;
        }
        cout << " -> nullptr" << endl;
    }

    static int length(ListNode* head) {
        int count = 0;
        while (head) {
            count++;
            head = head->next;
        }
        return count;
    }

    static ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* current = head;

        while (current) {
            ListNode* next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }

        return prev;
    }
};

#endif  // LIST_UTILS_HPP
