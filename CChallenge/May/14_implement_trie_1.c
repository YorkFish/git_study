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

void nodeInsert(Node* root, char* word) {
    if (word[0] == '\0') {
        root->isEnd = true;
        return;
    }
    int index = word[0] - 'a';
    if (root->children[index] == NULL) {
        root->children[index] = calloc(1, sizeof(Node));
    }
    nodeInsert(root->children[index], word + 1);
}

/** Inserts a word into the trie. */
void trieInsert(Trie* obj, char * word) {
    // obj: {root: Node()}
    // word: "apple"
    nodeInsert(obj->root, word);
}

bool nodeSearch(Node* root, char* word) {
    if (word[0] == '\0') {
        return root->isEnd;
    }
    int index = word[0] - 'a';
    if (root->children[index] == NULL) {
        return false;
    }
    return nodeSearch(root->children[index], word + 1);
}

/** Returns if the word is in the trie. */
bool trieSearch(Trie* obj, char * word) {
    return nodeSearch(obj->root, word);
}

bool nodeStartWith(Node* root, char* prefix) {
    if (prefix[0] == '\0') {
        return true;
    }
    int index = prefix[0] - 'a';
    if (root->children[index] == NULL) {
        return false;
    }
    return nodeStartWith(root->children[index], prefix + 1);
}

/** Returns if there is any word in the trie that starts with the given prefix. */
bool trieStartsWith(Trie* obj, char * prefix) {
    return nodeStartWith(obj->root, prefix);
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
