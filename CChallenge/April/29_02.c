#include <stdio.h>
#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int max3(int a, int b, int c) {
    int max = a;
    if (max < b) max = b;
    if (max < c) max = c;
    return max;
}

// ----------

// 只能从 root 开始的最大路径和（可以不选，都不选为零）
int maxPathSumRoot(struct TreeNode* root) {
    if (root == NULL) return 0;

    return max3(
        maxPathSumRoot(root->left) + root->val,
        maxPathSumRoot(root->right) + root->val,
        0);
}

// 回传任意起点走到任意终点的最大路径和（不可以不选，至少选一个节点；空的话，回传 INT_MIN）
int maxPathSum(struct TreeNode* root) {
    if (root == NULL) return INT_MIN;

    return max3(
        maxPathSumRoot(root->left) + root->val + maxPathSumRoot(root->right),
        maxPathSum(root->left),
        maxPathSum(root->right));
}

int main() {
    /** -10
     *  /  \
     * 9   20
     *     / \
     *    15  7
     */
    struct TreeNode n1, n2, n3, n4, n5;
    n1.val = -10;
    n2.val = 9;
    n3.val = 20;
    n4.val = 15;
    n5.val = 7;
    n1.left = &n2;
    n1.right = &n3;
    n2.left = NULL;
    n2.right = NULL;
    n3.left = &n4;
    n3.right = &n5;
    n4.left = NULL;
    n4.right = NULL;
    n5.left = NULL;
    n5.right = NULL;

    int result = maxPathSum(&n1);
    printf(">>> result = %d\n", result);

    return 0;
}
