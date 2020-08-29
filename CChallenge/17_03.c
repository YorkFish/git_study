#include <stdio.h>
#include <stdbool.h>

const char WATER = '0';
const char LAND = '1';
const char NEW = 'X';
const char USED = 'O';

void drawGrid(char** grid, int NUMBER_OF_ROWS, int NUMBER_OF_COLS) {
    for (int i = 0; i < NUMBER_OF_ROWS; i++) {
        for (int j = 0; j < NUMBER_OF_COLS; j++) {
            printf("%c", grid[i][j]);
        }
        printf("\n");
    }
    printf("----------\n");
}

void floorFill(char** grid, int NUMBER_OF_ROWS, int NUMBER_OF_COLS, int i, int j) {
    if (i < 0 || j < 0 || i >= NUMBER_OF_ROWS || j >= NUMBER_OF_COLS || grid[i][j] != LAND) return;
    grid[i][j] = NEW;
    floorFill(grid, NUMBER_OF_ROWS, NUMBER_OF_COLS, i+1, j);
    floorFill(grid, NUMBER_OF_ROWS, NUMBER_OF_COLS, i-1, j);
    floorFill(grid, NUMBER_OF_ROWS, NUMBER_OF_COLS, i, j+1);
    floorFill(grid, NUMBER_OF_ROWS, NUMBER_OF_COLS, i, j-1);
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int NUMBER_OF_ROWS = gridSize;
    int NUMBER_OF_COLS = gridColSize[0];
    int numberOfIslands = 0;
    for (int i = 0; i < NUMBER_OF_ROWS; i++) {
        for (int j = 0; j < NUMBER_OF_COLS; j++) {
            if (grid[i][j] == LAND) {
                floorFill(grid, NUMBER_OF_ROWS, NUMBER_OF_COLS, i, j);
                for (int y = 0; y < NUMBER_OF_ROWS; y++) {
                    for (int x = 0; x < NUMBER_OF_COLS; x++) {
                        if (grid[y][x] == NEW) {
                            grid[y][x] = USED;
                        }
                    }
                }
                numberOfIslands++;
            }
        }
    }
    return numberOfIslands;
}

int main() {
    char temp[][5] = {
        "11110",
        "11010",
        "11000",
        "00000"
    };
    char* grid[] = {temp[0], temp[1], temp[2], temp[3]};
    int gridSize = 4;
    int gridColSize[] = {5, 5, 5, 5};
    drawGrid(grid, gridSize, gridColSize[0]);
    int result = numIslands(grid, gridSize, gridColSize);
    printf(">>> result = %d\n", result);
    drawGrid(grid, gridSize, gridColSize[0]);

    return 0;
}
