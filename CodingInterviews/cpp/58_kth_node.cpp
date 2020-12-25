#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    TreeNode* res;
    TreeNode* kthNode(TreeNode* root, int k) {
        dfs(root, k);
        return res;
    }
    
    void dfs(TreeNode* root, int& k) {
        if (root == nullptr) return;
        dfs(root->left, k);
        k -- ;
        if (k == 0) res = root;
        if (k > 0) dfs(root->right, k);
    }
};

int main() {
    TreeNode n1(2), n2(1), n3(3);
    n1.left = &n2, n1.right = &n3;
    int k = 3;

    Solution s;
    TreeNode* ans = s.kthNode(&n1, k);
    if (ans) cout << ans->val << endl;
    else cout << "NULL" << endl;

    return 0;
}
