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

class LinkedList {
   public:
    static ListNode* build(const vector<int>& values) {
        if (values.empty()) return nullptr;

        ListNode* head = new ListNode(values[0]);
        ListNode* current = head;

        for (size_t i = 1; i < values.size(); i++) {
            current->next = new ListNode(values[i]);
            current = current->next;
        }

        return head;
    }

    static vector<int> to_array(ListNode* head) {
        vector<int> array;
        while (head) {
            array.push_back(head->val);
            head = head->next;
        }
        return array;
    }

    static void print_list(ListNode* head) {
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

    static ListNode* make_cycle(ListNode* head, int pos) {
        if (pos < 0) return head;

        ListNode* tail = head;
        ListNode* cycle_node = nullptr;
        int index = 0;

        while (tail && tail->next) {
            if (index == pos) cycle_node = tail;
            tail = tail->next;
            index++;
        }

        if (tail && index == pos) cycle_node = tail;

        if (tail) tail->next = cycle_node;

        return head;
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
