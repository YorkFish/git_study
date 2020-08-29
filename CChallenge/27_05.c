#include <stdio.h>
#include <stdbool.h>

int min2(int a, int b) {
    return a < b ? a : b;
}

int min3(int a, int b, int c) {
    return min2(min2(a, b), c);
}

int max2(int a, int b) {
    return a < b ? b : a;
}

// DP 前的准备
int findMaximalSquareBottomLeftOne(char** matrix, int rows, int cols) {
    if (rows == 0 || cols == 0) return 0;
    if (matrix[rows-1][cols-1] == '0') return 0;
    return min3(
        findMaximalSquareBottomLeftOne(matrix, rows-1, cols),
        findMaximalSquareBottomLeftOne(matrix, rows, cols-1),
        findMaximalSquareBottomLeftOne(matrix, rows-1, cols-1)) + 1;
}

int findMaximalSquare(char** matrix, int rows, int cols) {
    if (rows == 0 || cols == 0) return 0;

    // case 1
    // 当右下角是 0 时，或者
    // 当右下角是 1 时，但不在最大正方形内时
    int answer1 = max2(
        findMaximalSquare(matrix, rows-1, cols),
        findMaximalSquare(matrix, rows, cols-1));

    // case 2
    // 当右下角是 1，且在最大正方形内时，
    int answer2 = findMaximalSquareBottomLeftOne(matrix, rows, cols);

    return max2(answer1, answer2);
}

int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) return 0;

    int rows = matrixSize;
    int cols = matrixColSize[0];
    int answer = findMaximalSquare(matrix, rows, cols);

    return answer * answer;
    // matrix1: [[..... . ],
    //          [..... . ],
    //          [..... . ],
    //          [.....(0)],]

    // matrix2.1: [[..... . ],
    //             [..... . ],
    //             [..... . ],
    //             [.....(1)],]

    // matrix2.2: [[1, 1, 1, 0],
    //             [1, 1, 1, 0],
    //             [1, 1, 1, 0],
    //             [0, 0, 0, 1]]
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
