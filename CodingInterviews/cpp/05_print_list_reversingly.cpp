#include <iostream>
#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
} ;

class Solution {
public:
    vector<int> printListReversingly(ListNode* head) {
        vector<int> res;
        for (ListNode* cur = head; cur; cur = cur->next) res.push_back(cur->val);
        return vector<int>(res.rbegin(), res.rend());
    }
};

int main() {
    ListNode n1(2), n2(3), n3(5);
    n1.next = &n2;
    n2.next = &n3;
    Solution s;
    vector<int> ans = s.printListReversingly(&n1);
    for (int n : ans) cout << n << ' ';
    cout << endl;
    
    return 0;
}
