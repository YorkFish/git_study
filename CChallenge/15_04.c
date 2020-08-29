#include <stdio.h>
#include <stdlib.h>

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* result = malloc(sizeof(int) * numsSize);

    int rights[numsSize];
    rights[numsSize-1] = 1;
    for (int i = numsSize-2; i >= 0; i--) {
        rights[i] = rights[i+1] * nums[i+1];
    }
    int left = 1;
    for (int i = 0; i < numsSize; i++) {
        result[i] = left * rights[i];
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
