#include <stdio.h>
#include <stdbool.h>

bool canJamp(int* nums, int numsSize) {
    // 凑 numsSize-1
    // nums:     [2, 3, 1, 1, 4], numsSize = 5
    // canReach: [T, F, F, F, F] => [T, T, T, T, (T)]
    bool canReach[numsSize];
    canReach[0] = true;
    for (int i = 1; i < numsSize; i++) {
        canReach[i] = false;
    }
    
    for (int i = 0; i < numsSize; i++) {
        if (canReach[i]) {
            for (int j = 1; j <= nums[i]; j++) {
                int k = i + j;
                if (k < numsSize) {
                    canReach[k] = true;
                }
            }
        }
    }

    return canReach[numsSize-1];
}

int main() {
    int nums1[5] = {2, 3, 1, 1, 4};
    int nums2[5] = {3, 2, 1, 0, 4};
    bool result1 = canJamp(nums1, 5);
    bool result2 = canJamp(nums2, 5);
    
    printf(">>> result1 = %d\n", result1);
    printf(">>> result2 = %d\n", result2);

    return 0;
}
