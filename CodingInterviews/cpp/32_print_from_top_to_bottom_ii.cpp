#include <iostream>
#include <vector>
#include <queue>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<vector<int>> printFromTopToBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (root == nullptr) return res;

        queue<TreeNode*> q;
        q.push(root);
        q.push(nullptr);
        vector<int> level;
        while (q.size()) {
            TreeNode* node = q.front();
            q.pop();
            if (node == nullptr) {
                if (level.empty()) break;  // bottom 没有下一层
                res.push_back(level);
                level.clear();
                q.push(nullptr);
                continue;
            }
            level.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return res;
    }
};

int main() {
    /*
        8
       / \
      12  2
         /
        6
       /
      4
    */
    TreeNode n1(8), n2(12), n3(2), n4(6), n5(4);
    n1.left = &n2, n1.right = &n3;
    n3.left = &n4;
    n4.left = &n5;

    Solution s;
    vector<vector<int>> ans = s.printFromTopToBottom(&n1);
    print_matrix(ans);

    return 0;
}
