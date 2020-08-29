#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int minPartialPathSum(int** grid, int row, int col, int** cache) {
    if (row == 0 && col == 0) return grid[0][0];
    if (cache[row][col] != 0) return cache[row][col];

    int min = INT_MAX;
    if (row-1 >= 0) {
        int upMin = minPartialPathSum(grid, row-1, col, cache);
        if (upMin < min) {
            min = upMin;
        }
    }
    if (col-1 >= 0) {
        int leftMin = minPartialPathSum(grid, row, col-1, cache);
        if (leftMin < min) {
            min = leftMin;
        }
    }
    cache[row][col] = min + grid[row][col];

    return cache[row][col];
}

int minPathSum(int** grid, int gridSize, int* gridColSize) {
    int M = gridSize;  // row
    int N = gridColSize[0];  // col
    int** cache = malloc(M * sizeof(int*));
    for (int i = 0; i < M; i++) {
        cache[i] = calloc(N, sizeof(int));
    }
    int result = minPartialPathSum(grid, M-1, N-1, cache);
    for (int i = 0; i < M; i++) {
        free(cache[i]);
    }
    free(cache);
    return result;
}

int main() {
    int temp[][3] = {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1}
    };
    int* grid[] = {temp[0], temp[1], temp[2]};
    int gridSize = 3;
    int gridColSize[] = {3, 3, 3};
    int result = minPathSum(grid, gridSize, gridColSize);
    printf(">>> result = %d\n", result);

    return 0;
}
