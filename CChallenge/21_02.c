#include <stdio.h>

/**
 * This is the BinaryMatrix's API interface.
 * You should not implement it, or speculate about its implementation
 *
 * 自己写个简单的凑合用
 */
struct BinaryMatrix {
    int row, col;
    int binMatrixDimesions[2];
    int** binMatrix;

    int (*get)(struct BinaryMatrix*, int, int);
    int* (*dimensions)(struct BinaryMatrix*);
};

int count = 0;
int myGet(struct BinaryMatrix* matrix, int row, int col) {
    if (row < 0 || row >= matrix->row) return -1;
    if (col < 0 || col >= matrix->col) return -1;

    count++;
    if (count > 1000) return -1;
    return matrix->binMatrix[row][col];
}

int* myDimensions(struct BinaryMatrix* matrix) {
    matrix->binMatrixDimesions[0] = matrix->row;
    matrix->binMatrixDimesions[1] = matrix->col;
    return matrix->binMatrixDimesions;
}

int binarySearch(struct BinaryMatrix* matrix, int row, int start, int end) {
    // range: [start, end)
    if (start == end) return -1;

    int mid = (start + end) / 2;
    if (matrix->get(matrix, row, mid) == 1) {
        if (mid == 0) {
            return mid;
        }
        if (matrix->get(matrix, row, mid-1) == 0) {
            return mid;
        }
        else {
            return binarySearch(matrix, row, start, mid);
        }
    }
    else {
        return binarySearch(matrix, row, mid+1, end);
    }
}

int findFirstOne(struct BinaryMatrix* matrix, int row) {
    int m = matrix->dimensions(matrix)[1];
    return binarySearch(matrix, row, 0, m);
}

int leftMostColumnWithOne(struct BinaryMatrix* matrix) {
    int n = matrix->dimensions(matrix)[0];

    int leftMostCol = -1;
    for (int row = 0; row < n; row++) {
        int leftCol = findFirstOne(matrix, row);
        if (leftCol != -1) {
            if (leftMostCol == -1 || leftCol < leftMostCol) {
                leftMostCol = leftCol;
            }
        }
    }
    return leftMostCol;
}

int main() {
    int nums[][4] = {
        {0, 0, 0, 1},
        {0, 0, 1, 1},
        {0, 1, 1, 1}
    };
    int* arr[] = {nums[0], nums[1], nums[2]};
    struct BinaryMatrix bm;
    bm.row = 3;
    bm.col = 4;
    bm.binMatrix = arr;
    bm.get = myGet;
    bm.dimensions = myDimensions;

    int result = leftMostColumnWithOne(&bm);
    printf(">>> result = %d\n", result);

    return 0;
}
