#include <iostream>
#include "helper.h"

using namespace std;

class Solution {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string res;
        if (root == nullptr) return res;
        dfs_s(root, res);
        return res;
    }

    void dfs_s(TreeNode* root, string &res) {
        if (root == nullptr) {
            res += "null ";
            return;
        }
        res += to_string(root->val) + ' ';
        dfs_s(root->left, res);
        dfs_s(root->right, res);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int u = 0;  // 遍历标记
        return dfs_d(data, u);
    }

    TreeNode* dfs_d(string &data, int &u) {
        if (u == data.size()) return nullptr;
        int k = u;
        while (data[k] != ' ') k ++ ;
        if (data[u] == 'n') {
            u = k + 1;
            return nullptr;
        }
        bool is_negative = false;
        if (data[u] == '-') {
            is_negative = true;
            u ++ ;
        }
        int val = 0;
        for (int i = u; i < k; i ++ ) val = val * 10 + data[i] - '0';
        if (is_negative) val *= -1;
        u = k + 1;
        TreeNode* root = new TreeNode(val);
        root->left = dfs_d(data, u);
        root->right = dfs_d(data, u);
        return root;
    }
};

int main() {
    /*
       -10
       / \
      13  -1
         /
        6
       /
      2
    */
    TreeNode n1(-10), n2(13), n3(-1), n4(6), n5(2);
    n1.left = &n2, n1.right = &n3;
    n3.left = &n4;
    n4.left = &n5;

    Solution s;
    string data = s.serialize(&n1);
    cout << data << endl;
    TreeNode* root = s.deserialize(data);
    print_tree(root);

    return 0;
}
