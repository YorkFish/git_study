#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int** floodFill(int** image, int imageSize, int* imageColSize,
        int sr, int sc, int newColor, int* returnSize, int** returnColumnSizes) {
    const int nRows = imageSize, nCols = imageColSize[0];
    int** result = malloc(nRows * sizeof(int*));
    for (int row = 0; row < nRows; row ++ ) {
        result[row] = malloc(nCols * sizeof(int));
    }
    for (int row = 0; row < nRows; row ++ ) {
        for (int col = 0; col < nCols; col ++ ) {
            result[row][col] = image[row][col];
        }
    }

    int targetColor = result[sr][sc];
    result[sr][sc] = -1;
    bool isDirty = true;
    while (isDirty) {
        isDirty = false;
        for (int row = 0; row < nRows; row ++ ) {
            for (int col = 0; col < nCols; col ++ ) {
                if (result[row][col] == -1) {
                    if (row - 1 >= 0 && result[row - 1][col] == targetColor) {
                        result[row - 1][col] = -1;
                        isDirty = true;
                    }
                    if (row + 1 < nRows && result[row + 1][col] == targetColor) {
                        result[row + 1][col] = -1;
                        isDirty = true;
                    }
                    if (col - 1 >= 0 && result[row][col - 1] == targetColor) {
                        result[row][col - 1] = -1;
                        isDirty = true;
                    }
                    if (col + 1 < nCols && result[row][col + 1] == targetColor) {
                        result[row][col + 1] = -1;
                        isDirty = true;
                    }
                }
            }
        }
    }
    for (int row = 0; row < nRows; row ++ ) {
        for (int col = 0; col < nCols; col ++ ) {
            if (result[row][col] == -1) {
                result[row][col] = newColor;
            }
        }
    }

    *returnSize = imageSize;
    *returnColumnSizes = malloc(nRows * sizeof(int));
    for (int row = 0; row < nRows; row ++ ) {
        (*returnColumnSizes)[row] = imageColSize[row];
    }
    return result;
}

int main() {
    int row1[] = {1, 1, 1};
    int row2[] = {1, 1, 0};
    int row3[] = {1, 0, 1};
    int* image[] = {row1, row2, row3};
    int imageSize = 3;
    int imageColSize[] = {3, 3, 3};
    int sr = 1, sc = 1;
    int newColor = 2;
    int returnSize;
    int* returnColumnSizes;
    
    int** ans = floodFill(image, imageSize, imageColSize, sr, sc, newColor,
        &returnSize, &returnColumnSizes);

    for (int row = 0; row < imageSize; row ++ ) {
        for (int col = 0; col < imageColSize[row]; col ++ ) {
            printf("%d ", ans[row][col]);
        }
        printf("\n");
    }
    printf("over!\n");

    return 0;
}
