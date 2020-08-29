a#include <stdio.h>
#include <stdlib.h>

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    // 1. 没有 0
    // 2. 有一个 0
    // 3. 有两个 0
    *returnSize = numsSize;
    int* result = malloc(sizeof(int) * numsSize);

    int numberOfZeros = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            numberOfZeros++;
        }
    }

    if (numberOfZeros == 1) {
        int total = 1;
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] != 0) {
                total *= nums[i];
            }
        }
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] != 0) {
                result[i] = 0;
            }
            else {
                result[i] = total;
            }
        }
    }
    else if (numberOfZeros >= 2) {
        for (int i = 0; i < numsSize; i++) {
            result[i] = 0;
        }
    }
    else {
        int total = 1;
        for (int i = 0; i < numsSize; i++) {
            total *= nums[i];
        }
        for (int i = 0; i < numsSize; i++) {
            result[i] = total / nums[i];
        }
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
