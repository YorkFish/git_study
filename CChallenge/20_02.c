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

int pos;

struct TreeNode* bstFromPreorderRanged(int* preorder, int start, int end, int max) {
    if (start == end) return NULL;
    if (max < preorder[start]) return NULL;

    struct TreeNode* root = malloc(sizeof(struct TreeNode));
    root->val = preorder[start];
    pos++;
    root->left = bstFromPreorderRanged(preorder, start+1, end, root->val);
    root->right = bstFromPreorderRanged(preorder, pos, end, max);

    return root;
}

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize) {
    pos = 0;
    return bstFromPreorderRanged(preorder, 0, preorderSize, INT_MAX);
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
