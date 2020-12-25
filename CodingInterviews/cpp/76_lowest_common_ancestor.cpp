#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) return nullptr;
        if (root == p || root == q) return root;
        auto left = lowestCommonAncestor(root->left, p, q);
        auto right = lowestCommonAncestor(root->right, p, q);
        if (left && right) return root;
        if (left) return left;
        return right;
    }
};

int main() {
    /*
      8
     / \
    12  2
       / \
      6   4
    */
    TreeNode n1(8), n2(12), n3(2), n4(6), n5(4);
    n1.left = &n2, n1.right = &n3;
    n3.left = &n4, n3.right = &n5;

    Solution s;
    auto ans = s.lowestCommonAncestor(&n1, &n3, &n4);
    cout << ans->val << endl;

    return 0;
}
