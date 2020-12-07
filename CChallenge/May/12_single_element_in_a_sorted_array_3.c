#include <stdio.h>

int singleNonDuplicate(int* nums, int numsSize){
    int begin = 0, end = numsSize;
    while (end - begin != 1) {
        //      [1, 1, 2, |2, 3, 4|, 4, 5, 5]
        // ans:               ^
        int mid = begin + (end - begin) / 2;
        if (nums[mid - 1] < nums[mid] && nums[mid] < nums[mid + 1]) {
            return nums[mid];
        }

        //      [1, 2, |2, 3, 3|, 4, 4]
        // ans: [ odd    ]
        if (mid % 2 == 1 && nums[mid - 1] < nums[mid] && nums[mid] == nums[mid + 1]) {
            end = mid;
        }

        //      [1, 1, 2, |3, 3, 4|, 4, 5, 5]
        // ans: [ odd   ]
        else if (mid % 2 == 0 && nums[mid - 1] == nums[mid] && nums[mid] < nums[mid + 1]) {
            end = mid - 1;
        }

        //      [1, 1, 2, |2, 3, 3|, 4, 4, 5]
        // ans:                     [ odd   ]
        else if (nums[mid - 1] < nums[mid] && nums[mid] == nums[mid + 1]) {
            begin = mid + 2;
        }

        //      [1, 1, |2, 2, 3|, 3, 4]
        // ans:              [ odd    ]
        else {
            begin = mid + 1;
        }
    }
    return nums[begin];
}

int main() {
    int nums[] = {1, 1, 2, 3, 3, 4, 4, 8, 8};
    int ans = singleNonDuplicate(nums, 9);
    printf("single element: %d\n", ans);

    return 0;
}
