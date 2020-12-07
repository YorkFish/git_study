#include <stdio.h>

int singleNonDuplicate(int* nums, int numsSize){
    for (int i = 0; i + 1 < numsSize; i += 2) {
        if (nums[i] != nums[i + 1]) {
            return nums[i];
        }
    }
    return nums[numsSize - 1];
}

int main() {
    int nums[] = {1, 1, 2, 3, 3, 4, 4, 8, 8};
    int ans = singleNonDuplicate(nums, 9);
    printf("single element: %d\n", ans);

    return 0;
}
