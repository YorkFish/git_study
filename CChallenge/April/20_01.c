#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void preorderTraverse(struct TreeNode* node) {
    if (node == NULL) return;

    printf("%d\n", node->val);
    preorderTraverse(node->left);
    preorderTraverse(node->right);
}

void queueTraverse(struct TreeNode* node) {
    if (node == NULL) return;

    struct TreeNode* nodes[100];
    int start = 0, stop = 0;
    nodes[0] = node;
    stop++;
    while (start < stop) {
        node = nodes[start++];
        if (node == NULL) {
            printf("NULL ");
        }
        else {
            printf("%d ", node->val);
            if (node->left || node->right) {
                nodes[stop++] = node->left;
                nodes[stop++] = node->right;
            }
        }
    }
    printf("\n");
}

// --------

struct TreeNode* bstFromPreorderRanged(int* preorder, int start, int end) {
    if (start == end) return NULL;

    struct TreeNode* root = malloc(sizeof(struct TreeNode));
    root->val = preorder[start];
    int i = start + 1;
    while (i < end && preorder[i] < root->val) {
        i++;
    }
    root->left = bstFromPreorderRanged(preorder, start+1, i);
    root->right = bstFromPreorderRanged(preorder, i, end);

    return root;
}

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize) {
    // [0, preorderSize)
    return bstFromPreorderRanged(preorder, 0, preorderSize);
}

int main() {
    /*
        8
       / \
      5  10
     / \   \
    1  7   12
    */
    int arr[] = {8, 5, 1, 7, 10, 12};

    struct TreeNode* root = bstFromPreorder(arr, 6);
    preorderTraverse(root);
    queueTraverse(root);

    return 0;
}
