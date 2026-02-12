#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int val;
    struct Node *parent;
    struct Node *left;
    struct Node *right;
    bool colur; // 0 = black, 1 = red
} Node;

Node *root = NULL;

Node* leftrotate(Node* q) {
    Node* t = q->right;
    if (!t) return q;
    q->right = t->left;
    if (t->left) t->left->parent = q;
    t->parent = q->parent;
    if (q->parent) {
        if (q == q->parent->left) {
            q->parent->left = t;
        } else {
            q->parent->right = t;
        }
    } else {
        root = t;
    }
    t->left = q;
    q->parent = t;
    return t;
}

Node* rightrotate(Node* q) {
    Node* t = q->left;
    if (!t) return q;
    q->left = t->right;
    if (t->right) t->right->parent = q;
    t->parent = q->parent;
    if (q->parent) {
        if (q == q->parent->left) {
            q->parent->left = t;
        } else {
            q->parent->right = t;
        }
    } else {
        root = t;
    }
    t->right = q;
    q->parent = t;
    return t;
}

Node* insert(Node *node, int val, Node **inserted) {
    if (node == NULL) {
        Node *p = (Node *) malloc(sizeof(Node));
        p->val = val;
        p->parent = NULL;
        p->colur = 1; // new node is red
        p->left = NULL;
        p->right = NULL;
        *inserted = p;
        return p;
    }
    if (val < node->val) {
        node->left = insert(node->left, val, inserted);
        node->left->parent = node;
    } else {
        node->right = insert(node->right, val, inserted);
        node->right->parent = node;
    }
    return node;
}

void fixInsert(Node *node) {
    while (node->parent && node->parent->colur == 1) {
        Node *gp = node->parent->parent;
        if (!gp) break;
        if (node->parent == gp->left) {
            Node* uncle = gp->right;
            if (uncle && uncle->colur == 1) {
                node->parent->colur = 0;
                uncle->colur = 0;
                gp->colur = 1;
                node = gp;
            } else {
                if (node == node->parent->right) {
                    node = node->parent;
                    leftrotate(node);
                }
                node->parent->colur = 0;
                gp->colur = 1;
                rightrotate(gp);
            }
        } else {
            Node* uncle = gp->left;
            if (uncle && uncle->colur == 1) {
                node->parent->colur = 0;
                uncle->colur = 0;
                gp->colur = 1;
                node = gp;
            } else {
                if (node == node->parent->left) {
                    node = node->parent;
                    rightrotate(node);
                }
                node->parent->colur = 0;
                gp->colur = 1;
                leftrotate(gp);
            }
        }
    }
    root->colur=0;
}

Node* i(Node* node, int val) {
    Node* inserted = NULL;
    root = insert(node, val, &inserted);
    if (inserted->parent == NULL) inserted->colur=0; // first node black
    fixInsert(inserted);
    return root;
}

void display(Node *root) {
    if (root == NULL) return;
    printf("%d(%s) ", root->val, root->colur ? "R" : "B");
    display(root->left);
    display(root->right);
}

int main() {
    root = i(root, 10);
    root = i(root, 20);
    root = i(root, 5);
    display(root);
    return 0;
}