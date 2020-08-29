#include <stdio.h>
#include <stdlib.h>

// 键值对（字典）
struct Entry {
    int key;
    int value;
    int priority;
};

typedef struct {
    struct Entry* entries;
    int capacity;  // 数量
    int currentPriority;  // 优先度，碰一下就加一，可以理解成 time，越大越新
} LRUCache;

/*
lRUCacheCreat(3): obj->
                       capacity: 3
                       entries: [(key, value, priority),
                                 (key, value, priority),
                                 (key, value, priority)]
*/
LRUCache* lRUCacheCreat(int capacity) {
    LRUCache* obj = malloc(sizeof(LRUCache));
    obj->entries = calloc(capacity, sizeof(struct Entry));
    obj->capacity = capacity;
    obj->currentPriority = 0;
    for (int i = 0; i < capacity; i++) {
        obj->entries[i].key = -1;
    }
    return obj;
}

int lRUCacheGet(LRUCache* obj, int key) {
    // 有
    for (int i = 0; i < obj->capacity; i++) {
        if (obj->entries[i].key == key) {
            obj->currentPriority++;
            obj->entries[i].priority = obj->currentPriority;
            return obj->entries[i].value;
        }
    }
    // 没有
    return -1;
}

void lRUCachePut(LRUCache* obj, int key, int value) {
    // 原本就有：覆盖，取代
    for (int i = 0; i < obj->capacity; i++) {
        if (obj->entries[i].key == key) {
            obj->entries[i].value = value;
            obj->currentPriority++;
            obj->entries[i].priority = obj->currentPriority;
            return;
        }
    }

    // 原本没有：新增
    //     未满：新增在空格 (key, -1)
    for (int i = 0; i < obj->capacity; i++) {
        if (obj->entries[i].key == -1) {
            obj->entries[i].key = key;
            obj->entries[i].value = value;
            obj->currentPriority++;
            obj->entries[i].priority = obj->currentPriority;
            return;
        }
    }
    //     已满：找到 priority 最小的做取代
    int minI = 0;  // priority 最小的 entry 的索引号
    for (int i = 1; i < obj->capacity; i++) {
        if (obj->entries[i].priority < obj->entries[minI].priority) {
            minI = i;
        }
    }
    obj->entries[minI].key = key;
    obj->entries[minI].value = value;
    obj->currentPriority++;
    obj->entries[minI].priority = obj->currentPriority;
}

void lRUCacheFree(LRUCache* obj) {
    // LRUCache* obj = malloc(sizeof(LRUCache));
    // obj->entries = calloc(capacity, sizeof(struct Entry));
    // 这里释放与创建泛反着来
    free(obj->entries);
    free(obj);
}

int main() {
    LRUCache* obj = lRUCacheCreat(2);
    lRUCachePut(obj, 1, 1);
    lRUCachePut(obj, 2, 2);

    int param_1 = lRUCacheGet(obj, 1);
    printf(">>> param_1 = %d\n",param_1);  // 1
    
    lRUCachePut(obj, 3, 3);
    int param_2 = lRUCacheGet(obj, 2);
    printf(">>> param_2 = %d\n",param_2);  // -1
    
    lRUCachePut(obj, 4, 4);
    int param_3 = lRUCacheGet(obj, 3);
    printf(">>> param_3 = %d\n",param_3);  // 3
    
    int param_4 = lRUCacheGet(obj, 4);
    printf(">>> param_4 = %d\n",param_4);  // 4

    lRUCacheFree(obj);

    return 0;
}
