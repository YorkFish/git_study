#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    int treeDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        return max(treeDepth(root->left), treeDepth(root->right)) + 1;
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
    int ans = s.treeDepth(&n1);
    cout << ans << endl;

    return 0;
}
