#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* deleteDuplication(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;

        ListNode* pre = dummy;
        while (pre->next) {
            ListNode* cur = pre->next;
            while (cur->next && cur->val == cur->next->val) cur = cur->next;
            if (pre->next == cur) pre = cur;
            else pre->next = cur->next;
        }
        return dummy->next;
    }
};

void print_linked_list(ListNode* root) {
    ListNode* cur = root;
    while (cur) {
        cout << cur->val << "->";
        cur = cur->next;
    }
    cout << "NULL" << endl;
}

int main() {
    ListNode n1(1), n2(1), n3(1), n4(2), n5(3);
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;

    Solution s;
    ListNode* newHead = s.deleteDuplication(&n1);
    print_linked_list(newHead);

    return 0;
}
