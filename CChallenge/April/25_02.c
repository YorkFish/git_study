#include <stdio.h>

bool canJamp(int* nums, int numsSize) {
    int maxCanReach = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i <= maxCanReach) {
            int canReach = i + nums[i];
            if (maxCanReach < canReach) {
                maxCanReach = canReach;
            }
        }
    }
    return numsSize-1 <= maxCanReach;
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
