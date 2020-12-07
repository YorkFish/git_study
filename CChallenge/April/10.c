#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* data;
    int* mins;
    int size;
} MinStack;

/** initialize your data structure here. */

MinStack* minStackCreate() {
    MinStack* s = malloc(sizeof(MinStack));
    s->data = NULL;
    s->mins = NULL;
    s->size = 0;
    return s;
}

void minStackPush(MinStack* obj, int x) {
    obj->data = realloc(obj->data, sizeof(int)*(obj->size+1));
    obj->mins = realloc(obj->mins, sizeof(int)*(obj->size+1));
    obj->data[obj->size] = x;
    if (obj->size == 0 || x < obj->mins[obj->size-1]) {
        obj->mins[obj->size] = x;
    }
    else {
        obj->mins[obj->size] = obj->mins[obj->size-1];
    }
    obj->size++;
}

void minStackPop(MinStack* obj) {
    obj->size--;
}

int minStackTop(MinStack* obj) {
    return obj->data[obj->size-1];
}

int minStackGetMin(MinStack* obj) {
    return obj->mins[obj->size-1];
}

void minStackFree(MinStack* obj) {
    free(obj->data);
    free(obj->mins);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStack();
 * minStackPush(obj, x);

 * minStackPop(obj);

 * int param_3 = minStackTop(obj);

 * int param_4 = minStackGetMin(obj);

 * minStackFree(obj);
 */

int main() {
    MinStack* obj = minStackCreate();

    minStackPush(obj, -2);
    minStackPush(obj, 0);
    minStackPush(obj, -3);
    int param_1 = minStackGetMin(obj);
    minStackPop(obj);
    int param_2 = minStackTop(obj);
    int param_3 = minStackGetMin(obj);
    minStackFree(obj);

    printf(">>> param_1 = %d, param_2 = %d, param_3 = %d\n",
        param_1, param_2, param_3);

    return 0;
}
