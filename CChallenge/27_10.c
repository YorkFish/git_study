#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int min2(int a, int b) {
    if (a < b) return a;
    return b;
}

int min3(int a, int b, int c) {
    return min2(min2(a, b), c);
}

int max2(int a, int b) {
    return a < b ? b : a;
}

int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) return 0;
    
    int** cache1 = malloc((matrixSize+1) * sizeof(int*));
    int** cache2 = malloc((matrixSize+1) * sizeof(int*));
    for (int row = 0; row <= matrixSize; row++) {
        cache1[row] = calloc(matrixColSize[0]+1, sizeof(int));
        cache2[row] = malloc((matrixColSize[0]+1) * sizeof(int));
    }
    for (int row = 0; row <= matrixSize; row++) {
        for (int col = 0; col <= matrixColSize[0]; col++) {
            cache2[row][col] = -1;  // miss
        }
    }

    for (int rows = 0; rows <= matrixSize; rows++) {
        for (int cols = 0; cols <= matrixColSize[0]; cols++) {
            if (rows == 0 || cols == 0) {
                cache2[rows][cols] = 0;
                continue;
            }
            if (matrix[rows-1][cols-1] == '0') {
                cache2[rows][cols] = 0;
                continue;
            }
            cache2[rows][cols] = min3(
                cache2[rows-1][cols],
                cache2[rows][cols-1],
                cache2[rows-1][cols-1]) + 1;
        }
    }

    for (int rows = 1; rows <= matrixSize; rows++) {
        for (int cols = 1; cols <= matrixColSize[0]; cols++) {
            cache1[rows][cols] = max2(
                max2(cache1[rows-1][cols], cache1[rows][cols-1]),
                cache2[rows][cols]);
        }
    }

    int answer = cache1[matrixSize][matrixColSize[0]];

    for (int row = 0; row < matrixSize; row++) {
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
