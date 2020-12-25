#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {        
        ListNode* pre = NULL;
        ListNode* cur = head;
        while (cur) {
            ListNode* nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
};

int main() {
    ListNode n1(1), n2(2), n3(3), n4(4), n5(5);
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;

    Solution s;
    ListNode* ans = s.reverseList(&n1);
    if (ans) print_linked_list(ans);
    else cout << "NULL" << endl;

    return 0;
}
