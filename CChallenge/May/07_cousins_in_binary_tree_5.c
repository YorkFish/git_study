#include <stdio.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct {
    int depth;
    int parent;
} Info;

Info getDepthAndParent(struct TreeNode* root, int target, int parent) {
    if (root == NULL) {
        return (Info) {-1, 0};
    }
    if (root->val == target) {
        return (Info) {0, parent};
    }

    Info left = getDepthAndParent(root->left, target, root->val);
    Info right = getDepthAndParent(root->right, target, root->val);
    if (left.parent != 0) {
        return (Info) {left.depth + 1, left.parent};
    }
    if (right.parent != 0) {
        return (Info) {right.depth + 1, right.parent};
    }
    return (Info) {-1, 0};
}

bool isCousins(struct TreeNode* root, int x, int y){
    Info xInfo = getDepthAndParent(root, x, 0);
    Info yInfo = getDepthAndParent(root, y, 0);
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
