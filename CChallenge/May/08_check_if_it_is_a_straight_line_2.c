#include <stdio.h>
#include <stdbool.h>

bool checkStraightLine(int** coordinates, int coordinatesSize, int* coordinatesColSize){
    int x1 = coordinates[0][0], y1 = coordinates[0][1];
    int x2 = coordinates[1][0], y2 = coordinates[1][1];
    int X1_X2 = x1 - x2, Y1_Y2 = y1 - y2;
    for (int k = 2; k < coordinatesSize; k ++ ){
        int x3 = coordinates[k][0], y3 = coordinates[k][1];
        // (x1 - x2) / (y1 - y2), (x1 - x3) / (y1 - y3)
        if (X1_X2 * (y1 - y3) != (x1 - x3) * Y1_Y2) {
            return false;
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
