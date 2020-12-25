#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;  // 空结点视为对称的树
        return dfs(root->left, root->right);
    }

    bool dfs(TreeNode* left, TreeNode* right) {
        if (left == NULL || right == NULL) return left == right;
        if (left->val != right->val) return false;
        return dfs(left->left, right->right) && dfs(left->right, right->left);
    }
};

int main() {
    /*
         1
       /   \
      2     2
     / \   / \
    3   4 4   3
    */
    TreeNode t1(1), t2(2), t3(2), t4(3), t5(4), t6(4), t7(3);
    t1.left = &t2, t1.right = &t3;
    t2.left = &t4, t2.right = &t5;
    t3.left = &t6, t3.right = &t7;

    Solution s;
    if (s.isSymmetric(&t1)) cout << "true" << endl;
    else cout << "false" << endl;

    return 0;
}
