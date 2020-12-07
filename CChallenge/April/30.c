#include <stdio.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool isValid(struct TreeNode* root, int* arr, int arrSize, int start) {
    // root:
    // arr:  [0, 1, 0, 1], arrSize: 4
    // start:          ^  <- 3
    if (root == NULL) return false;
    if (arrSize <= start) return false;

    // 不是
    // 1. 树根的值与子阵列的开头不同
    if (root->val != arr[start]) {
        return false;
    }

    // 是
    // 1. 下到一个树叶，且阵列刚好用完
    if (root->left == NULL && root->right == NULL) {
        return start + 1 == arrSize;
    }

    // 2. 走到的不是个树叶
    return isValid(root->left, arr, arrSize, start+1) || isValid(root->right, arr, arrSize, start+1);
}


// 题目说 root != NULL && arrSize >= 1
// 但还是要考虑到以下几种情形（root 可以是空的，arr 也可以是空的）
// root == NULL && arrSize == 0: return false
// root == NULL && arrSize != 0: return false
// root != NULL && arrSize == 0: return false
// root != NULL && arrSize != 0: return root->val == arr[0] && (isValid(root->left) || isValid(root->right))
bool isValidSequence(struct TreeNode* root, int* arr, int arrSize) {
    return isValid(root, arr, arrSize, 0);
}

int main() {
    /*     0
        /     \ 
       1       0
     /   \    /
    0     1  0
     \   / \
      1 0   0
    */
    struct TreeNode n1, n2, n3, n4, n5, n6, n7, n8, n9;
    n1.val = 0;
    n2.val = 1;
    n3.val = 0;
    n4.val = 0;
    n5.val = 1;
    n6.val = 0;
    n7.val = 1;
    n8.val = 0;
    n9.val = 0;
    n1.left = &n2;
    n1.right = &n3;
    n2.left = &n4;
    n2.right = &n5;
    n3.left = &n6;
    n3.right = NULL;
    n4.left = NULL;
    n4.right = &n7;
    n5.left = &n8;
    n5.right = &n9;
    n6.left = NULL;
    n6.right = NULL;
    n7.left = NULL;
    n7.right = NULL;
    n8.left = NULL;
    n8.right = NULL;
    n9.left = NULL;
    n9.right = NULL;

    int arr1[] = {0, 1, 0, 1};
    int arr2[] = {0, 0, 1};
    int arr3[] = {0, 1, 1};
    bool res1 = isValidSequence(&n1, arr1, 4);
    bool res2 = isValidSequence(&n1, arr2, 3);
    bool res3 = isValidSequence(&n1, arr3, 3);
    printf(">>> res1 = %d\n", res1);
    printf(">>> res2 = %d\n", res2);
    printf(">>> res3 = %d\n", res3);

    return 0;
}
