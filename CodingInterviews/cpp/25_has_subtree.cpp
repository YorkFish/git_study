#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    bool hasSubtree(TreeNode* pRoot1, TreeNode* pRoot2) {
        if (pRoot2 == NULL || pRoot1 == NULL) return false;
        if (isPart(pRoot1, pRoot2)) return true;
        return hasSubtree(pRoot1->left, pRoot2) || hasSubtree(pRoot1->right, pRoot2);
    }
    
    bool isPart(TreeNode* p1, TreeNode* p2) {
        if (p2 == NULL) return true;
        if (p1 == NULL || p2->val != p1->val) return false;
        return isPart(p1->left, p2->left) && isPart(p1->right, p2->right);
    }
};

int main() {
    TreeNode a1(1), a2(8), a3(7), a4(9), a5(2), a6(4), a7(7);
    TreeNode b1(8), b2(9), b3(2);
    a1.left = &a2, a1.right = &a3;
    a2.left = &a4, a2.right = &a5;
    a5.left = &a6, a5.right = &a7;
    b1.left = &b2, b1.right = &b3;

    Solution s;
    bool ans = s.hasSubtree(&a1, &b1);
    if (ans) cout << "true" << endl;
    else cout << "false" << endl;

    return 0;
}
