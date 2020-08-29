#include <stdio.h>
#include <stdbool.h>

int extractMax(int* counter) {
    for (int i = 1000; i > 0; i--) {
        if (counter[i] > 0) {
            counter[i]--;
            return i;
        }
    }
    return 0;
}

void insert(int* counter, int val) {
    counter[val]++;
}

int lastStoneWeight(int* stones, int stonesSize){
    int counter[1001] = {0};
    for (int i = 0; i < stonesSize; i++) {
        counter[stones[i]]++;
    }
    while (true) {
        int y = extractMax(counter);
        int x = extractMax(counter);
        if (x == 0) {
            return y;
        }
        else if (x != y) {
            insert(counter, y-x);
        }
    }
    return 0;
}

int main() {
    int stones[] = {2, 7, 4, 1, 8, 1};
    int stonesSize = 6;
    int result = lastStoneWeight(stones, stonesSize);
    printf(">>> result = %d\n", result);

    return 0;
}
