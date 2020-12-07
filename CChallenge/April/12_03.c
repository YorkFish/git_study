#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int lastStoneWeight(int* stones, int stonesSize){
    if (stonesSize < 2) return stones[0];
    while (true) {
        qsort(stones, stonesSize, sizeof(int), cmp);
        int y = stones[0];
        int x = stones[1];
        stones[0] = stones[1] = 0;
        if (x == 0) {
            return y;
        }
        else if (x != y) {
            stones[0] = y - x;
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
