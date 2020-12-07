#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int minPathSum(int** grid, int gridSize, int* gridColSize) {
    int M = gridSize;  // row
    int N = gridColSize[0];  // col
    int** cache = malloc(M * sizeof(int*));
    for (int i = 0; i < M; i++) {
        cache[i] = calloc(N, sizeof(int));
    }

    for (int row = 0; row < M; row++) {
        for (int col = 0; col < N; col++) {
            if (row == 0 && col == 0) {
                cache[row][col] = grid[0][0];
                continue;
            }
            int min = INT_MAX;
            if (row-1 >= 0) {
                int upMin = cache[row-1][col];
                if (upMin < min) {
                    min = upMin;
                }
            }
            if (col-1 >= 0) {
                int leftMin = cache[row][col-1];
                if (leftMin < min) {
                    min = leftMin;
                }
            }
            cache[row][col] = min + grid[row][col];
        }
    }
    int result = cache[M-1][N-1];
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
