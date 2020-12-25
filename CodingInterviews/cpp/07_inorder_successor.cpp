#include <iostream>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode *father;
    TreeNode(int x) : val(x), left(NULL), right(NULL), father(NULL) {}
};

class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* p) {
        if (p->right) {
            p = p->right;
            while (p->left) p = p->left;
            return p;
        }

        while (p->father && p == p->father->right) p = p->father;
        return p->father;
    }
};

int main() {
    TreeNode n1(1), n2(2), n3(3);
    n2.left = &n1;
    n2.right = &n3;
    n1.father = &n2;
    n3.father = &n2;
    Solution s;
    TreeNode* ans = s.inorderSuccessor(&n3);
    if (ans) cout << ans->val << endl;
    else cout << "null" << endl;
    
    return 0;
}
