#include <stdio.h>

int cindex(int j) {
    return j + 1;
}

int findex(int j, int numsSize) {
    return j + numsSize;
}

int findMaxLength(int* nums, int numsSize) {
    int cntDiffSize = numsSize + 1;
    int cntDiff[cntDiffSize];
    cntDiff[cindex(-1)] = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            cntDiff[cindex(i)] = cntDiff[cindex(i-1)] + 1;
        }
        else {
            cntDiff[cindex(i)] = cntDiff[cindex(i-1)] - 1;
        }
    }

    int findMaxJSize = 2 * numsSize + 1;
    int findMaxJ[findMaxJSize];
    for (int i = -numsSize; i<=numsSize; i++) {
        findMaxJ[findex(i, numsSize)] = -1;
    }
    for (int j = 0; j < numsSize; j++) {
        findMaxJ[findex(cntDiff[cindex(j)], numsSize)] = j;
    }
    int maxLength = 0;
    for (int i = 0; i < numsSize; i++) {
        int target = cntDiff[cindex(i-1)];
        int length = findMaxJ[findex(target, numsSize)] - i + 1;
        if (maxLength < length) {
            maxLength = length;
        }
    }
    return maxLength;
}

int main() {
    int nums[] = {1, 1, 0, 0, 1, 1, 1, 0, 1, 0};
    int numsSize = 10;
    int result = findMaxLength(nums, numsSize);
    printf(">>> result = %d\n", result);

    return 0;
}
