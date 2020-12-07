#include <stdio.h>

int rangeSearch(int* nums, int start, int end, int target) {
    // range: [start, end), target
    if (start == end) return -1;

    int mid = (start + end) / 2;
    if (nums[mid] == target) return mid;

    if (target < nums[mid]) {
        if (nums[0] > nums[mid]) {
            // nums: [6, 7, 8, *0, (1), 2, 3, 4, 5]
            return rangeSearch(nums, start, mid, target);  // FindLeft();
        }
        else {
            if (nums[0] > target) {
                // nums: [3, 4, 5, 6, (7), 8, *0, 1, 2]
                return rangeSearch(nums, mid+1, end, target);  // FindRight();
            }
            else {
                // nums: [3, *4, 5, 6, (7), 8, 0, 1, 2]
                return rangeSearch(nums, start, mid, target);  // FindLeft();
            }
        }
    }

    if (nums[mid] < target) {
        if (nums[0] < nums[mid]) {
            // nums: [3, 4, 5, 6, (7), *8, 0, 1, 2]
            return rangeSearch(nums, mid+1, end, target);  // FindRight();
        }
        else {
            if (nums[0] > target) {
                // nums: [6, 7, 8, 0, (1), 2, 3, *4, 5]
                return rangeSearch(nums, mid+1, end, target);  // FindRight();
            }
            else {
                // nums: [6, 7, *8, 0, (1), 2, 3, 4, 5]
                return rangeSearch(nums, start, mid, target);  // FindLeft();
            }
        }
    }

    return -1;
}

int search(int* nums, int numsSize, int target) {
    return rangeSearch(nums, 0, numsSize, target);
}

int main() {
    int arr[] = {3, 4, 5, 6, 7, 8, 0, 1, 2};
    int result = search(arr, 9, 0);
    printf(">>> result = %d\n", result);

    return 0;
}
