#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *entryNodeOfLoop(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while (fast) {
            slow = slow->next;
            fast = fast->next;
            if (fast) fast = fast->next;
            else return NULL;
            if (fast == slow) {
                fast = head;
                while (fast != slow) {
                    slow = slow->next;
                    fast = fast->next;
                }
                return fast;
            }
        }
        return NULL;
    }
};

int main() {
    ListNode n1(1), n2(2), n3(3), n4(4), n5(5), n6(6);
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;
    n5.next = &n6;
    n6.next = &n3;

    Solution s;
    ListNode* res = s.entryNodeOfLoop(&n1);
    if (res != NULL) cout << res->val << endl;
    else cout << "NULL" << endl;

    return 0;
}
