#include <stdio.h>
#include <stdbool.h>

int search(int* nums, int numsSize, int target) {
    int start = 0, end = numsSize;
    while (true) {
        if (start == end) return -1;

        int mid = (start + end) / 2;
        if (nums[mid] == target) return mid;

        if (target < nums[mid]) {
            if (nums[0] > nums[mid]) {
                end = mid;
            }
            else {
                if (nums[0] > target) {
                    start = mid + 1;
                }
                else {
                    end = mid;
                }
            }
        }

        if (nums[mid] < target) {
            if (nums[0] < nums[mid]) {
                start = mid + 1;
            }
            else {
                if (nums[0] > target) {
                    start = mid + 1;
                }
                else {
                    end = mid;
                }
            }
        }
    }
    return -1;
}

int main() {
    int arr[] = {3, 1};
    int result = search(arr, 2, 3);
    printf(">>> result = %d\n", result);

    return 0;
}
