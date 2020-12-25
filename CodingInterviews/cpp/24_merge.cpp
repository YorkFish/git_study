#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode(-1), *cur = dummy;
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                cur = cur->next = l1;
                l1 = l1->next;
            }
            else {
                cur = cur->next = l2;
                l2 = l2->next;
            }
        }
        if (l1) cur->next = l1;
        else cur->next = l2;
        return dummy->next;
    }  
};

int main() {
    ListNode a1(1), a2(3), a3(5), b1(2), b2(4), b3(5);
    a1.next = &a2; a2.next = &a3;
    b1.next = &b2; b2.next = &b3;

    Solution s;
    ListNode* ans = s.merge(&a1, &b1);
    if (ans) print_linked_list(ans);
    else cout << "NULL" << endl;

    return 0;
}
