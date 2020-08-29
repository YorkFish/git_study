#include <stdio.h>

int maxSubArray(int* nums, int numsSize) {
    int max = nums[0], sum = nums[0];
    for (int i = 1; i < numsSize; i++) {
        sum += nums[i];
        if (sum < nums[i]) sum = nums[i];
        if (max < sum) max = sum;
    }
    return max;
}

int main() {
    int arr1[9] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int arr2[1] = {-1};
    int arr3[2] = {-2, 1};
    printf(">>> maxSubArray(arr1) = %d\n", maxSubArray(arr1, 9));
    printf(">>> maxSubArray(arr2) = %d\n", maxSubArray(arr2, 1));
    printf(">>> maxSubArray(arr3) = %d\n", maxSubArray(arr3, 2));

    return 0;
}