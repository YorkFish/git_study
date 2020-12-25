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
    ListNode* findKthToTail(ListNode* pListHead, int k) {
        ListNode* cur = pListHead;
        int size = 0;
        while (cur) {
            size ++ ;
            cur = cur->next;
        }
        if (size < k) return NULL;
        
        cur = pListHead;
        for (int i = 0; i < size - k; i ++ ) cur = cur->next;
        return cur;
    }
};

int main() {
    ListNode n1(1), n2(2), n3(3), n4(4), n5(5);
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;

    Solution s;
    ListNode* res = s.findKthToTail(&n1, 2);
    cout << res->val << endl;

    return 0;
}
