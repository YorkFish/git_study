#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    bool res = true;
    bool isBalanced(TreeNode* root) {
        dfs(root);
        return res;
    }

    int dfs(TreeNode* root) {
        if (root == nullptr) return 0;
        int left = dfs(root->left), right = dfs(root->right);
        if (abs(left - right) > 1) res = false;
        return max(left, right) + 1;
    }
};

int main() {
    /*
      5
     / \
    7  11
       / \
      12  9
    */
    TreeNode n1(5), n2(7), n3(11), n4(12), n5(9);
    n1.left = &n2, n1.right = &n3;
    n3.left = &n4, n3.right = &n5;

    Solution s;
    bool ans = s.isBalanced(&n1);
    if (ans) cout << "is balanced" << endl;
    else cout << "is not balanced" << endl;

    return 0;
}
