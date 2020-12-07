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

int findMaximalSquareBottomLeftOne(char** matrix, int rows, int cols, int** cache2) {
    if (rows == 0 || cols == 0) return 0;
    if (matrix[rows-1][cols-1] == '0') return 0;
    if (cache2[rows][cols] != -1) return cache2[rows][cols];

    cache2[rows][cols] = min3(
        findMaximalSquareBottomLeftOne(matrix, rows-1, cols, cache2),
        findMaximalSquareBottomLeftOne(matrix, rows, cols-1, cache2),
        findMaximalSquareBottomLeftOne(matrix, rows-1, cols-1, cache2)) + 1;
    return cache2[rows][cols];
}

int findMaximalSquare(char** matrix, int rows, int cols, int** cache1, int** cache2) {
    if (rows == 0 || cols == 0) return 0;
    if (cache1[rows][cols] != -1) return cache1[rows][cols];

    // case 1
    // 当右下角是 0 时，或者
    // 当右下角是 1 时，但不在最大正方形内时
    int answer1 = max2(
        findMaximalSquare(matrix, rows-1, cols, cache1, cache2),
        findMaximalSquare(matrix, rows, cols-1, cache1, cache2));

    // case 2
    // 当右下角是 1，且在最大正方形内时，
    int answer2 = findMaximalSquareBottomLeftOne(matrix, rows, cols, cache2);
    cache1[rows][cols] = max2(answer1, answer2);

    return cache1[rows][cols];
}

int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) return 0;

    int rows = matrixSize;
    int cols = matrixColSize[0];
    int** cache1 = malloc((rows+1) * sizeof(int*));
    int** cache2 = malloc((rows+1) * sizeof(int*));
    for (int row = 0; row <= rows; row++) {
        cache1[row] = malloc((cols+1) * sizeof(int));
        cache2[row] = malloc((cols+1) * sizeof(int));
    }
    for (int row = 0; row <= rows; row++) {
        for (int col = 0; col <= cols; col++) {
            cache1[row][col] = -1;  // miss
            cache2[row][col] = -1;  // miss
        }
    }

    int answer = findMaximalSquare(matrix, rows, cols, cache1, cache2);

    for (int row = 0; row <= rows; row++) {
        free(cache1[row]);
        free(cache2[row]);
    }
    free(cache1);
    free(cache2);

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
