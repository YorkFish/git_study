#include <stdio.h>
#include <stdbool.h>

int min2(int a, int b) {
    return a < b ? a : b;
}

int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) return 0;

    int rows = matrixSize;
    int cols = matrixColSize[0];
    int maxSize = 0;
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            int squareSize = min2(rows-row, cols-col);
            for (int size = 1; size <= squareSize; size++) {
                // 检查在 size * size 的范围内是否没有 0
                bool noZero = true;
                for (int dr = 0; dr < size; dr++) {
                    for (int dc = 0; dc < size; dc++) {
                        if (matrix[row+dr][col+dc] == '0') {
                            noZero = false;
                        }
                    }
                }
                if (noZero && maxSize < size) {
                    maxSize = size;
                }
            }
        }
    }
    return maxSize * maxSize;
}

int main() {
    char arr1[] = "10100";
    char arr2[] = "10111";
    char arr3[] = "11111";
    char arr4[] = "10010";
    char* matrix[] = {arr1, arr2, arr3, arr4};
    int matrixSize = 4;
    int matrixColSize[4] = {5, 5, 5, 5};
    int result = maximalSquare(matrix, matrixSize, matrixColSize);
    printf(">>> result = %d\n", result);

    return 0;
}
