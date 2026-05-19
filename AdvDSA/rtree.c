#include <stdio.h>
#include <stdlib.h>

#define MAX 3
#define MIN 1

typedef struct Rect {
    int xmin, ymin, xmax, ymax;
} Rect;

typedef struct Node {
    int count;
    Rect rect[MAX];
    struct Node *child[MAX];
    int leaf;
} Node;

Node* createNode(int leaf) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->count = 0;
    node->leaf = leaf;

    for(int i=0;i<MAX;i++)
        node->child[i] = NULL;

    return node;
}

Rect combine(Rect a, Rect b) {
    Rect r;
    r.xmin = (a.xmin < b.xmin) ? a.xmin : b.xmin;
    r.ymin = (a.ymin < b.ymin) ? a.ymin : b.ymin;
    r.xmax = (a.xmax > b.xmax) ? a.xmax : b.xmax;
    r.ymax = (a.ymax > b.ymax) ? a.ymax : b.ymax;
    return r;
}

int area(Rect r) {
    return (r.xmax - r.xmin) * (r.ymax - r.ymin);
}

int enlargement(Rect r, Rect newRect) {
    Rect c = combine(r,newRect);
    return area(c) - area(r);
}

int chooseLeaf(Node *node, Rect r) {
    int best = 0;
    int min = enlargement(node->rect[0], r);

    for(int i=1;i<node->count;i++) {
        int e = enlargement(node->rect[i], r);
        if(e < min) {
            min = e;
            best = i;
        }
    }
    return best;
}

void splitNode(Node *node, Rect r) {
    node->rect[node->count] = r;
    node->count++;
}

void insert(Node *node, Rect r) {

    if(node->leaf) {

        if(node->count < MAX) {
            node->rect[node->count++] = r;
        }
        else {
            printf("Node overflow → split required\n");
            splitNode(node,r);
        }
    }

    else {

        int index = chooseLeaf(node,r);
        insert(node->child[index], r);
        node->rect[index] = combine(node->rect[index], r);
    }
}

void printTree(Node *node) {

    for(int i=0;i<node->count;i++) {

        printf("Rectangle %d: (%d,%d) to (%d,%d)\n",
        i+1,
        node->rect[i].xmin,
        node->rect[i].ymin,
        node->rect[i].xmax,
        node->rect[i].ymax);
    }
}

int main() {

    Node *root = createNode(1);

    Rect r1 = {1,1,2,2};
    Rect r2 = {3,3,4,4};
    Rect r3 = {5,5,6,6};
    Rect r4 = {2,4,3,5};

    insert(root,r1);
    insert(root,r2);
    insert(root,r3);
    insert(root,r4);

    printTree(root);

    return 0;
}
