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

int maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0) return 0;
    
    int** cache2 = malloc((matrixSize+1) * sizeof(int*));  // cache2 可以改名为 maximalSquareBottomLeft
    for (int row = 0; row <= matrixSize; row++) {
        cache2[row] = calloc(matrixColSize[0]+1, sizeof(int));
    }

    int answer = 0;
    for (int rows = 1; rows <= matrixSize; rows++) {
        for (int cols = 1; cols <= matrixColSize[0]; cols++) {
            if (matrix[rows-1][cols-1] == '1') {
                cache2[rows][cols] = min3(  // 这个关系式是最重要的
                    cache2[rows-1][cols],
                    cache2[rows][cols-1],
                    cache2[rows-1][cols-1]) + 1;
            }
            
            answer = max2(answer, cache2[rows][cols]);
        }
    }

    for (int row = 0; row < matrixSize; row++) {
        free(cache2[row]);
    }
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
