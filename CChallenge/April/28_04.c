#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define CAPACITY (100000+50000)

typedef struct {
    int table[100000001];  // table[value]: value 在 data 中出现了几次
    int data[CAPACITY];
    int size;
} FirstUnique;

void firstUniqueAdd(FirstUnique* obj, int value) {
    obj->table[value]++;
    obj->data[obj->size] = value;  // obj->size 可以代表新增的位置编号
    obj->size++;
}

FirstUnique* firstUniqueCreate(int* nums, int numsSize) {
    FirstUnique* obj = calloc(1, sizeof(FirstUnique));
    obj->size = numsSize;
    for (int i = 0; i < numsSize; i++) {
        firstUniqueAdd(obj, nums[i]);
    }
    return obj;
}

int firstUniqueShowFirstUnique(FirstUnique* obj) {
    for (int i = 0; i < obj->size; i++) {
        if (obj->table[obj->data[i]] == 1) {
            return obj->data[i];
        }
    }
    return -1;
}

void firstUniqueFree(FirstUnique* obj) {
    free(obj);
}

int main() {
    int nums[5] = {3, 9, 7, 1, 5};
    FirstUnique* obj = firstUniqueCreate(nums, 5);  // obj: {3, 9, 7, 1, 5}
    printf("%d\n", firstUniqueShowFirstUnique(obj));  // 3

    firstUniqueAdd(obj, 3);  // obj: {3, 9, 7, 1, 5, 3}
    printf("%d\n", firstUniqueShowFirstUnique(obj));  // 9
    
    firstUniqueAdd(obj, 9);  // obj: {3, 9, 7, 1, 5, 3, 9}
    printf("%d\n", firstUniqueShowFirstUnique(obj));  // 7
    
    firstUniqueFree(obj);

    return 0;
}
