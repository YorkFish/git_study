#include <stdio.h>

void moveZeroes(int* nums, int numsSize) {
    int loop = 1;
    while (loop) {
        for (int i = 0; i < numsSize-1; i++) {
            if (nums[i] == 0 && nums[i+1] != 0) {
                nums[i] = nums[i+1];
                nums[i+1] = 0;
                break;
            }
            if (i == numsSize-2) loop = 0;
        }
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
