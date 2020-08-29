#include <stdio.h>
#include <limits.h>

// (0, 0) => ... => (row, col)
int minPartialPathSum(int** grid, int row, int col) {
    if (row == 0 && col == 0) return grid[0][0];

    int min = INT_MAX;
    if (row-1 >= 0) {
        int upMin = minPartialPathSum(grid, row-1, col) + grid[row][col];
        if (upMin < min) {
            min = upMin;
        }
    }
    if (col-1 >= 0) {
        int leftMin = minPartialPathSum(grid, row, col-1) + grid[row][col];
        if (leftMin < min) {
            min = leftMin;
        }
    }
    return min;
}

int minPathSum(int** grid, int gridSize, int* gridColSize) {
    int M = gridSize;  // row
    int N = gridColSize[0];  // col
    return minPartialPathSum(grid, M-1, N-1);
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
