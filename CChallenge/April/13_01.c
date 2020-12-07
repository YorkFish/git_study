#include <stdio.h>

int findMaxLength(int* nums, int numsSize) {
    int maxLength = 0;
    for (int i = 0; i < numsSize-1; i++) {
        for (int j = i+1; j < numsSize; j++) {
            int count0 = 0;
            int count1 = 0;
            for (int k = i; k <= j; k++) {
                if (nums[k] == 0) {
                    count0++;
                }
                else {
                    count1++;
                }
            }
            if (count0 == count1) {
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
