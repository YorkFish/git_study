#include <stdio.h>

/**
 * countDiff == count0 - count1
 * 索引号 => [0, j] 0、1 出现的次数相差多少
 */
int countDiff(int j, int* nums) {
    int diff = 0;
    for (int i = 0; i <= j; i++) {
        if (nums[i] == 0) {
            diff++;
        }
        if (nums[i] == 1) {
            diff--;
        }
    }
    return diff;
}

/**
 * [0, 1] 出现的次数相差 j 次 => 差 j 次的最大索引号是谁
 */
int findMaxJ(int target, int* nums, int numsSize) {
    int maxJ = -1;
    for (int j = 0; j < numsSize; j++) {
        if (countDiff(j, nums) == target) {
            maxJ = j;
        }
    }
    return maxJ;
}

int findMaxLength(int* nums, int numsSize) {
    int maxLength = 0;
    for (int i = 0; i < numsSize; i++) {
        int target = countDiff(i-1, nums);
        int length = findMaxJ(target, nums, numsSize) - i + 1;
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
