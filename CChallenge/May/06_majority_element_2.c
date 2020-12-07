#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int majorityElement(int* nums, int numsSize){
    int halfNumsSize = numsSize / 2;
    while (true) {
        int i = rand() % numsSize;
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
