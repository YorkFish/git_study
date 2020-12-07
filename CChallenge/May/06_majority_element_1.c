#include <stdio.h>

int majorityElement(int* nums, int numsSize){
    int halfNumsSize = numsSize / 2;
    for (int i = 0; i < numsSize; i ++ ) {
        int count = 0;
        for (int j = 0; j < numsSize; j ++ ) {
            if (nums[j] == nums[i]) {
                count ++ ;
            }
        }
        if (halfNumsSize < count) {
            return nums[i];
        }
    }
    return -1;
}

int main() {
    int nums1[] = {3, 2, 3};
    int nums2[] = {2, 2, 1, 1, 1, 2, 2};
    int ans1 = majorityElement(nums1, 3);
    int ans2 = majorityElement(nums2, 7);
    printf("ans1: %d\n", ans1);
    printf("ans2: %d\n", ans2);

    return 0;
}
