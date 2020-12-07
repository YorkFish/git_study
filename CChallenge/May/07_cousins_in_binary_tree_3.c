#include <stdio.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void getDepthAndParent(struct TreeNode* root, int target, int parent, int* returnDepth, int* returnParent) {
    if (root == NULL) {
        *returnDepth = -1;
        *returnParent = 0;
        return;
    }
    if (root->val == target) {
        *returnDepth = 0;
        *returnParent = parent;
        return;
    }

    int leftDepth, rightDepth, leftParent, rightParent;
    getDepthAndParent(root->left, target, root->val, &leftDepth, &leftParent);
    getDepthAndParent(root->right, target, root->val, &rightDepth, &rightParent);
    if (leftParent != 0) {
        *returnDepth = leftDepth + 1;
        *returnParent = leftParent;
        return;
    }
    if (rightParent != 0) {
        *returnDepth = rightDepth + 1;
        *returnParent = rightParent;
        return;
    }
    *returnDepth = -1;
    *returnParent = 0;
    return;
}

bool isCousins(struct TreeNode* root, int x, int y){
    int xDepth, yDepth, xParent, yParent;
    getDepthAndParent(root, x, 0, &xDepth, &xParent);
    getDepthAndParent(root, y, 0, &yDepth, &yParent);

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
