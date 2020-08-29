#include <stdio.h>

int subarraySum(int* nums, int numsSize, int k) {
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i; j < numsSize; j++) {
            int sum = 0;
            for (int x = i; x <= j; x++) {
                sum += nums[x];
            }
            if (sum == k) {
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
