#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    void deleteNode(ListNode* node) {
        *node = *(node->next);
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
    ListNode n1(1), n2(4), n3(6), n4(8);    
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;

    Solution s;
    s.deleteNode(&n3);
    print_linked_list(&n1);

    return 0;
}
