#include <stdio.h>
#include <stdlib.h>

int CAPACITY = 1000000;

struct Entry {
    int sum;
    int count;
};

// [0, CAPACITY)
int getIndex(int sum) {
    return (sum % CAPACITY + CAPACITY) % CAPACITY;  // -12 % 10 = -1 ...... -2
}

void addOne(struct Entry** counter, int sum) {
    int i = getIndex(sum);
    while (counter[i] != NULL) {
        if (counter[i]->sum == sum) {
            counter[i]->count++;
            return;
        }
        i = getIndex(i+1);
    }
    struct Entry* entry = malloc(sizeof(struct Entry));
    entry->sum = sum;
    entry->count = 1;
    counter[i] = entry;
}

int query(struct Entry** counter, int sum) {
    int i = getIndex(sum);
    while (counter[i] != NULL) {
        if (counter[i]->sum == sum) {
            return counter[i]->count;
        }
        i = getIndex(i+1);
    }
    return 0;
}

int subarraySum(int* nums, int numsSize, int k) {
    // HashTable
    struct Entry** counter = calloc(CAPACITY, sizeof(struct Entry*));

    int sum = 0;
    int totalCount = 0;
    for (int j = 0; j < numsSize; j++) {
        addOne(counter, sum);
        sum += nums[j];
        int target = sum - k;
        totalCount += query(counter, target);
    }
    free(counter);
    return totalCount;
}

int main() {
    int array[] = {-1, -1, 1};
    int result = subarraySum(array, 3, 0);
    printf(">>> result = %d\n", result);
    
    return 0;
}
