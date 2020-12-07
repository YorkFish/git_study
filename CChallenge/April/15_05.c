#include <stdio.h>
#include <stdlib.h>

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* result = malloc(sizeof(int) * numsSize);
    result[numsSize-1] = 1;
    for (int i = numsSize-2; i >= 0; i--) {
        result[i] = result[i+1] * nums[i+1];
    }
    int left = 1;
    for (int i = 0; i < numsSize; i++) {
        result[i] = left * result[i];
        left *= nums[i];
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
