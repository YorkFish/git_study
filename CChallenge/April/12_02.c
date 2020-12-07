#include <stdio.h>
#include <stdbool.h>

int extractMax(int* stones, int stonesSize) {
    int max_i = 0;
    for (int i = 1; i < stonesSize; i++) {
        if (stones[max_i] < stones[i]) {
            max_i = i;
        }
    }
    int max = stones[max_i];
    stones[max_i] = 0;
    return max;
}

void insert(int* stones, int stonesSize, int val) {
    for (int i = 0; i < stonesSize; i++) {
        if (stones[i] == 0) {
            stones[i] = val;
            break;
        }
    }
}

int lastStoneWeight(int* stones, int stonesSize){
    while (true) {
        int y = extractMax(stones, stonesSize);
        int x = extractMax(stones, stonesSize);
        if (x == 0) {
            return y;
        }
        else if (x != y) {
            insert(stones, stonesSize, y-x);
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
