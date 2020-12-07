#include <stdio.h>

// 回传 nums 在 [begin, end) 中只出现一次的数字
int binarySearch(int* nums, int begin, int end) {
    if (end - begin == 1) return nums[begin];

    //      [1, 1, 2, |2, 3, 4|, 4, 5, 5]
    // ans:               ^
    int mid = begin + (end - begin) / 2;
    if (nums[mid - 1] < nums[mid] && nums[mid] < nums[mid + 1]) {
        return nums[mid];
    }

    //      [1, 2, |2, 3, 3|, 4, 4]
    // ans: [ odd    ]
    if (mid % 2 == 1 && nums[mid - 1] < nums[mid] && nums[mid] == nums[mid + 1]) {
        return binarySearch(nums, begin, mid);
    }

    //      [1, 1, 2, |3, 3, 4|, 4, 5, 5]
    // ans: [ odd   ]
    if (mid % 2 == 0 && nums[mid - 1] == nums[mid] && nums[mid] < nums[mid + 1]) {
        return binarySearch(nums, begin, mid - 1);
    }

    //      [1, 1, 2, |2, 3, 3|, 4, 4, 5]
    // ans:                     [ odd   ]
    if (nums[mid - 1] < nums[mid] && nums[mid] == nums[mid + 1]) {
        return binarySearch(nums, mid + 2, end);
    }

    //      [1, 1, |2, 2, 3|, 3, 4]
    // ans:              [ odd    ]
    if (nums[mid - 1] == nums[mid] && nums[mid] < nums[mid + 1]) {
        return binarySearch(nums, mid + 1, end);
    }

    return -1;
}

int singleNonDuplicate(int* nums, int numsSize){
    return binarySearch(nums, 0, numsSize);
}

int main() {
    int nums[] = {1, 1, 2, 3, 3, 4, 4, 8, 8};
    int ans = singleNonDuplicate(nums, 9);
    printf("single element: %d\n", ans);

    return 0;
}
