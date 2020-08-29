#include <stdio.h>
#include <stdbool.h>

void drawGrid(char** grid, int NUMBER_OF_ROWS, int NUMBER_OF_COLS) {
    for (int i = 0; i < NUMBER_OF_ROWS; i++) {
        for (int j = 0; j < NUMBER_OF_COLS; j++) {
            printf("%c", grid[i][j]);
        }
        printf("\n");
    }
    printf("----------\n");
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;

    const char WATER = '0';
    const char LAND = '1';
    const char NEW = 'X';
    const char USED = 'O';
    int NUMBER_OF_ROWS = gridSize;
    int NUMBER_OF_COLS = gridColSize[0];
    int numberOfIslands = 0;
    for (int i = 0; i < NUMBER_OF_ROWS; i++) {
        for (int j = 0; j < NUMBER_OF_COLS; j++) {
            if (grid[i][j] == LAND) {
                grid[i][j] = NEW;
                bool hasNew;
                do {
                    hasNew = false;
                    for (int y = 0; y < NUMBER_OF_ROWS; y++) {
                        for (int x = 0; x < NUMBER_OF_COLS; x++) {
                            if (grid[y][x] == LAND) {
                                int upX = x;
                                int upY = y-1;
                                if (upY >= 0 && grid[upY][upX] == NEW) {
                                    grid[y][x] = NEW;
                                    hasNew = true;
                                }

                                int downX = x;
                                int downY = y+1;
                                if (downY < NUMBER_OF_ROWS && grid[downY][downX] == NEW) {
                                    grid[y][x] = NEW;
                                    hasNew = true;
                                }

                                int leftX = x-1;
                                int leftY = y;
                                if (leftX >= 0 && grid[leftY][leftX] == NEW) {
                                    grid[y][x] = NEW;
                                    hasNew = true;
                                }

                                int rightX = x+1;
                                int rightY = y;
                                if (rightX < NUMBER_OF_COLS && grid[rightY][rightX] == NEW) {
                                    grid[y][x] = NEW;
                                    hasNew = true;
                                }
                            }
                        }
                    }
                } while (hasNew);

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
