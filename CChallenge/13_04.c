#include <stdio.h>

int cindex(int j) {
    return j + 1;
}

int findMaxJ(int target, int numsSize, int* cntDiff) {
    int maxJ = -1;
    for (int j = 0; j < numsSize; j++) {
        if (cntDiff[cindex(j)] == target) {
            maxJ = j;
        }
    }
    return maxJ;
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

    int maxLength = 0;
    for (int i = 0; i < numsSize; i++) {
        int target = cntDiff[cindex(i-1)];
        int length = findMaxJ(target, numsSize, cntDiff) - i + 1;
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
