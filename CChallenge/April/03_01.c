#include <stdio.h>

int maxSubArray(int* nums, int numsSize) {
    int max = nums[0];
    for (int i = 0; i < numsSize; i++) {
        int sum = 0;
        for (int j = i; j < numsSize; j++) {
            sum += nums[j];
            if (max < sum) {
                max = sum;
            }
        }
    }
    return max;
}

int main() {
    int arr1[9] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int arr2[1] = {-1};
    printf(">>> maxSubArray(arr1) = %d\n", maxSubArray(arr1, 9));
    printf(">>> maxSubArray(arr2) = %d\n", maxSubArray(arr2, 1));

    return 0;
}
