#include <stdio.h>

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

// 树的高度
int maxDepth(struct TreeNode* root) {
    if (root == NULL) return 0;
    int leftMax = maxDepth(root->left);
    int rightMax = maxDepth(root->right);
    int res = (leftMax < rightMax ? rightMax : leftMax) + 1;
    return res;
}

int diameterOfBinaryTree(struct TreeNode* root) {
    if (root == NULL) return 0;
    // 1. 最长的路径会通过 root
    //   起点在左边，终点在右边
    int middle = maxDepth(root->left) + maxDepth(root->right);

    // 2. 最长的路径没有通过 root
    //   要么都在左边
    int left = diameterOfBinaryTree(root->left);
    //   要么都在右边
    int right = diameterOfBinaryTree(root->right);

    int res = left < middle ? middle : left;
    res = res < right ? right : res;
    return res;
}

int main() {
    /*
        1
       / \
      2   3
     / \
    4   5
    */
    struct TreeNode n1, n2, n3, n4, n5;
    n1.val = 1;
    n2.val = 2;
    n3.val = 3;
    n4.val = 4;
    n5.val = 5;
    n1.left = &n2;
    n1.right = &n3;
    n2.left = &n4;
    n2.right = &n5;
    n3.left = NULL;
    n3.right = NULL;
    n4.left = NULL;
    n4.right = NULL;
    n5.left = NULL;
    n5.right = NULL;

    int result = diameterOfBinaryTree(&n1);
    printf(">>> result = %d\n", result);

    return 0;
}
