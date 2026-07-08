#include <stdio.h>
#include <stdlib.h>

#define MAX 3   // Max keys in a node (order = MAX+1)
#define MIN 1   // Min keys in a node

struct Node {
    int keys[MAX+1];          // store keys
    struct Node *child[MAX+2]; // child pointers
    int count;                // number of keys
    int leaf;                 // 1 if leaf, 0 if internal
};

struct Node *root = NULL;

/* Create new node */
struct Node *newNode(int leaf) {
    struct Node *p = (struct Node *)malloc(sizeof(struct Node));
    p->count = 0;
    p->leaf = leaf;
    for (int i = 0; i < MAX+2; i++) p->child[i] = NULL;
    return p;
}

/* Split child */
void splitChild(struct Node *parent, int i, struct Node *child) {
    struct Node *newChild = newNode(child->leaf);
    newChild->count = MIN;

    // Move last MIN keys to newChild
    for (int j = 0; j < MIN; j++)
        newChild->keys[j] = child->keys[j+MIN+1];

    // Move children if not leaf
    if (!child->leaf) {
        for (int j = 0; j <= MIN; j++)
            newChild->child[j] = child->child[j+MIN+1];
    }

    child->count = MIN;

    // Shift parent's children
    for (int j = parent->count; j >= i+1; j--)
        parent->child[j+1] = parent->child[j];

    parent->child[i+1] = newChild;

    // Shift parent's keys
    for (int j = parent->count-1; j >= i; j--)
        parent->keys[j+1] = parent->keys[j];

    parent->keys[i] = child->keys[MIN];
    parent->count++;
}

/* Insert non-full */
void insertNonFull(struct Node *p, int key) {
    int i = p->count-1;

    if (p->leaf) {
        // Shift keys
        while (i >= 0 && key < p->keys[i]) {
            p->keys[i+1] = p->keys[i];
            i--;
        }
        p->keys[i+1] = key;
        p->count++;
    } else {
        while (i >= 0 && key < p->keys[i]) i--;
        i++;
        if (p->child[i]->count == MAX) {
            splitChild(p, i, p->child[i]);
            if (key > p->keys[i]) i++;
        }
        insertNonFull(p->child[i], key);
    }
}

/* Insert wrapper */
void insert(int key) {
    if (root == NULL) {
        root = newNode(1);
        root->keys[0] = key;
        root->count = 1;
        return;
    }

    if (root->count == MAX) {
        struct Node *newRoot = newNode(0);
        newRoot->child[0] = root;
        splitChild(newRoot, 0, root);
        int i = 0;
        if (key > newRoot->keys[0]) i++;
        insertNonFull(newRoot->child[i], key);
        root = newRoot;
    } else {
        insertNonFull(root, key);
    }
}

/* Inorder traversal (prints leaves only for B+ tree) */
void inorder(struct Node *p) {
    if (p == NULL) return;

    if (p->leaf) {
        for (int i = 0; i < p->count; i++)
            printf("%d ", p->keys[i]);
    } else {
        for (int i = 0; i < p->count; i++) {
            inorder(p->child[i]);
        }
        inorder(p->child[p->count]);
    }
}

int main() {
    int keys[] = {10, 20, 5, 6, 12, 30, 7, 17};
    int n = sizeof(keys)/sizeof(keys[0]);

    for (int i = 0; i < n; i++)
        insert(keys[i]);

    inorder(root);
    return 0;
}
