#include <stdio.h>

void moveZeroes(int* nums, int numsSize) {
    int j = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != 0) {
            nums[j] = nums[i];
            j++;
        }
    }
    while (j < numsSize) {
        nums[j++] = 0;
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
