#include <stdio.h>
#include <stdlib.h>

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* result = malloc(sizeof(int) * numsSize);

    int lefts[numsSize];
    int rights[numsSize];
    lefts[0] = 1;
    rights[numsSize-1] = 1;
    for (int i = 1; i < numsSize; i++) {
        lefts[i] = lefts[i-1] * nums[i-1];
    }
    for (int i = numsSize-2; i >= 0; i--) {
        rights[i] = rights[i+1] * nums[i+1];
    }
    for (int i = 0; i < numsSize; i++) {
        result[i] = lefts[i] * rights[i];
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
