#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    map<int, int> hash;
    vector<int> preorder, inorder;

    TreeNode* buildTree(vector<int>& _preorder, vector<int>& _inorder) {
        preorder = _preorder, inorder = _inorder;
        for (int i = 0; i < inorder.size(); i ++ ) hash[inorder[i]] = i;
        return dfs(0, preorder.size() - 1, 0, inorder.size() - 1);
    }

    // [pl, pr], [il, ir]
    TreeNode* dfs(int pl, int pr, int il, int ir) {
        if (pr < pl) return nullptr;
        TreeNode* root = new TreeNode(preorder[pl]);
        int rootIdx = hash[root->val];
        root->left = dfs(pl + 1, pl + rootIdx - il, il, rootIdx - 1);
        root->right = dfs(pl + rootIdx - il + 1, pr, rootIdx + 1, ir);
        return root;
    }
};

void print_tree(TreeNode* root) {
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* tmp = q.front();
        q.pop();
        if (tmp == nullptr) {
            cout << "null ";
        }
        else {
            cout << tmp->val << ' ';
            q.push(tmp->left);
            q.push(tmp->right);
        }
    }
    cout << endl;

}

int main() {
    vector<int> preorder{3, 9, 20, 15, 7};
    vector<int> inorder{9, 3, 15, 20, 7};
    Solution s;
    TreeNode* ans = s.buildTree(preorder, inorder);
    print_tree(ans);
    
    return 0;
}
