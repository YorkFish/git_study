#include <iostream>
#include <algorithm>
#include "helper.h"

using namespace std;

class Solution {
public:
    void mirror(TreeNode* root) {
        if (root == NULL) return;
        mirror(root->left);
        mirror(root->right);
        swap(root->left, root->right);
    }
};

int main() {
    /*
         8
       /   \
      6     10
     / \   / \
    5   7 9   11
    */
    TreeNode t1(8), t2(6), t3(10), t4(5), t5(7), t6(9), t7(11);
    t1.left = &t2, t1.right = &t3;
    t2.left = &t4, t2.right = &t5;
    t3.left = &t6, t3.right = &t7;

    Solution s;
    s.mirror(&t1);
    print_tree(&t1);

    return 0;
}
