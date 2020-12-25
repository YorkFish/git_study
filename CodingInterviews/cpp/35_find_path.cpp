#include <iostream>
#include <vector>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<vector<int>> all_paths;
    vector<int> path;

    vector<vector<int>> findPath(TreeNode* root, int sum) {
        dfs(root, sum);
        return all_paths;
    }

    void dfs(TreeNode* root, int sum) {
        if (root == nullptr) return;
        path.push_back(root->val);
        sum -= root->val;
        if (root->left == nullptr && root->right == nullptr && sum == 0)
            all_paths.push_back(path);
        dfs(root->left, sum);
        dfs(root->right, sum);
        path.pop_back();
    }
};

int main() {
    /*
          5
         / \
        4   6
       /   / \
      12  13  6
     /  \    / \
    9    1  5   1
    */
    TreeNode n1(5), n2(4), n3(6), n4(12), n5(13), n6(6), n7(9), n8(1), n9(5), n10(1);
    n1.left = &n2, n1.right = &n3;
    n2.left = &n4;
    n3.left = &n5, n3.right = &n6;
    n4.left = &n7, n4.right = &n8;
    n6.left = &n9, n6.right = &n10;
    int sum = 22;

    Solution s;
    vector<vector<int>> ans = s.findPath(&n1, sum);
    print_matrix(ans);

    return 0;
}
