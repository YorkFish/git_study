#include <stdio.h>
#include <stdlib.h>

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* result = malloc(sizeof(int) * numsSize);

    for (int i = 0; i < numsSize; i++) {
        int left = 1;
        for (int j = 0; j < i; j++) {
            left *= nums[j];
        }
        int right = 1;
        for (int j = i+1; j < numsSize; j++) {
            right *= nums[j];
        }
        result[i] = left * right;
    }
    return result;
}

int main() {
    int nums[] = {1, 2, 3, 4};
    int numsSize = 4;
    int returnSize = 0;
    int* result = productExceptSelf(nums, numsSize, &returnSize);
    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    free(result);

    return 0;
}
