#include <stdio.h>
#include <stdbool.h>

struct Entry {
    int num;
    int count;
};

void addOne(struct Entry* countMap, int num, int hashTableSize) {
    int hash = (num % hashTableSize + hashTableSize) % hashTableSize;
    while (true) {
        if (countMap[hash].count == 0) {
            countMap[hash].num = num;
            countMap[hash].count = 1;
            return;
        }
        if (countMap[hash].num == num) {
            countMap[hash].count ++ ;
            return;
        }
        hash = (hash + 1) % hashTableSize;
    }
}

int majorityElement(int* nums, int numsSize){
    int halfNumsSize = numsSize / 2;
    int hashTableSize = numsSize * 2;
    struct Entry countMap[hashTableSize];
    for (int i = 0; i < hashTableSize; i ++ ) {
        countMap[i].count = 0;
    }

    for (int i = 0; i < numsSize; i ++ ) {
        addOne(countMap, nums[i], hashTableSize);
    }
    for (int i = 0; i < hashTableSize; i ++ ) {
        if (halfNumsSize < countMap[i].count) {
            return countMap[i].num;
        }
    }
    return -1;
}

int main() {
    int nums1[] = {3, 2, 3};
    int nums2[] = {2, 2, 1, 1, 1, 2, 2};
    int ans1 = majorityElement(nums1, 3);
    int ans2 = majorityElement(nums2, 7);
    printf("ans1: %d\n", ans1);
    printf("ans2: %d\n", ans2);

    return 0;
}
