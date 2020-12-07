#include <stdio.h>

void moveZeroes(int* nums, int numsSize) {
    if (numsSize <= 0) return;
    int first = 0;
    int second;
    while (first < numsSize) {
        while (first < numsSize && nums[first]) {  // 找零
            first++;
        }
        second = first + 1;
        while (second < numsSize && !nums[second]) {  // 找非零
            second++;
        }
        if (second < numsSize) {
            int tmp = nums[first];
            nums[first] = nums[second];
            nums[second] = tmp;
        }
        first++;
    }
}

void printArray(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        printf("%d\n", nums[i]);
    }
    printf("==========\n");
}

int main() {
    int arr1[] = {0, 1, 0, 3, 12};
    int arr2[] = {0, 11, 0, 3, 2};

    moveZeroes(arr1, 5);
    printArray(arr1, 5);

    moveZeroes(arr2, 5);
    printArray(arr2, 5);

    return 0;
}
