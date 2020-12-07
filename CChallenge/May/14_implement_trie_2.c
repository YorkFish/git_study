#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct Node_ {
    bool isEnd;
    struct Node_ * children[26];  // 'a' - 'z'
} Node;

typedef struct {
    Node* root;
} Trie;

/** Initialize your data structure here. */

Trie* trieCreate() {
    Trie* trie = calloc(1, sizeof(Trie));
    trie->root = calloc(1, sizeof(Node));    
    return trie;
}

/** Inserts a word into the trie. */
void trieInsert(Trie* obj, char * word) {
    Node* cur = obj->root;
    for (int i = 0; word[i] != '\0'; i ++ ) {
        int index = word[i] - 'a';
        if (cur->children[index] == NULL) {
            cur->children[index] = calloc(1, sizeof(Node));
        }
        cur = cur->children[index];
    }
    cur->isEnd = true;
}

/** Returns if the word is in the trie. */
bool trieSearch(Trie* obj, char * word) {
    Node* cur = obj->root;
    for (int i = 0; word[i] != '\0'; i ++ ) {
        int index = word[i] - 'a';
        if (cur->children[index] == NULL) {
            return false;
        }
        cur = cur->children[index];
    }
    return cur->isEnd;
}

/** Returns if there is any word in the trie that starts with the given prefix. */
bool trieStartsWith(Trie* obj, char * prefix) {
    Node* cur = obj->root;
    for (int i = 0; prefix[i] != '\0'; i ++ ) {
        int index = prefix[i] - 'a';
        if (cur->children[index] == NULL) {
            return false;
        }
        cur = cur->children[index];
    }

    return true;
}

void nodeFree(Node* root) {
    if (root == NULL) return;
    for (char c = 'a'; c <= 'z'; c ++ ) {
        int index = c - 'a';
        nodeFree(root->children[index]);
    }
    free(root);
}

void trieFree(Trie* obj) {
    nodeFree(obj->root);
    free(obj);
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/

int main() {
    char word[] = "apple";
    char prefix[] = "app";
    Trie* obj = trieCreate();
    trieInsert(obj, word);
    bool param_2 = trieSearch(obj, word);
    bool param_3 = trieStartsWith(obj, prefix);
    trieFree(obj);

    if (param_2) printf("have %s\n", word);
    if (param_3) printf("start with %s\n", prefix);

    return 0;
}
