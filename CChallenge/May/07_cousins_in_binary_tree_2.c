#include <stdio.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int getDepth(struct TreeNode* root, int target) {
    if (root == NULL) return -1;
    if (root->val == target) return 0;
    
    int leftDepth = getDepth(root->left, target);
    int rightDepth = getDepth(root->right, target);
    if (leftDepth != -1) return leftDepth + 1;
    if (rightDepth != -1) return rightDepth + 1;
    
    return -1;
}

int getParent(struct TreeNode* root, int target, int parent) {
    if (root == NULL) return 0;
    else if (root->val == target) return parent;

    int leftParent = getParent(root->left, target, root->val);
    int rightParent = getParent(root->right, target, root->val);
    if (leftParent != 0) return leftParent;
    if (rightParent != 0) return rightParent;

    return 0;
}

bool isCousins(struct TreeNode* root, int x, int y){
    int xDepth = getDepth(root, x);
    int yDepth = getDepth(root, y);
    int xParent = getParent(root, x, 0);
    int yParent = getParent(root, y, 0);
    return xDepth == yDepth && xParent != yParent;
}

int main() {
    /*
       1
      / \
     2   3
      \   \
       4   5
    */
    struct TreeNode n1, n2, n3, n4, n5;
    n1.val = 1; n2.val = 2; n3.val = 3; n4.val = 4; n5.val = 5;
    n1.left = &n2; n1.right = &n3;
    n2.left = NULL; n2.right = &n4;
    n3.left = NULL; n3.right = &n5;
    n4.left = NULL; n4.right = NULL;
    n5.left = NULL; n5.right = NULL;
    bool ans = isCousins(&n1, 4, 5);
    if (ans) printf("is cousins\n");
    else printf("is not cousins\n");

    return 0;
}
