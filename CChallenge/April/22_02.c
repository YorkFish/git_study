#include <stdio.h>

int subarraySum(int* nums, int numsSize, int k) {
    // sum(x): nums[0] + nums[1] + ... + nums[x-1]
    int sum[numsSize+1];
    sum[0] = 0;
    for (int x = 1; x <= numsSize; x++) {
        sum[x] = sum[x-1] + nums[x-1];
    }

    // 0 <= i <= j < numsSize
    int count = 0;
    for (int j = 0; j < numsSize; j++) {
        int target = sum[j+1] - k;  // sum(j+1) - sum(i) == k => sum(i) = sum(j+1) - k
        for (int i = 0; i <= j; i++) {
            if (sum[i] == target) {
                count++;
            } 
        }
    }
    return count;
}

int main() {
    int array[] = {-1, -1, 1};
    int result = subarraySum(array, 3, 0);
    printf(">>> result = %d\n", result);
    
    return 0;
}
