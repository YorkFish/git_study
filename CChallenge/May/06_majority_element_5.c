#include <stdio.h>

// [start, stop]
int rangedMajorityElement(int* nums, int start, int stop) {
    if (start == stop) return nums[start];
    int mid = start + (stop - start) / 2;
    int leftMajorityElement = rangedMajorityElement(nums, start, mid);
    int rightMajorityElement = rangedMajorityElement(nums, mid + 1, stop);
    if (leftMajorityElement == rightMajorityElement) return leftMajorityElement;
    int leftCount = 0, rightCount = 0;
    for (int i = start; i <= stop; i ++ ) {
        if (nums[i] == leftMajorityElement) {
            leftCount ++ ;
        }
        if (nums[i] == rightMajorityElement) {
            rightCount ++ ;
        }
    }
    return leftCount < rightCount ? rightMajorityElement : leftMajorityElement;
}

int majorityElement(int* nums, int numsSize){
    return rangedMajorityElement(nums, 0, numsSize - 1);
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
