#include <stdio.h>

int majorityElement(int* nums, int numsSize){
    int num = 0, count = 0;
    for (int i = 0; i < numsSize; i ++ ) {
        if (count == 0) {
            num = nums[i];
            count = 1;
        }
        else if (nums[i] == num) {
            count ++ ;
        }
        else {
            count -- ;
        }
    }
    return num;
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
