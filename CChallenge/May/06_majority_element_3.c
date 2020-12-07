#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int majorityElement(int* nums, int numsSize){
    qsort(nums, numsSize, sizeof(int), cmp);
    return nums[numsSize / 2];
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
