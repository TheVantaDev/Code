#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int val, h;
    struct Node *l, *r;
} Node;

Node *root = NULL;

/* helpers */
int height(Node *n) { return n ? n->h : 0; }
int max(int a, int b) { return (a > b) ? a : b; }

/* rotations */
Node* rightRotate(Node *y) {
    Node *x = y->l, *T2 = x->r;
    x->r = y; y->l = T2;
    y->h = 1 + max(height(y->l), height(y->r));
    x->h = 1 + max(height(x->l), height(x->r));
    return x;
}

Node* leftRotate(Node *x) {
    Node *y = x->r, *T2 = y->l;
    y->l = x; x->r = T2;
    x->h = 1 + max(height(x->l), height(x->r));
    y->h = 1 + max(height(y->l), height(y->r));
    return y;
}

int balance(Node *n) { return n ? height(n->l) - height(n->r) : 0; }

Node* newNode(int val) {
    Node *n = malloc(sizeof(Node));
    n->val = val; n->l = n->r = NULL; n->h = 1;
    return n;
}

/* insert */
Node* insert(Node *node, int val) {
    if (!node) return newNode(val);

    if (val < node->val) node->l = insert(node->l, val);
    else if (val > node->val) node->r = insert(node->r, val);
    else return node; // no duplicates

    node->h = 1 + max(height(node->l), height(node->r));
    int bf = balance(node);

    if (bf > 1 && val < node->l->val) return rightRotate(node);       // LL
    if (bf < -1 && val > node->r->val) return leftRotate(node);       // RR
    if (bf > 1 && val > node->l->val) { node->l = leftRotate(node->l); return rightRotate(node); } // LR
    if (bf < -1 && val < node->r->val) { node->r = rightRotate(node->r); return leftRotate(node); } // RL

    return node;
}

/* min value node */
Node* minValue(Node *n) {
    while (n->l) n = n->l;
    return n;
}

/* delete */
Node* delete(Node *node, int val) {
    if (!node) return NULL;

    if (val < node->val) node->l = delete(node->l, val);
    else if (val > node->val) node->r = delete(node->r, val);
    else {
        if (!node->l || !node->r) {
            Node *temp = node->l ? node->l : node->r;
            free(node);
            return temp;
        } else {
            Node *temp = minValue(node->r);
            node->val = temp->val;
            node->r = delete(node->r, temp->val);
        }
    }

    node->h = 1 + max(height(node->l), height(node->r));
    int bf = balance(node);

    if (bf > 1 && balance(node->l) >= 0) return rightRotate(node);       // LL
    if (bf > 1 && balance(node->l) < 0) { node->l = leftRotate(node->l); return rightRotate(node); } // LR
    if (bf < -1 && balance(node->r) <= 0) return leftRotate(node);       // RR
    if (bf < -1 && balance(node->r) > 0) { node->r = rightRotate(node->r); return leftRotate(node); } // RL

    return node;
}

/* traversals */
void inorder(Node *n) { if (n) { inorder(n->l); printf("%d ", n->val); inorder(n->r); } }
void preorder(Node *n) { if (n) { printf("%d(h=%d) ", n->val, n->h); preorder(n->l); preorder(n->r); } }

int main() {
    int keys[] = {10, 20, 30, 40, 50, 25};
    for (int i = 0; i < 6; i++) root = insert(root, keys[i]);

    printf("Inorder:\n"); inorder(root); printf("\nPreorder:\n"); preorder(root); printf("\n");

    root = delete(root, 40);
    printf("After deleting 40:\n"); inorder(root); printf("\nPreorder:\n"); preorder(root); printf("\n");

    return 0;
}
