#include <stdio.h>

/** count(a, b) = count(0, b) - count(0, a-1) */
int count0(int j, int* nums) {
    int count = 0;
    for (int i = 0; i <= j; i++) {
        if (nums[i] == 0) {
            count++;
        }
    }
    return count;
}

int count1(int j, int* nums) {
    int count = 0;
    for (int i = 0; i <= j; i++) {
        if (nums[i] == 1) {
            count++;
        }
    }
    return count;
}

int findMaxLength(int* nums, int numsSize) {
    int maxLength = 0;
    for (int i = 0; i < numsSize-1; i++) {
        for (int j = i+1; j < numsSize; j++) {
            if (count0(j, nums) - count0(i-1, nums) == count1(j, nums) - count1(i-1, nums)) {
            // if (count0(j, nums) - count1(j, nums) == count0(i-1, nums) - count1(i-1, nums)) {
                int length = j - i + 1;
                if (maxLength < length) {
                    maxLength = length;
                }
            }
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
