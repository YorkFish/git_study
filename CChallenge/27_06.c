#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int min2(int a, int b) {
    return a < b ? a : b;
}

int min3(int a, int b, int c) {
    return min2(min2(a, b), c);
}

int max2(int a, int b) {
    return a < b ? b : a;
}

int findMaximalSquareBottomLeftOne(char** matrix, int rows, int cols) {
    if (rows == 0 || cols == 0) return 0;
    if (matrix[rows-1][cols-1] == '0') return 0;
    return min3(
        findMaximalSquareBottomLeftOne(matrix, rows-1, cols),
        findMaximalSquareBottomLeftOne(matrix, rows, cols-1),
        findMaximalSquareBottomLeftOne(matrix, rows-1, cols-1)) + 1;
}

int findMaximalSquare(char** matrix, int rows, int cols, int** cache) {
    if (rows == 0 || cols == 0) return 0;
    if (cache[rows][cols] != -1) return cache[rows][cols];

    // case 1
    // 当右下角是 0 时，或者
    // 当右下角是 1 时，但不在最大正方形内时
    int answer1 = max2(
        findMaximalSquare(matrix, rows-1, cols, cache),
        findMaximalSquare(matrix, rows, cols-1, cache));

    // case 2
    // 当右下角是 1，且在最大正方形内时，
    int answer2 = findMaximalSquareBottomLeftOne(matrix, rows, cols);
    cache[rows][cols] = max2(answer1, answer2);

    return cache[rows][cols];
}

int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) return 0;

    int rows = matrixSize;
    int cols = matrixColSize[0];
    int** cache = malloc((rows+1) * sizeof(int*));
    for (int row = 0; row <= rows; row++) {
        cache[row] = malloc((cols+1) * sizeof(int));
    }
    for (int row = 0; row <= rows; row++) {
        for (int col = 0; col <= cols; col++) {
            cache[row][col] = -1;  // miss
        }
    }

    int answer = findMaximalSquare(matrix, rows, cols, cache);

    for (int row = 0; row <= rows; row++) {
        free(cache[row]);
    }
    free(cache);

    return answer * answer;
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
