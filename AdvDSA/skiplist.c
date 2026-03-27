#include <stdio.h>
#include <stdlib.h>
# define level 16
typedef struct Node {
    int value;
    struct Node* forward[level];
    int key; // Array of forward pointers
} Node;
int currLevel=0;
Node * head;
Node * newNode(int level, int key)
{ Node *ptr=(Node *)malloc(sizeof(Node));
    ptr->key=key;
    ptr->value=1;
    currLevel=1;
return ptr;
}

int main()
{
    return 0;
}