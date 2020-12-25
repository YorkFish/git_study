#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    ListNode *findFirstCommonNode(ListNode *headA, ListNode *headB) {        
        ListNode *cur_a = headA, *cur_b = headB;
        while (cur_a != cur_b) {
            if (cur_a) cur_a = cur_a->next;
            else cur_a = headB;
            if (cur_b) cur_b = cur_b->next;
            else cur_b = headA;
        }
        return cur_a;
    }
};

int main() {
    /*
    1 -> 2 -> 3
               \
                4 -> 5 -> NULL
               /
         6 -> 7
    */
    ListNode n1(1), n2(2), n3(3), n4(4), n5(5), n6(6), n7(7);
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;
    n6.next = &n7;
    n7.next = &n4;

    Solution s;
    ListNode* ans = s.findFirstCommonNode(&n1, &n6);
    if (ans) cout << ans->val << endl;
    else cout << "NULL" << endl;

    return 0;
}
