#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

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

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize) {
    struct TreeNode* root = malloc(sizeof(struct TreeNode));
    root->val = preorder[0];
    root->left = root->right = NULL;

    struct TreeNode* path[100];
    int topIndex = 0;
    path[topIndex] = root;

    for (int i = 1; i < preorderSize; i++) {
        struct TreeNode* node = malloc(sizeof(struct TreeNode));
        node->val = preorder[i];
        node->left = node->right = NULL;

        if (preorder[i] < path[topIndex]->val) {
            path[topIndex]->left = node;
            topIndex++;
            path[topIndex] = node;
        }
        else {
            while (topIndex-1 >= 0 && path[topIndex-1]->val < preorder[i]) {
                topIndex--;
            }
            if (topIndex-1 >= 0) {
                path[topIndex]->right = node;
                path[topIndex] = node;
            }
            else {
                path[0]->right = node;
                path[0] = node;
            }
        }
    }
    return root;
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
    queueTraverse(root);

    return 0;
}
