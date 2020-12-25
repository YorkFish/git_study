#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:
    TreeNode* convert(TreeNode* root) {
        if (root == nullptr) return root;
        pair<TreeNode*, TreeNode*> side = dfs(root);
        return side.first;
    }
    
    pair<TreeNode*, TreeNode*> dfs(TreeNode* root) {
        if (root->left == nullptr && root->right == nullptr) return {root, root};
        
        if (root->left && root->right) {
            auto lside = dfs(root->left), rside = dfs(root->right);
            lside.second->right = root, root->left = lside.second;
            root->right = rside.first, rside.first->left = root;
            return {lside.first, rside.second};
        }
        else if (root->left) {
            auto lside = dfs(root->left);
            lside.second->right = root, root->left = lside.second;
            return {lside.first, root};
        }
        else {
            auto rside = dfs(root->right);
            root->right = rside.first, rside.first->left = root;
            return {root, rside.second};
        }
    }
};

int main() {
    /*
        10
       /  \
      6    14    4 <=> 6 <=> 8 <=> 10 <=> 12 <=> 14 <=> 16
     / \   / \
    4   8 12 16
    */
    TreeNode n1(10), n2(6), n3(14), n4(4), n5(8), n6(12), n7(16);
    n1.left = &n2, n1.right = &n3;
    n2.left = &n4, n2.right = &n5;
    n3.left = &n6, n3.right = &n7;

    Solution s;
    TreeNode* ans = s.convert(&n1);

    TreeNode* node = ans;
    while (node) {
        cout << node->val << ' ';
        if (node->right == nullptr) break;
        node = node->right;
    }
    cout << endl;
    while (node) {
        cout << node->val << ' ';
        node = node->left;
    }
    cout << endl;

    return 0;
}
