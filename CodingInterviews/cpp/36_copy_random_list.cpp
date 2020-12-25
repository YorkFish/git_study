#include <iostream>

using namespace std;

// Definition for singly-linked list with a random pointer
struct ListNode {
    int val;
    ListNode *next, *random;
    ListNode(int x) : val(x), next(NULL), random(NULL) {}
};

class Solution {
public:
    ListNode *copyRandomList(ListNode *head) {
        for (ListNode* p = head; p; p = p->next->next) {
            ListNode* np = new ListNode(p->val);
            np->next = p->next;
            p->next = np;
        }
        for (ListNode* p = head; p; p = p->next->next)
            if (p->random)
                p->next->random = p->random->next;
        
        ListNode* dummy = new ListNode(-1);
        ListNode* cur = dummy;
        for (ListNode* p = head; p; p = p->next) {
            cur->next = p->next;
            cur = cur->next;
            p->next = cur->next;
        }
        return dummy->next;
    }
};

int main() {
    /*
        ------------
       |  -------   ^
       v ^       v  |
    1-> 2 -> 3 ->4->5->NULL
    v_______^ v_____^
    */
    ListNode n1(1), n2(2), n3(3), n4(4), n5(5);
    n1.next = &n2, n1.random = &n3;
    n2.next = &n3, n2.random = &n4;
    n3.next = &n4, n3.random = &n5;
    n4.next = &n5; n5.random = &n2;

    Solution s;
    ListNode* ans = s.copyRandomList(&n1);
    ListNode* np1 = ans;
    ListNode* np2 = np1->next;
    ListNode* np3 = np2->next;
    ListNode* np4 = np3->next;
    ListNode* np5 = np4->next;
    cout << (np1->random->val == np3->val) << endl;
    cout << (np2->random->val == np4->val) << endl;
    cout << (np3->random->val == np5->val) << endl;
    cout << (np4->random == nullptr) << endl;
    cout << (np5->random->val == np2->val) << endl;

    return 0;
}
