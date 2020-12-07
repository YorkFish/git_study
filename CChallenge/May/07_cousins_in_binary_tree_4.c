#include <stdio.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct Info {
    int depth;
    int parent;
};

void getDepthAndParent(struct TreeNode* root, int target, int parent, struct Info* info) {
    if (root == NULL) {
        info->depth = -1;
        info->parent = 0;
        return;
    }
    if (root->val == target) {
        info->depth = 0;
        info->parent = parent;
        return;
    }

    struct Info left, right;
    getDepthAndParent(root->left, target, root->val, &left);
    getDepthAndParent(root->right, target, root->val, &right);
    if (left.parent != 0) {
        info->depth = left.depth + 1;
        info->parent = left.parent;
        return;
    }
    if (right.parent != 0) {
        info->depth = right.depth + 1;
        info->parent = right.parent;
        return;
    }
    info->depth = -1;
    info->parent = 0;
    return;
}

bool isCousins(struct TreeNode* root, int x, int y){
    struct Info xInfo, yInfo;
    getDepthAndParent(root, x, 0, &xInfo);
    getDepthAndParent(root, y, 0, &yInfo);

    return xInfo.depth == yInfo.depth && xInfo.parent != yInfo.parent;
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
