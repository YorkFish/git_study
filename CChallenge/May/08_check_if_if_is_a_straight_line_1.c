#include <stdio.h>
#include <stdbool.h>

bool isSameSlope(int** coordinates, int i, int j, int k) {
    int x1 = coordinates[i][0];
    int y1 = coordinates[i][1];
    int x2 = coordinates[j][0];
    int y2 = coordinates[j][1];
    int x3 = coordinates[k][0];
    int y3 = coordinates[k][1];
    // (x1 - x2) / (y1 - y2), (x1 - x3) / (y1 - y3)
    return (double)(x1 - x2) * (y1 - y3) == (double)(x1 - x3) * (y1 - y2);  // 浮点数有误差

}

bool checkStraightLine(int** coordinates, int coordinatesSize, int* coordinatesColSize){
    for (int i = 0; i < coordinatesSize - 2; i ++ ) {
        for (int j = i + 1; j < coordinatesSize - 1; j ++ ) {
            for (int k = j + 1; k < coordinatesSize; k ++ ){
                if (!isSameSlope(coordinates, i, j, k)) {
                    return false;
                }
            }
        }
    }
    return true;
}

int main() {
    int pos1[] = {1, 1};
    int pos2[] = {2, 2};
    int pos3[] = {3, 4};
    int pos4[] = {4, 5};
    int pos5[] = {5, 6};
    int pos6[] = {7, 7};
    int coordinatesColSize[] = {2, 2, 2, 2, 2, 2};
    int* coordinates[] = {pos1, pos2, pos3, pos4, pos5, pos6};
    bool ans = checkStraightLine(coordinates, 6, coordinatesColSize);
    if (ans) printf("is straight line\n");
    else printf("is not straight line\n");

    return 0;
}
