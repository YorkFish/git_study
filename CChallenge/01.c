#include <stdio.h>

int singleNumber(int* nums, int numsSize) {
    int res = nums[0];
    for (int i = 1; i < numsSize; i++) {
        res ^= nums[i];
    }
    return res;
}

int main() {
    int nums[] = {2, 2, 1};
    int numsSize = 3;
    int result = singleNumber(nums, numsSize);
    printf("result = %d\n", result);

    return 0;
}
